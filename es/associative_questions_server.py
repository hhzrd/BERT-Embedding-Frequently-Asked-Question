# coding=UTF-8
'''
@Author: xiaoyichao
LastEditors: xiaoyichao
@Date: 2020-06-12 08:15:51
LastEditTime: 2021-06-06 23:29:05
@Description: 
'''
from sanic import Sanic
import sanic
import configparser
import os
import sys
os.chdir(sys.path[0])
sys.path.append("../")
from es.es_search_cn import SearchData4Association
from common.response_add_head import res_with_head


dir_name = os.path.abspath(os.path.dirname(__file__))
search_data = SearchData4Association()




def kill_port(port):

    find_kill = "kill -9 $(lsof -i:%d -t)" % port
    print(find_kill)
    result = os.popen(find_kill)
    return result.read()


# 接口会返回json数据
app = Sanic()
app = Sanic("associative questions")


@app.route("/associative_questions", methods=["POST", "HEAD"])
async def associative_questions(request):

    # 接收到的参数
    current_question = str(request.form.get("current_question"))
    limit_num = int(request.form.get("limit_num"))
    owner_name = str(request.form.get("owner_name"))
    if_middle = int(request.form.get("if_middle", default=1))
    if if_middle == 1:
        if_middle = True
    if if_middle == 0:
        if_middle = False
    else:
        if_middle = True

    maybe_original_questions = search_data.search_question_cn(
        owner_name=owner_name, current_question=current_question, limit_num=limit_num, if_middle=if_middle)

    answer_json = {}
    answer_json["code"] = "1"
    answer_json["msg"] = "OK"
    answer_json["data"] = {
        "message": maybe_original_questions}
    return res_with_head(answer_json)


@app.route("/", methods=["GET", "HEAD"])
async def alibaba_operator_check(request):
    print("alibaba SLB checking server status")
    return sanic.response.text(200)


if __name__ == "__main__":
    root_config = configparser.ConfigParser()
    root_config.read(os.path.join(
        dir_name, "associative_questions_config.ini"))

    kill_port(int(root_config["ServerAddress"]["port"]))

    app.run(host="0.0.0.0"
            port=int(root_config["ServerAddress"]["port"]),
            workers=int(root_config["ServerInfo"]["work_number"]),
            debug=True, access_log=True)

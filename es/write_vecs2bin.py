# coding=UTF-8
'''
@Author: xiaoyichao
LastEditors: xiaoyichao
@Date: 2020-01-02 16:55:23
LastEditTime: 2021-06-25 15:27:08
@Description: 将问题的集合的向量写入bin文件

'''


import numpy as np
from read_excel import ExcelData
import os
import sys
os.chdir(sys.path[0])
sys.path.append("../")
from bert_server.sentence_bert_server import SentenceBERT


dir_name = os.path.abspath(os.path.dirname(__file__))


class WriteVec2bin(object):
    def __init__(self):
        self.exceldata = ExcelData()
        self.excel_list = self.exceldata.read_QA_data()
        self.sheet_names = self.exceldata.get_sheet_names()
        self.sentenceBERT = SentenceBERT()

    def write_bert_vecs(self, owner_name, num):
        '''
        @Author: xiaoyichao
        @param {type}
        @Description: 句向量都进行写入bin文件
        '''
        if os.path.exists(os.path.join(dir_name, '../faq/bert_vect')) is False:
            os.mkdir(os.path.join(dir_name, '../faq/bert_vect'))
        bert_vecs_path = os.path.join(
            dir_name, '../faq/bert_vect/%s_bert_vecs.npy' % (owner_name))
        bert_sentences_path = os.path.join(
            dir_name, '../faq/bert_vect/%s_bert_sentences.txt' % (owner_name))
        orgin_query_vecs = np.zeros(shape=(1, 512))
        with open(bert_sentences_path, "w") as f:
            f.write("数据库中的问题"+"\n")
            for info in self.excel_list[num]:
                original_question = info[1]
                f.write(original_question+"\n")
                orgin_query = original_question.replace("，", " ")
                orgin_query_list = orgin_query.split(' ')
                orgin_query_vec = self.sentenceBERT.get_bert(orgin_query_list)
                orgin_query_vecs = np.concatenate(
                    (orgin_query_vecs, orgin_query_vec), axis=0)
            if os.path.exists(bert_vecs_path):
                os.remove(bert_vecs_path)
                print("删除旧的BERT向量文件")
            # 将铺平的向量reshape
            orgin_query_vecs = np.reshape(orgin_query_vecs, (-1, 512))
            np.save(bert_vecs_path, orgin_query_vecs)

        print("BERT向量文件写入", bert_vecs_path)

    def write_bert_vecs4sheets(self):
        '''
        Author: xiaoyichao
        param {type}
        Description: 对每个领域语料的句向量都进行写入bin文件的操作
        '''
        for i, sheet_name in enumerate(self.sheet_names):
            self.write_bert_vecs(owner_name=sheet_name, num=i)


if __name__ == "__main__":
    write_vec2bin = WriteVec2bin()
    write_vec2bin.write_bert_vecs4sheets()

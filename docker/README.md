# docker 方式启动程序

## 1、启动docker集群
    首先请根据自己的系统安装docker-compose，然后才能启动docker-compose。
    交互方式启动
    docker-compose up
    后台方式启动
    docker-compose up -d
    如果想要停止docker-compose
    docker-compose stop
## 2、进入BEFAQ的doker
    Es相关的测试数据已经写到了Es的docker内。如果需要更新数据，请参考项目根目录下的README.md
    进入befaq的docker
    docker exec -it befaq /bin/bash
## 3、启动BEFAQ服务
    进入项目根目录
    cd /projects/BERT-Embedding-Frequently-Asked-Question/
    进入faq文件夹
    cd faq
    python main_faq.py
    或者在后台中启动
    nohup python -u main_faq.py > "logs/log$(date +"%Y-%m-%d-%H").txt" 2>&1 &
## 4、启动BEFAQ的联想词接口服务
    cd /projects/BEFAQ
    cd es
    python associative_questions_server.py
    或者在后台中启动
    nohup python -u associative_questions_server.py >/dev/null 2>&1 &
## 5、测试接口
    请参考项目根目录下的README.md
    




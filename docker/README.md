# docker 方式启动程序

## 启动docker集群
    进入根目录下的docker文件夹
    交互方式启动
    docker-compose up
    后台方式启动
    docker-compose up -d
    停止docker-compose
    docker-compose stop
## 进入BEFAQ的doker并启动服务
    Sentence BERT模型 已经下载到docker内, Es相关的测试数据也写到了Es的docker内。如果需要更新数据，请参考项目根目录下的README.md
    进入befaq docker
    docker exec -it befaq /bin/bash
    进入项目根目录
    cd /projects/BEFAQ
    拉取最新的项目代码
    git pull
### 启动BEFAQ服务
    进入faq文件夹
    cd faq
    python main_faq.py
    或者在后台中启动
    nohup python -u main_faq.py > "logs/log$(date +"%Y-%m-%d-%H").txt" 2>&1 &
### 启动BEFAQ的联想词接口服务
    cd /projects/BEFAQ
    cd es
    python associative_questions_server.py
    或者在后台中启动
    nohup python -u associative_questions_server.py >/dev/null 2>&1 &
### 测试接口
    请参考项目根目录下的README.md
    




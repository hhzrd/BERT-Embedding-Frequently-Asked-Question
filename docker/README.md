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
    下载项目到/projects文件下
## 3、sentence-transformers 多语言预训练模型的下载
    进入项目根目录后，
    cd model
    wget https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/v0.2/distiluse-base-multilingual-cased.zip
    unzip distiluse-base-multilingual-cased.zip
    如果最新的模型报错，请到百度网盘中下载
## 4、启动BEFAQ服务
    进入faq文件夹
    cd faq
    python main_faq.py
    或者在后台中启动
    nohup python -u main_faq.py > "logs/log$(date +"%Y-%m-%d-%H").txt" 2>&1 &
## 5、启动BEFAQ的联想词接口服务
    cd /projects/BEFAQ
    cd es
    python associative_questions_server.py
    或者在后台中启动
    nohup python -u associative_questions_server.py >/dev/null 2>&1 &
## 6、测试接口
    请参考项目根目录下的README.md
    




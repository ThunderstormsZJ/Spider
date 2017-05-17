# Twitter Spider 
- 爬取推特人物信息
- 爬取推推文

> ### 本项目依赖
-  Redis
-  代理
    ```
    #代理设置(最好使用墙外代理IP池,可减少重定向次数)
    PROXIES = [
        {'ip_port': '127.0.0.1:1087','user_pass':None},
    ]
    ```

> ### 使用scrapyd 管理爬虫
* #### 安装scrapyd并运行
    文档：[Scrapyd Document](http://scrapyd.readthedocs.io/en/stable/overview.html)
    ```
    pip install scrapy
    scrapyd
    ```
    Web界面：http://localhost:6800/
    
* #### 部署scrapy 项目
    文档：[Scrapyd Chient](https://github.com/scrapy/scrapyd-client)
    ```
    pip install scrapyd-client
    scrapyd-deploy
    ```
* ### API
    开启爬虫 schedule
    ```
    curl http://localhost:6800/schedule.json -d project=[project name] -d spider=[spider name]
    ```
    停止 cancel
    ```
    curl http://localhost:6800/cancel.json -d project=tutorial -d job=[job id]
    ```
    列出爬虫
    ```
    curl http://localhost:6800/listspiders.json?project=[project name]
    ```
    删除项目
    ```
    curl http://localhost:6800/delproject.json -d project=[project name]
    ```

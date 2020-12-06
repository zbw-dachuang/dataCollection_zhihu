## 知乎给定话题下问题和回答信息爬取

#### 写在前面

本项目主要用于对知乎给定话题下的问题的基本信息，以及这些问题的所对应的回答的基本信息进行收集
由于本人能力有限，代码的封装程度不高，重用性不强，希望之后可以有所改进。

- 下面对每个文件进行说明：
  - dataBase_Readme.txt # 数据库类说明文件 包含数据库建表语言
  - dataExplain_Readme.txt # 数据解析类说明文件
  - http_fake.py # 请求头伪装
  - dataBase.py # 数据库操作封装类
  - data_explain.py # 数据解析封装类
  - questionCollect.py  # 给定话题下问题基本信息收集
  - questionDetail.py # 问题细节收集
  - answerCollect.py # 回答基本信息收集

- 注意事项
  - 本项目是从话题入手获取问题信息
  - questionCollect（问题基本信息收集）中的main函数必须最先执行
  - questionDetail和answerCollect可以随意顺序

- 使用接口
  - questionCollect中可设置话题ID
  - 自定义数据库连接信息
# _*_ coding:utf-8 _*_
import requests
import dataBase
import http_fake
import data_explain
import json
# 写在前面
# 该程序主要用于将知乎中固定话题ID问题的信息收集下来
# 所对应的数据库中表的名称为COVID_question

# 启动爬虫
def main():

    # 构建数据库类，完成数据库连接
    # 此处需要填写自己的数据库的名称、用户名和密码
    db = dataBase.dataBase(host='127.0.0.1', port=3306, user='root',
                           password='123456', db='zhihu', charset='utf8')
    # 构建数据解析类
    de = data_explain.explain_data(db)

    # 自定义所要收集话题的ID
    topicID = '21246026'
    # 构建动态的URL
    url_COIVD_question = "http://www.zhihu.com/api/v4/topics/"+topicID+"/feeds/timeline_question?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0"
    # 开始循环收集
    cirData_get(de, url_COIVD_question)



# 循环获取、解析、存储数据
def cirData_get(de, url):
        nexturl = url
        while nexturl:
            response_data = getData(nexturl)
            nexturl = de.explain_data_question(response_data=response_data)
        return "close!"


# 获取响应数据
def getData(xpath):
    response = requests.get(xpath, headers = http_fake.UA_fake())
    data_json = response.json()
    return data_json


if __name__ == '__main__':

    main()











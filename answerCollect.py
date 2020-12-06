# _*_ coding:utf-8 _*_

# 这个部分是对于问题回答内容的爬取。
# 希望通过对于一个热门问题下的多个内容的获取以及分析，从而判断出回答内容的影响

import requests
from lxml import etree
import time
import random
import pandas as pd

# 自定义py调用
import dataBase
import http_fake
import data_explain

def main():

    # 构建数据库类，完成数据库连接
    # 此处需要填写自己的数据库的名称、用户名和密码
    db = dataBase.dataBase(host='127.0.0.1', port=3306, user='root',
                           password='123456', db='zhihu', charset='utf8')
    # 构建数据解析类
    de = data_explain.explain_data(db)

    # 获取需要回答信息的问题ID
    question_id = db.getQuestionId_Answer()
    result = pd.DataFrame(list(question_id))
    result.columns = ['question_id']

    # 按照问题的ID依次获取回答信息并解析存储
    for i in range(1, len(result['question_id'])):
        print(i)
        print(result['question_id'][i])
        URL = 'https://www.zhihu.com/api/v4/questions/'+ result['question_id'][i] +'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics%3Bsettings.table_of_content.enabled%3B&limit=5&offset=0&platform=desktop&sort_by=default'

        if(i%100 == 0):
            time.sleep(random.uniform(0,1)*50) # 每隔一定时间休息较长一段时间

        cirData_get_explain(URL, "get",de,"json")


# 循环获取
def cirData_get_explain(nexturl, getStyle, de, label):

    ## 第一次请求，判断是否成功
    response_data = getData_first(nexturl,getStyle, label=label)
    if(response_data == "error"):
        return "close!"
    else:
        nexturl = de.explain_data_answer(response_data)
    while nexturl:
        response_data = getData(nexturl,getStyle, label=label)
        nexturl = de.explain_data_answer(response_data)
    return "close!"

# 获取数据
# label 表示标签
# label - 'HTML' 获取HTML数据
# label - 'json' 获取json数据

# 用于第一次请求网页判断是否网页为空
def getData_first(url, getStyle, label):
    if(getStyle=="get"):
        response = requests.get(url = url, cookies = http_fake.Cookie(), headers = http_fake.UA_fake())
        if(response.status_code != 200):
            return "error"
        else:
            time.sleep(random.uniform(0,1))
    if(getStyle=="post"):
        response = requests.post(url = url, cookies = http_fake.Cookie(), headers = http_fake.UA_fake())
    if(label=="HTML"):
        return response.text
    if(label=="json"):
        return response.json()

def getData(url, getStyle,label):  # 用于之后网页请求判断
    if(getStyle=="get"):
        response = requests.get(url = url, cookies = http_fake.Cookie(), headers = http_fake.UA_fake())
        time.sleep(random.uniform(0,1))
    if(getStyle=="post"):
        response = requests.post(url = url, cookies = http_fake.Cookie(), headers = http_fake.UA_fake())
    if (label == "HTML"):
        return response.text
    if (label == "json"):
        return response.json()


# 执行
if __name__ == '__main__':
    main()
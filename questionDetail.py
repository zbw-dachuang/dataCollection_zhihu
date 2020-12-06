# _*_ coding:utf-8 _*_

# 对于知乎新冠肺炎下的每个问题进行具体的分析

import pandas as pd
import requests
from lxml import etree
import time
import random
import dataBase
import http_fake
import data_explain

def main():

    # 连接数据库
    db = dataBase.dataBase(host='127.0.0.1', port=3306, user='root',
                  password='123456', db='zhihu', charset='utf8')
    # 创建数据解析对象
    de = data_explain.explain_data(db)

    # 获取需要分析detail的问题ID
    result = pd.DataFrame(list(db.getId_MoreInfo()))
    result.columns = ['id']

    # 循环获取、分析、存储
    for item in range(len(result['id'])):
        test_id = result['id'][item]
        print(test_id)
        test_url = "https://www.zhihu.com/question/" + test_id
        response_data = getData(test_url,"get")
        base_info = de.explain_html_question_base_info(response_data)
        db.insertDB_label(base_info['label'], test_id)
        db.insertDB_like_count(base_info['like_count'], test_id)
        db.insertDB_look_count(base_info['look_count'], test_id)
        db.insertDB_question_create_time(base_info['question_create_time'], test_id)
        time.sleep(random.uniform(0,1))



def getData(url,getStyle):

    if (getStyle == 'get'):
        response = requests.get(url=url, cookies=http_fake.Cookie(), headers=http_fake.UA_fake())  # 发出请求
    if (getStyle == 'post'):
        response = requests.post(url=url,cookies=http_fake.Cookie(), headers=http_fake.UA_fake())  # 发出请求
    response_data = response.text  # 获取页面信息
    return response_data




if __name__ == '__main__':
    main()
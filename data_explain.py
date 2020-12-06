# _*_ coding:utf-8 _*_
import dataBase
from lxml import etree
import time

# 这部分是对于数据的解析使用，包含有HTML解析和页面动态解析
# 包含有对问题和回答的解析


class explain_data:

    def __init__(self,db):

        self.db = db

    # 解析问题HTML页面的前两条回答
    def explain_html_question_answer(self,response_data):

        # 获取HTML界面上的两条回答
        # 根部节点
        html = etree.HTML(response_data)
        # 展示数量
        mm = html.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[1]')
        # 回答者姓名
        answer_name = html.xpath('//*[@id="Popover28-toggle"]/a/text()')
        # 回答者信息
        answer_info = html.xpath(
            '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[5]/div/div[1]/div[1]/div/div[2]/div/div/text()')
        # '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div'
        # 回答的点赞数
        support_number = html.xpath(
            '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[5]/div/div[1]/div[3]/span/span/button/text()')
        # 回答建立的时间
        create_time = html.xpath(
            '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[5]/div/div[2]/div[2]/div/a/span/@data-tooltip')
        # 评论数量
        review_number = html.xpath(
            '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[5]/div/div[2]/div[3]/div/button[1]/text()')
        # '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[3]/button[1]'
        # 回答的内容
        review_text = html.xpath(
            '//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[5]/div/div[2]/div[1]/span/p[1]/text()')

        dataList = {
            'answer_name': answer_name,
            'answer_info': answer_info,
            'support_number': support_number,
            'create_time': create_time,
            'review_number': review_number,
            'review_text': review_text
        }
        return dataList

    # 解析问题HTML界面的基本信息，获取标签，浏览次数，问题具体说明，问题点赞数量
    def explain_html_question_base_info(self, response_data):
        # 根部节点
        html = etree.HTML(response_data)
        # 标签内容
        label = html.xpath('//*[@id="root"]/div/main/div/meta[3]/@content')
        # 点赞数
        like_count = html.xpath(
            '//button[@class = "Button GoodQuestionAction-commonBtn Button--plain Button--withIcon Button--withLabel"]/text()')
        # 被浏览次数
        look_count = html.xpath('//strong[@class = "NumberBoard-itemValue"]/text()')
        if (len(look_count) == 2):
            look_count = look_count[1]
        # 问题创造时间
        question_create_time = html.xpath('//meta[@itemprop = "dateCreated"]/@content')
        if (len(question_create_time) != 0):
            question_create_time = question_create_time[0]
        # 问题的具体说明
        dataList = {
            'label': label,
            'like_count': like_count,
            'look_count': look_count,
            'question_create_time': question_create_time
        }

        return dataList

    # 解析动态获取的问题数据，并插入数据库
    def explain_data_question(self,response_data):

        lst = response_data['data']
        next_url = response_data['paging']['next']
        if not lst:
            return;
        for item in lst:
            type = item['target']['type']
            if(type == 'question'):
                object_item = item['target'] # 获取每一个问题的信息
                author = object_item['author'] # 作者的信息

                # 问题基本信息
                id = object_item['id'] # 问题编号
                title = object_item['title'] # 问题具体标题
                answer_count = object_item['answer_count'] # 回答数量
                comment_count = object_item['comment_count'] # 评论数量
                follower_count = object_item['follower_count'] # 关注者数量

                question_type = object_item['question_type'] # 如果是问题，问题的类型
                object_url = object_item['url'] # 问题所对应的具体的网页地址

                # 作者信息
                author_name = author['name'] # 作者姓名
                author_gender = author['gender'] # 作者性别
                author_headline = author['headline'] # 作者标签
                is_advertiser = author['is_advertiser'] # 是否为广告商
                author_edu_member_tag = author['edu_member_tag']['member_tag'] # 作者教育标签

                # 存储数据
                self.db.insertDB_COVID_question(id ,title, answer_count, comment_count ,follower_count ,type ,question_type,object_url ,
                       author_name ,author_gender,author_headline,is_advertiser,author_edu_member_tag)

        return next_url

    # 解析动态获取的回答数据，并插入数据库
    def explain_data_answer(self, response_data):
        lst = response_data['data']
        next_url = response_data['paging']['next']
        if not lst:
            return;
        for item in lst:
            type = item['type']
            if (type == 'answer'):
                # 回答的基本信息
                answer_id = item['id']  # 回答编号
                create_time = self.change_time_style(item['created_time'])  # 创建时间
                update_time = self.change_time_style(item['updated_time'])  # 最后更新时间
                excerpt = item['excerpt']  # 回答的内容
                vote_number = item['voteup_count']  # 点赞数
                comment_number = item['comment_count']  # 评论数

                # 回答作者基本信息
                author = item['author']
                author_name = author['name']  # 作者姓名
                author_headline = author['headline']  # 作者标签
                author_label = author['badge_v2']['detail_badges']
                good_certification_description = None  # 优秀回答者证明描述
                certification_description = None  # 回答者证明描述
                # 回答者信息优秀认证
                if (len(author_label) == 2):
                    # 这种情况说明具有优秀认证
                    good_certification = author_label[0]
                    good_certification_description = good_certification['description']
                    certification = author_label[1]
                    certification_description = certification['description']
                if (len(author_label) == 1):
                    # 这种情况只有回答者认证
                    mm = author_label[0]
                    certification_description = mm['description']

                # 回答所对应的问题的基本信息
                question = item['question']
                question_title = question['title']  # 回答对应问题标题
                question_id = question['id']  # 回答问题编号
                # 存储数据
                self.db.insertDB_COVID_question_answer(answer_id, create_time, update_time, excerpt, vote_number, comment_number,
                                                     author_name, author_headline, good_certification_description,
                                                     certification_description,
                                                     question_id, question_title)

        return next_url

    # 对日期数据进行转化
    def change_time_style(self,now):
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime
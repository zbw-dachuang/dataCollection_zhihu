# _*_ coding:utf-8 _*_

# 该py文件主要用于将数据库的操作进行封装
# 使用class定义相关的行为和属性
# 对于数据库的具体描述在dataBase_Readme的文件中，如果需要了解细节，请看该文件
import pymysql

class dataBase:

    ## 数据库初始化
    def __init__(self, host, port, user, password, db,charset):
        self.host= host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.db_connect = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                          password=self.password, db=self.db,charset=self.charset)
        self.cursor = self.db_connect.cursor()

    # 向新冠肺炎的问题表(COVID_question)中插入数据
    def insertDB_COVID_question(self,id, title, answer_count, comment_count, follower_count, type, question_type, object_url,
                       author_name, author_gender, author_headline, is_advertiser, author_edu_member_tag):
        # insert data
        try:
            sql = "insert into COVID_question(id ,title, answer_count, comment_count ,follower_count ,type ,question_type,object_url ,author_name ,author_gender,author_headline,is_advertiser,author_edu_member_tag) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                  id, title, answer_count, comment_count, follower_count, type, question_type, object_url,
                  author_name, author_gender, author_headline, is_advertiser, author_edu_member_tag)
            self.cursor.execute(sql)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

        # 向问题表中插入数据(top_question)

    # 向新冠肺炎的回答表(COVID_question_answer)中插入数据
    def insertDB_COVID_question_answer(self, answer_id, create_time, update_time, excerpt, vote_number, comment_number,
                              author_name, author_headline, good_certification_description, certification_description,
                              question_id, question_title):
        # insert data
        try:
            sql = "insert into COVID_question_answer (answer_id,create_time,update_time ,excerpt," \
                  "vote_number,comment_number,author_name,author_headline,good_certification_description," \
                  "certification_description,question_id, question_title) " \
                  "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (answer_id, create_time, update_time, excerpt, vote_number, comment_number,
                   author_name, author_headline, good_certification_description, certification_description,
                   question_id, question_title)
            self.cursor.execute(sql)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

            # 获取问题的id 和 url的操作

        # 获取问题回答的id和对应问题的id

    # 向新冠肺炎的问题表(COVID_question)其中插入标签
    def insertDB_label(self,label, id):
        try:
            sql = "update COVID_question set label = %s where id = %s"
            val = (label,id)
            self.cursor.execute(sql,val)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

    # 向新冠肺炎的问题表(COVID_question)其中插入浏览次数
    def insertDB_look_count(self,look_count, id):
        try:
            sql = "update COVID_question set look_count = %s where id = %s"
            val = (look_count,id)
            self.cursor.execute(sql,val)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

    # 向新冠肺炎的问题表(COVID_question)其中插入点赞数量
    def insertDB_like_count(self,like_count, id):
        try:
            sql = "update COVID_question set like_count = %s where id = %s"
            val = (like_count,id)
            self.cursor.execute(sql,val)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

    # 向新冠肺炎的问题表(COVID_question)其中插入问题创建时间
    def insertDB_question_create_time(self, question_create_time, id):
        try:
            sql = "update COVID_question set question_create_time = %s where id = %s"
            val = (question_create_time, id)
            self.cursor.execute(sql, val)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

    # 向新冠肺炎的问题表(COVID_question)集体插入标签、浏览次数、点赞数量、创建时间
    def insertDB_update(self,label,look_count,like_count,question_create_time,id):
        try:
            sql = "update COVID_question set label = %s, like_count = %s, look_count = %s, question_create_time = %s where id = %s"
            val = (label,look_count,like_count,question_create_time,id)
            self.cursor.execute(sql,val)
            self.db_connect.commit()
        except Exception as e:
            self.db_connect.rollback()
            print(e)

    # 用于添加问题的回答信息的ID
    def getQuestionId_Answer(self):
        try:
            sql = "select id from COVID_question where id not in (select DISTINCT(question_id) from COVID_question_answer)"
            self.cursor.execute(sql)
            self.db_connect.commit()
            result = self.cursor.fetchall()
        except Exception as e:
            self.db_connect.rollback()
            print(e)
        return result

    # 获取未查询详细信息的问题ID
    def getId_MoreInfo(self):
        try:
            sql = "select id from COVID_question where question_create_time is null"
            self.cursor.execute(sql)
            self.db_connect.commit()
            result = self.cursor.fetchall()
        except Exception as e:
            self.db_connect.rollback()
            print(e)
        return result

    # 断开数据库链接
    def dataBase_close(self):
        self.cursor.close()
        self.db_connect.close()
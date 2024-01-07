# coding:utf-8
from django.db import connections, transaction
import logging
'''执行django原始sql语句 并返回一个列表对象'''
def execute_query(env_d,sql):
    logger = logging.getLogger('django')


    try:
        if env_d == 'test':
        #连接服务器
            connection = connections["test"]
        elif env_d=='default':
            connection = connections["default"]
        else:
            connection = connections["dev"]



        cursor = connection.cursor() # 获得一个游标(cursor)对象
        cursor.execute(sql)
        rawData = cursor.fetchall()

        col_names = [desc[0] for desc in cursor.description]
        result = []
        for row in rawData:

            objDict = {}
            # 把每一行的数据遍历出来放到Dict中
            for index, value in enumerate(row):
                objDict[col_names[index]] = value

            result.append(objDict)

        #关闭游标
        cursor.close()

        # 关闭数据库连接
        connection.close()
        return result
    except Exception as e:
        logger.error(e)
'''执行django原始sql语句 并返回原始'''

def other_query(env_d,sql):
    logger = logging.getLogger('django')

    try:

        if env_d == 'test':
            #连接服务器
            connection = connections["test"]
            cursor = connection.cursor() # 获得一个游标(cursor)对象
            cursor.execute(sql)
            rawData = cursor.fetchall()
            print(rawData)

            #关闭游标
            cursor.close()

            # 关闭数据库连接
            connection.close()
            return rawData
        elif env_d == 'default':
            #连接服务器
            connection = connections["default"]
            cursor = connection.cursor() # 获得一个游标(cursor)对象
            cursor.execute(sql)
            rawData = cursor.fetchall()
            print(rawData)

            #关闭游标
            cursor.close()

            # 关闭数据库连接
            connection.close()
            return rawData
        else:
            # 连接服务器
            connection = connections["dev"]
            cursor = connection.cursor()  # 获得一个游标(cursor)对象
            cursor.execute(sql)
            rawData = cursor.fetchall()
            print(rawData)

            # 关闭游标
            cursor.close()

            # 关闭数据库连接
            connection.close()
            return rawData


    except Exception as e:
        logger.error(e)

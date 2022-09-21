#!/usr/bin/env python
# coding=utf-8
import traceback
import mysql
from mysql import connector
from mysql.connector import pooling
from globals import g_logger


class MySQLPool(object):
    """
    MySQL连接池,帮助管理连接的建立和关闭
    note: 异常处理规则如下
    构造函数发生错误时,抛出异常,使程序停止运行
    具体数据库访问发生错误时,内部处理异常并输出日志,使程序继续运行
    """
    def __init__(self, host='127.0.0.1', port='3306', user='root', password='123456', database='test',
                 pool_name='mypool', pool_size=5):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

        self.dbconfig = {'host': self._host, 'port': self._port, 'user': self._user, 'password': self._password,
                         'database': self._database}

        self.pool = self.create_pool(pool_name=pool_name, pool_size=pool_size)

    def create_pool(self, pool_name='mypool', pool_size=5):
        """
        创建连接池
        :param pool_name: 连接池名称
        :param pool_size: 连接池最大连接数
        :return:
        """
        pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size,
                                                           pool_reset_session=True, **self.dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        关闭cursor, 将连接归还到连接池
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        执行一条sql.支持通过查询参数的方式执行.
        :param sql:
        :param args: sql中需要的参数
        :param commit: 是否执行commit
        :return: 返回一个元组(boolean, list)
                boolean: 发生错误时为False,否则为True
                list:    查询结果集. commit时为None
        """
        success = False
        result_set = None
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        try:
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            g_logger.debug('statement: %s' % cursor.statement)

            if commit:
                conn.commit()
            else:
                result_set = cursor.fetchall()
            success = True
        except Exception as e:
            g_logger.error(traceback.format_exc())
            g_logger.error(e)
            g_logger.error('sql: %s, args: %s' % (sql, str(args)))
        finally:
            self.close(conn, cursor)
            return success, result_set

    def execute_many(self, sql, args, commit=False):
        """
        遍历args,为每一个arg执行一次sql语句.
        :param sql:
        :param args: 用于执行多次sql的参数列表,类型为list
        :param commit: 是否执行commit
        :return: 返回一个元组(boolean, list)
                boolean: 发生错误时为False,否则为True
                list:    查询结果集. commit时为None
        """
        success = False
        result_set = None
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, args)
            for arg in args:
                g_logger.debug('%s args:%s' % (sql, str(arg)))

            if commit:
                conn.commit()
            else:
                result_set = cursor.fetchall()
            success = True
        except Exception as e:
            g_logger.error(traceback.format_exc())
            g_logger.error(e)
            g_logger.error('sql: %s, args: %s' % (sql, str(args)))
        finally:
            self.close(conn, cursor)
            return success, result_set

#!/usr/bin/env python
# coding=utf-8
from .Logger import Logger
from .MySQLPool import MySQLPool
from .Errors import ProjectBaseError
from .config import PRODUCTION, DEBUG
from .globals import g_cfg, g_logger, g_mysql_conn_pool_map

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_mysql_conn_pool(db_name):
    """
    获取全局保存的对应数据库pool对象,不存在时则先创建pool对象
    db_name: 对应于config.py中配置对象db中的keys
    """
    global g_mysql_conn_pool_map

    if db_name in g_mysql_conn_pool_map:
        return g_mysql_conn_pool_map[db_name]
    else:
        return MySQLPool(**g_cfg['db'][db_name])

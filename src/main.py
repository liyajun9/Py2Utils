#!/usr/bin/env python
# coding=utf-8
from utils import g_cfg, g_logger, get_mysql_conn_pool, ProjectBaseError


if __name__ == '__main__':
    global g_logger
    g_logger.reinit(**g_cfg['auto_import_device_log'])
    try:
        sql = '''select * from t_user where user_id = %d''' % 1001
        pool = get_mysql_conn_pool('my_database')
        success, result_set = pool.execute(sql)
        if success:
            for row in result_set:
                g_logger.info(str(row))
        else:
            g_logger.error('execute sql failed: %s' % sql)
    except ProjectBaseError as e:
        g_logger.error(e)

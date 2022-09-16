#!/usr/bin/env python
# coding=utf-8
import logging

# 生产环境的配置
PRODUCTION = {
    'main_log': {
        'logger_name': 'root',
        'log_level': logging.INFO,
        'log_format': '[%(asctime)s] %(levelname)s at %(filename)s:%(lineno)d %(message)s',
        'log_file': '/data/project/project.log',
        'max_bytes': 100 * 1024 * 1024,
        'backup_count': 10,
        'encoding': 'utf-8'
    },
    'other_log': {
        'logger_name': 'other',
        'log_level': logging.DEBUG,
        'log_format': '[%(asctime)s] %(levelname)s at %(filename)s:%(lineno)d %(message)s',
        'log_file': '/data/project/other.log',
        'max_bytes': 100 * 1024 * 1024,
        'backup_count': 50,
        'encoding': 'utf-8'
    },
    'db': {
        'my_database': {'host': '127.0.0.1', 'port': '3306', 'user': 'root', 'password': '123456', 'database': 'data'}
    }
}

# 测试环境的配置: 将与生产环境不同的配置写在下面
DEBUG = dict(PRODUCTION)
DEBUG['main_log']['other_log'] = logging.DEBUG



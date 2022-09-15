#!/usr/bin/env python
# coding=utf-8
import logging

# 生产环境的配置
PRODUCTION = {
    'log': {
        'logger_name': 'root',
        'log_level': logging.INFO,
        'log_format': '[%(asctime)s] %(levelname)s in %(filename)s:%(lineno)d %(message)s',
        'log_file': 'var/log/manage.log',
        'max_bytes': 100 * 1024 * 1024,
        'backup_count': 10,
        'encoding': 'utf-8'
    }
}

# 测试环境的配置: 将与生产环境不同的配置写在下面
TEST = dict(PRODUCTION)
TEST['log']['log_level'] = logging.DEBUG

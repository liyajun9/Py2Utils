#!/usr/bin/env python
# coding=utf-8

import logging
from logging.handlers import RotatingFileHandler


class Logger(object):
    def __init__(self, logger_name='root', log_level=logging.INFO,
                 log_format='[%(asctime)s] %(levelname)s in %(filename)s:%(lineno)d %(message)s',
                 log_file='var/log/manage.log', max_bytes=100*1024*1024,
                 backup_count=10, encoding='utf-8'):
        self.logger = logging.getLogger(logger_name)
        self.handler = RotatingFileHandler(log_file, mode='a', maxBytes=max_bytes, backupCount=backup_count,
                                           encoding=encoding, delay=False)
        self.handler.setFormatter(logging.Formatter(log_format))
        self.logger.setLevel(log_level)
        self.logger.addHandler(self.handler)

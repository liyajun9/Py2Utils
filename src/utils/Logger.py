#!/usr/bin/env python
# coding=utf-8

import logging
from logging.handlers import RotatingFileHandler


class Logger(logging.Logger):
    def __init__(self, logger_name='root', log_level=logging.INFO,
                 log_format='[%(asctime)s] %(levelname)s at %(filename)s:%(lineno)d %(message)s',
                 log_file='var/log/manage.log', max_bytes=100 * 1024 * 1024,
                 backup_count=10, encoding='utf-8'):
        logging.Logger.__init__(self, logger_name, log_level)
        self.formatter = logging.Formatter(fmt=log_format)
        self.handler = RotatingFileHandler(log_file, mode='a', maxBytes=max_bytes, backupCount=backup_count,
                                           encoding=encoding, delay=False)
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

    def reinit(self, logger_name='root', log_level=logging.INFO,
               log_format='[%(asctime)s] %(levelname)s at %(filename)s:%(lineno)d %(message)s',
               log_file='var/log/manage.log', max_bytes=100 * 1024 * 1024,
               backup_count=10, encoding='utf-8'):
        logging.Logger.__init__(self, logger_name, log_level)
        self.formatter = logging.Formatter(fmt=log_format)
        self.handler = RotatingFileHandler(log_file, mode='a', maxBytes=max_bytes, backupCount=backup_count,
                                           encoding=encoding, delay=False)
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

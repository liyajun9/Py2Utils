#!/usr/bin/env python
# coding=utf-8

import config
import Logger

g_cfg = config.DEBUG  # 在此处选择不同配置

g_logger = Logger.Logger(**g_cfg['main_log'])

g_mysql_conn_pool_map = {}

#!/usr/bin/env python
# coding=utf-8
from src.utils.Logger import Logger
from . import config

g_logger = Logger(**config.TEST['log'])

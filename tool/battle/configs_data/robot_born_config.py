# -*- coding:utf-8 -*-
"""
created by sphinx on 15/10/14.
"""

from common_item import CommonItem


class RobotBornConfig(object):
    def __init__(self):
        self._items = {}

    def parser(self, config_value):
        for row in config_value:
            item = CommonItem(row)
            self._items[item.id] = item

        return self._items
# -*- coding:utf-8 -*-
"""
author:dotahero
"""

from shared.db_opear.configs_data.common_item import CommonItem

class TaskType:
    ACHIEVE = 1
    LIVELY = 2
    LIVELY_REWARD = 3
    
class AchievementConfig(object):
    def __init__(self):
        self._items = {}

    def parser(self, config_value):
        for row in config_value:
            item = CommonItem(row)
            if item.sort == TaskType.LIVELY or item.sort == TaskType.LIVELY_REWARD:
                self._items[item.id] = item
        return self._items
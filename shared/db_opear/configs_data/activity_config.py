# -*- coding:utf-8 -*-
"""
created by server on 14-8-25
"""

from shared.db_opear.configs_data.common_item import CommonItem
from shared.db_opear.configs_data.data_helper import parse


class ActivityConfig(object):
    def __init__(self):
        self._items = {}

    def parser(self, config_value):
        for row in config_value:
            row["reward"] = parse(row.get("reward"))
            item = CommonItem(row)
            if not self._items.get(item.type):
                self._items[item.type] = []
            self._items[item.type].append(item)

        return self._items
# -*- coding:utf-8 -*-
"""
created by server on 14-7-15下午2:50.
"""

from app.game.core.equipment.equipment_chip import EquipmentChip
from app.game.core.PlayersManager import PlayersManager
from app.game.redis_mode import tb_character_equipment_chip
from shared.db_opear.configs_data.game_configs import chip_config


def init_equipment_chip(player):

    for k, val in chip_config.get('chips').items():
        if val.get('type') == 1: continue
        equipment_chip = EquipmentChip(int(k), 1000)
        player.equipment_chip_component.add_chip(equipment_chip)

    return
    chip1 = EquipmentChip(2100005, 16)
    chip2 = EquipmentChip(2100006, 16)

    player.equipment_chip_component.add_chip(chip1)
    player.equipment_chip_component.add_chip(chip2)
# -*- coding:utf-8 -*-
"""
created by server on 14-7-16下午3:25.
"""
from app.game.logic.common.check import have_player
from app.proto_file.shop_pb2 import ShopRequest
from app.proto_file.common_pb2 import CommonResponse
from shared.db_opear.configs_data.game_configs import shop_config
from app.game.logic.item_group_helper import is_afford, consume, gain, get_return
from app.proto_file.player_response_pb2 import GameResourcesResponse
import time


@have_player
def shop_oper(dynamic_id, pro_data, **kwargs):
    player = kwargs.get('player')
    """商城所有操作"""
    request = ShopRequest()
    request.ParseFromString(pro_data)
    game_resources_response = GameResourcesResponse()
    response = CommonResponse()
    game_resources_response.res = response

    shop_id = request.id
    shop_item = shop_config.get(shop_id)

    if is_consume(player, shop_item):
        # 判断是否消耗
        result = is_afford(player, shop_item.consume)  # 校验
        if not result.get('result'):
            response.result = False
            response.message = '消费不足！'
        consume(player, shop_item.consume)  # 消耗
    return_data = gain(player, shop_item.gain)  # 获取
    extra_return_data = gain(player, shop_item.extra_gain)  # 额外获取

    get_return(player, return_data, game_resources_response)
    get_return(player, extra_return_data, game_resources_response)

    response.result = True
    return game_resources_response.SerializeToString()


def is_consume(player, shop_item):
    """判断是否免费抽取"""
    free_period = shop_item.free_period
    shop_item_type = shop_item.type
    if free_period == -1:
        return True

    last_pick_time = 0
    if shop_item_type == 1:
        # 单抽良将
        last_pick_time = player.last_pick_time.fine_hero
    elif shop_item_type == 2:
        # 单抽神将
        last_pick_time = player.last_pick_time.excellent_hero
    elif shop_item_type == 3:
        # 单抽良装
        last_pick_time = player.last_pick_time.fine_equipment
    elif shop_item_type == 4:
        # 单抽神装
        last_pick_time = player.last_pick_time.excellent_equipment

    if last_pick_time + free_period*60*60 <= int(time.time()):
        # 抽取后重置时间
        if shop_item_type == 1:
            # 单抽良将
            player.last_pick_time.fine_hero = int(time.time())
        elif shop_item_type == 2:
            # 单抽神将
            player.last_pick_time.excellent_hero = int(time.time())
        elif shop_item_type == 3:
            # 单抽良装
            player.last_pick_time.fine_equipment = int(time.time())
        elif shop_item_type == 4:
            # 单抽神装
            player.last_pick_time.excellent_equipment = int(time.time())

        player.last_pick_time.save_data()
        return False

    return True


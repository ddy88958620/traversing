# -*- coding:utf-8 -*-
"""
created by server on 14-7-18下午3:44.
"""
from app.game.logic.common.check import have_player
from app.game.logic.item_group_helper import gain, get_return
from app.proto_file import stage_response_pb2
from shared.db_opear.configs_data import game_configs


@have_player
def get_stage_info(dynamic_id, stage_id, **kwargs):
    """取得关卡信息
    """
    player = kwargs.get('player')

    response = []
    if stage_id:  # 根据关卡ID
        stage_obj = player.stage_component.get_stage(stage_id)
        response.append(stage_obj)
    else:  # 全部
        stages_obj = player.stage_component.get_stages()
        response.extend(stages_obj)

    return response


@have_player
def get_chapter_info(dynamic_id, chapter_id, **kwargs):
    """取得章节奖励信息
    """
    player = kwargs.get('player')

    response = []

    if chapter_id:
        chapter_obj = player.stage_component.get_chapter(chapter_id)
        response.append(chapter_obj)
    else:
        chapters_obj = player.stage_component.get_chapters()
        response.extend(chapters_obj)

    return response


@have_player
def fight_start(dynamic_id, stage_id, line_up, **kwargs):
    """开始战斗
    """
    player = kwargs.get('player')

    # 校验关卡是否开启
    state = player.stage_component.check_stage_state(stage_id)
    if state == -2:  # 未开启
        return {'result': False}

    # 保存阵容
    player.line_up_component.line_up_order = line_up
    player.line_up_component.save_data()

    fight_cache_component = player.fight_cache_component
    fight_cache_component.stage_id = stage_id

    red_units, blue_units, drop_num = fight_cache_component.fighting_start()
    return {'result': True, 'red_units': red_units, 'blue_units': blue_units, 'drop_num': drop_num}


@have_player
def fight_settlement(dynamic_id, stage_id, result, **kwargs):
    player = kwargs.get('player')

    response = stage_response_pb2.StageSettlementResponse()
    drops = response.drops
    res = response.res
    res.result = True

    # 校验是否保存关卡
    fight_cache_component = player.fight_cache_component
    if stage_id != fight_cache_component.stage_id:
        res.result = False
        res.message = u"关卡id和战斗缓存id不同"
        return response.SerializeToString()

    settlement_drops = fight_cache_component.fighting_settlement(stage_id, result)
    data = gain(player, settlement_drops)

    get_return(player, data, drops)
    res.message = u'成功返回'

    return response.SerializePartialToString()

@have_player
def get_warriors(dynamic_id, **kwargs):
    player = kwargs.get('player')
    response = stage_response_pb2.UnparalleledResponse()

    warriors = player.line_up_component.warriors
    for warrior in warriors:
        unpar_add = response.unpar.add()
        unpar_add.id = warrior
        warriors_cof = game_configs.warriors_config.get(warrior)   # 无双配置

        for i in range(1, 4):
            triggle = getattr(warriors_cof, 'triggle%s' % i)  # 技能编号
            if triggle:
                skill_cof = game_configs.skill_config.get(triggle)  # 技能配置
                group = skill_cof.group

                skill = unpar_add.unpar.add()
                skill.id = triggle

                buffs = skill.buffs

                for buff_id in group:
                    buffs.append(buff_id)
    return response.SerializePartialToString()






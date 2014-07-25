# -*- coding:utf-8 -*-
"""
created by server on 14-7-24下午6:32.
"""
from app.game.component.Component import Component
from app.game.core.guild import Guild
from app.game.redis_mode import tb_character_guild, tb_guild_info, tb_guild_name


class CharacterGuildComponent(Component):
    """公会组件类"""

    def __init__(self, owner):
        super(CharacterGuildComponent, self).__init__(owner)
        self._heros = {}

    @property
    def heros(self):
        return self._heros

    @heros.setter
    def heros(self, heros):
        self._heros = heros

    # def init_heros(self):
    #     pid = self.owner.base_info.id
    #     character_heros = tb_character_heros.getObjData(pid)
    #     if not character_heros:
    #         # 没有武将列表数据
    #         data = {
    #             'id': pid,
    #             'hero_ids': [],
    #         }
    #         tb_character_heros.new(data)
    #         return
    #
    #     hero_ids = character_heros.get('hero_ids')
    #
    #     if not hero_ids:
    #         return
    #
    #     heros = tb_character_hero.getObjList(hero_ids)
    #
    #     for hero_mmode in heros:
    #         data = hero_mmode.get('data')
    #         hero = Hero(pid)
    #         hero.init_data(data)
    #         self.add_hero(hero)
    #
    # def get_hero(self, hero_no):
    #     return self._heros.get(hero_no)
    #
    # def get_multi_hero(self, *args):
    #     return [self.get_hero(hero_no) for hero_no in args]
    #
    # def get_heros(self):
    #     return self._heros.values()
    #
    # def get_heros_by_nos(self, hero_no_list):
    #     heros = []
    #     for no in hero_no_list:
    #         heros.append(self._heros.get(no))
    #     return heros
    #
    # def add_hero(self, hero_no):
    #     hero = Hero(self.owner.base_info.id)
    #     hero.hero_no = hero_no
    #     self._heros[hero_no] = hero
    #     self.new_hero_data(hero)
    #     self.save_data()
    #     return hero
    #
    # def delete_hero(self, hero_no):
    #     del self._heros[hero_no]
    #     self.save_data()
    #     tb_character_hero.deleteMode(self.get_hero_id(hero_no))
    #
    # def delete_heros_by_nos(self, hero_no_list):
    #     for no in hero_no_list:
    #         self.delete_hero(no)
    #
    # def contain_hero(self, hero_no):
    #     return hero_no in self._heros
    #
    # def save_data(self):
    #     hero_ids = []
    #     character_id = self.owner.base_info.id
    #     for hero_no in self._heros:
    #         hero_ids.append(self.get_hero_id(hero_no))
    #     character_heros = tb_character_heros.getObj(character_id)
    #     character_heros.update('hero_ids', hero_ids)
    #
    # def get_hero_id(self, hero_no):
    #     character_id = self.owner.base_info.id
    #     return str(character_id)+'_'+str(hero_no)
    #
    # def new_hero_data(self, hero):
    #     character_id = self.owner.base_info.id
    #     hero_property = hero.hero_proerty_dict()
    #
    #     data = {
    #         'id': self.get_hero_id(hero.hero_no),
    #         'character_id': character_id,
    #         'property': hero_property
    #     }
    #     hero.mmode = tb_character_hero.new(data)
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Dynamic_init'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass
    # def creating_session(self):
    #     self.get_players()[0].participant.vars['dynamic_rounds'] = 32
    #     self.get_players()[0].participant.vars['sequence'] = [0] * self.get_players()[0].participant.vars['dynamic_rounds']
    #     result_sequence = []
    #     for i in range(2, self.get_players()[0].participant.vars['dynamic_rounds'], 4):
    #         dev = random.choice([-2, -1, 0, 1])
    #         self.get_players()[0].participant.vars['sequence'][i + dev] = 1
    #     for i in range(self.get_players()[0].participant.vars['dynamic_rounds']):
    #         result_sequence.append(random.choice([0, 1]))
    #     self.get_players()[0].participant.vars['result_sequence'] = result_sequence
    #
    #     print(self.get_players()[0].participant.vars['dynamic_rounds'])
    #     print(self.get_players()[0].participant.vars['sequence'])
    #     print(self.get_players()[0].participant.vars['result_sequence'])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # understand & agreement
    graveness = models.BooleanField(label='', choices=[[1, '是'], [0, '否']],
                                    widget=widgets.RadioSelectHorizontal)


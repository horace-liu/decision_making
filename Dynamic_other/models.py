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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Dynamic_other'
    players_per_group = None
    num_rounds = 32
    choices = ['拒绝投入', '投入硬币']
    pics = ['dynamic/refusal.png', 'dynamic/accept.png']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tom_bene_prob = models.IntegerField(label='',min=0,max=100)
    rule_prob = models.IntegerField(label='',min=0,max=100)
    bene_prob = models.IntegerField(label='',min=0,max=100)






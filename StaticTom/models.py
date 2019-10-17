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
    name_in_url = 'StaticTom'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # TOM.
    tom1_b1 = models.IntegerField(label='')
    tom1_b2 = models.IntegerField(label='')
    tom3_p1 = models.IntegerField(label='')
    tom3_p2 = models.IntegerField(label='')
    tom3_p3 = models.IntegerField(label='')
    tom2_m1 = models.IntegerField(label='')
    tom2_m2 = models.IntegerField(label='')



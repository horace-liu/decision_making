from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'coverstroy'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # demographic data.
    name = models.StringField()
    gender = models.IntegerField()
    age = models.IntegerField()
    education = models.StringField()

    # consent.
    consent = models.IntegerField(label='', choices=[[1, '同意'], [0, '不同意']], widget=widgets.RadioSelectHorizontal)

    # check.
    check_q1 = models.BooleanField(label='1.参与者第5回合仍可以选择是否投币?', choices=[[1, '是'], [0, '否']], widget=widgets.RadioSelectHorizontal)
    check_q2 = models.BooleanField(label='2.编号为032的参与者第4回合的实际收益为+2.5 ?', choices=[[1, '是'], [0, '否']], widget=widgets.RadioSelectHorizontal)
    check_q3 = models.BooleanField(label='3.编号为034的参与者第1和2回合选择了投币?', choices=[[1, '是'], [0, '否']], widget=widgets.RadioSelectHorizontal)







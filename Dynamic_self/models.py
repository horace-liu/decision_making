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
    name_in_url = 'Dynamic_self'
    players_per_group = None
    num_rounds = 32

    result_content = ['没有收益', '增加￥5']
    result_pic = ['dynamic/loss.png', 'dynamic/win.png']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    agreement = models.IntegerField(
        label='我已充分阅读上述游戏规则，同意继续实验',
        choices=[[1, '是'], [0, '否']],
        widget=widgets.RadioSelectHorizontal
    )

    choice = models.IntegerField(
        label='',
        choices=[[1, '投入'], [0, '拒绝']],
        widget=widgets.RadioSelectHorizontal,
        initial=2
    )

    reward = models.IntegerField()
    refusal = models.StringField(initial='locked')
    final_benefit = models.FloatField()
    possibility = models.IntegerField(label='')

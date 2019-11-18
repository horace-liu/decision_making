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
from django import forms


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Final_evaluation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def make_field_char(label):
        return models.IntegerField(
            label=label,
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
            widget=widgets.RadioSelectHorizontal
        )

    def make_field_des(label):
        return models.IntegerField(
            label=label,
            choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7']],
            widget=widgets.RadioSelectHorizontal
        )


    char1 = make_field_char('明智')
    char2 = make_field_char('冲动')
    char3 = make_field_char('冷静')
    char4 = make_field_char('稳重')
    char5 = make_field_char('乐观')
    char6 = make_field_char('积极')
    char7 = make_field_char('莽撞')

    descrip1 = make_field_des('在不确定的情况下，林*总是期待最好的')
    descrip2 = make_field_des('预期对林*不利的事情，最后总会变成现实')
    descrip3 = make_field_des('林*对自己的未来总是很乐观')
    descrip4 = make_field_des('林*几乎不敢期望事情会照着自己的意愿变化')
    descrip5 = make_field_des('林*很少指望好事会发生在自己身上')
    descrip6 = make_field_des('总的来说，林*希望有更多好事儿，而非坏事儿发生在自己身上')

    question = models.StringField(label='', widget=forms.Textarea)



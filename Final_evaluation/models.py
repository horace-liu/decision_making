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
            choices=[[1, '完全不符合'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, '完全符合']],
            widget=widgets.RadioSelectHorizontal
        )

    def make_field_des(label):
        return models.IntegerField(
            label=label,
            choices=[[1, '非常不同意'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, '非常同意']],
            widget=widgets.RadioSelectHorizontal
        )

    char1 = make_field_char('1. 明智')
    char2 = make_field_char('2. 冲动')
    char3 = make_field_char('3. 冷静')
    char4 = make_field_char('4. 稳重')
    char5 = make_field_char('5. 乐观')
    char6 = make_field_char('6. 积极')
    char7 = make_field_char('7. 莽撞')

    descrip1 = make_field_des('1.  在不确定的情况下，林*总是期待最好的。')
    descrip2 = make_field_des('2.  放松下来对林*而言是件容易的事情。')
    descrip3 = make_field_des('3.  预期对林*不利的事情，最后总会变成现实。')
    descrip4 = make_field_des('4.  林*对自己的未来总是很乐观。')
    descrip5 = make_field_des('5.  林*很喜欢和自己的朋友们呆在一块儿。')
    descrip6 = make_field_des('6.  让自己保持忙碌对于林*来说是很重要的。')
    descrip7 = make_field_des('7.  林*几乎不敢期望事情会照着自己的意愿变化。')
    descrip8 = make_field_des('8.  林*不会轻易心烦意乱。 ')
    descrip9 = make_field_des('9.  林*很少指望好事会发生在自己身上。')
    descrip10 = make_field_des('10.  总的来说，林*希望有更多好事儿，而非坏事儿发生在自己身上。')




from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class S_vo1(Page):
    form_model = 'player'
    form_fields = ['vo1_b{}'.format(i) for i in [1, 2, 3]]


class S_vo2(Page):
    form_model = 'player'
    form_fields = ['vo2_m{}'.format(i) for i in [1, 2, 3]]

class S_vo3(Page):
    form_model = 'player'
    form_fields = ['vo3_p{}'.format(i) for i in [1, 2, 3]]

class connection_vo_tom(Page):
    form_model = 'player'
    form_fields = ['vt_check']


# not string!
vo_sequence = [S_vo1, S_vo2, S_vo3]
random.shuffle(vo_sequence)
page_sequence = vo_sequence + [connection_vo_tom]


from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class S_tom1(Page):
    form_model = 'player'
    form_fields = ['tom1_b{}'.format(i) for i in [1, 2, 3]]


class S_tom2(Page):
    form_model = 'player'
    form_fields = ['tom2_m{}'.format(i) for i in [1, 2, 3]]


class S_tom3(Page):
    form_model = 'player'
    form_fields = ['tom3_p{}'.format(i) for i in [1, 2, 3]]


tom_sequence = [S_tom1, S_tom2, S_tom3]
random.shuffle(tom_sequence)
page_sequence = tom_sequence

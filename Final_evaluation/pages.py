from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Char(Page):
    form_model = 'player'
    form_fields = ['char{}'.format(i) for i in range(1, 8)]


class Descrip(Page):
    form_model = 'player'
    form_fields = ['descrip{}'.format(i) for i in range(1, 11)]

page_sequence = [Char, Descrip]

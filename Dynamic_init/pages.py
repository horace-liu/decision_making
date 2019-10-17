from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class graveness(Page):
    form_model = 'player'
    form_fields = ['graveness']

    def before_next_page(self):
        self.participant.vars['dynamic_rounds'] = 32
        self.participant.vars['sequence'] = [0] * self.participant.vars['dynamic_rounds']
        result_sequence = []
        for i in range(2, self.participant.vars['dynamic_rounds'], 4):
            dev = random.choice([-2, -1, 0, 1])
            self.participant.vars['sequence'][i + dev] = 1
        for i in range(self.participant.vars['dynamic_rounds']):
            result_sequence.append(random.choice([0, 1]))
        self.participant.vars['result_sequence'] = result_sequence

        print('sequence of dynamic_self')
        print(self.participant.vars['sequence'])
        print(self.participant.vars['result_sequence'])


page_sequence = [graveness]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        sequence = [0] * 32
        for i in [4, 7, 11, 16, 21, 24, 28, 32]:
            sequence[i - 1] = 1
        choice_sequence = [0] * 16 + [1] * 16
        for i in [1, 10, 12]:
            choice_sequence[i - 1] = 1
        self.session.vars['sequence'] = sequence
        self.session.vars['choice_sequence'] = choice_sequence

        print('sequence of dynamic_other:')
        print(self.session.vars['sequence'])
        print(self.session.vars['choice_sequence'])


class Choice(Page):
    def is_displayed(self):
        return self.session.vars['sequence'][self.round_number - 1] == 0

    def vars_for_template(self):
        choice_sequence = self.session.vars['choice_sequence']
        cons = Constants()
        return dict(
            choice=cons.choices[choice_sequence[self.round_number - 1]],
            pic_dir=cons.pics[choice_sequence[self.round_number - 1]]
        )


class Evaluation(Page):
    form_model = 'player'
    form_fields = ['tom_benefit_exp', 'rule_obtain', 'benefit_poss']

    def is_displayed(self):
        return self.session.vars['sequence'][self.round_number - 1] == 1


page_sequence = [Introduction, Choice, Evaluation]

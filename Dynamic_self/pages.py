from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Introduction(Page):
    form_model = 'player'
    form_fields = ['agreement']

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.session.vars['dynamic_rounds'] = 32
        self.session.vars['sequence'] = [0] * self.session.vars['dynamic_rounds']
        result_sequence = []


        lock_result = [1] * 4 + [0] * 4
        random.shuffle(lock_result)
        print(lock_result)

        for i in range(2, self.session.vars['dynamic_rounds'], 4):
            dev = random.choice([-2, -1, 0, 1])
            self.session.vars['sequence'][i + dev] = 1

        l = 0
        for index, lock in enumerate(self.session.vars['sequence']):
            # print(index, '\t', lock)
            if lock == 1:
                result_sequence.append(lock_result[l])
                l += 1
            else:
                result_sequence.append(random.choice([0, 1]))

        self.session.vars['result_sequence'] = result_sequence

        print('sequence of dynamic_self')
        print("lock sequence:\t\t", self.session.vars['sequence'])
        print("result sequence:\t", self.session.vars['result_sequence'])

class Choice(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(self):
        sequence = self.session.vars['sequence']
        return sequence[self.round_number - 1] == 0

    def before_next_page(self):
        result_sequence = self.session.vars['result_sequence']
        if self.player.choice == 1:
            self.player.refusal = '0'
            if result_sequence[self.round_number - 1] == 1:
                self.player.reward = 1
                self.player.final_benefit = 5
            else:
                self.player.reward = 0
                self.player.final_benefit = 0
        else:
            self.player.refusal = '1'
            self.player.final_benefit = 4.5


class Locked(Page):
    form_model = 'player'
    form_fields = ['possibility','rule_prob']

    def is_displayed(self):
        sequence = self.session.vars['sequence']
        return sequence[self.round_number - 1] == 1

    def before_next_page(self):
        result_sequence = self.session.vars['result_sequence']
        if result_sequence[self.round_number - 1] == 1:
            self.player.reward = 1
            self.player.final_benefit = 5
        else:
            self.player.reward = 0
            self.player.final_benefit = 0


class Result(Page):
    def vars_for_template(self):
        cons = Constants
        return dict(
            pic_link=cons.result_pic[self.player.reward],
            result_content=cons.result_content[self.player.reward]
        )

    def is_displayed(self):
        sequence = self.session.vars['sequence']
        return self.player.choice == 1 or sequence[self.round_number - 1] == 1


class Refusal(Page):
    def is_displayed(self):
        sequence = self.session.vars['sequence']
        return self.player.choice == 0 and sequence[self.round_number - 1] == 0


class Rest(Page):
    def is_displayed(self):
        return self.round_number == 32


page_sequence = [Introduction, Choice, Locked, Result, Refusal, Rest]

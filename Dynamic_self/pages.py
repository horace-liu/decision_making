from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    form_model = 'player'
    form_fields = ['agreement']

    def is_displayed(self):
        return self.round_number == 1


class Choice(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(self):
        sequence = self.participant.vars['sequence']
        return sequence[self.round_number - 1] == 0

    def before_next_page(self):
        result_sequence = self.participant.vars['result_sequence']
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
        sequence = self.participant.vars['sequence']
        return sequence[self.round_number - 1] == 1

    def before_next_page(self):
        result_sequence = self.participant.vars['result_sequence']
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
        sequence = self.participant.vars['sequence']
        return self.player.choice == 1 or sequence[self.round_number - 1] == 1


class Refusal(Page):
    def is_displayed(self):
        sequence = self.participant.vars['sequence']
        return self.player.choice == 0 and sequence[self.round_number - 1] == 0


class Rest(Page):
    def is_displayed(self):
        return self.round_number == 32


page_sequence = [Introduction, Choice, Locked, Result, Refusal, Rest]

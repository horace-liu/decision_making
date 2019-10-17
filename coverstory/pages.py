from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def app_after_this_page(self, upcoming_apps):
        if self.player.consent == 0:
            return 'Theend'

    def is_displayed(self):
        return self.round_number == 1


class S_CoverStory(Page):
    form_model = 'player'
    form_fields = ['check_q{}'.format(i) for i in [1, 2, 3]]

    def app_after_this_page(self, upcoming_apps):
        q1 = self.player.check_q1
        q2 = self.player.check_q2
        q3 = self.player.check_q3
        if q1 == 0 and q2 == 1 and q3 == 1:
            return upcoming_apps[0]


class S_coverstory_failed(Page):
    def is_displayed(self):
        q1 = self.player.check_q1
        q2 = self.player.check_q2
        q3 = self.player.check_q3
        return not (q1 == 0 and q2 == 1 and q3 == 1)


page_sequence = [Consent, S_CoverStory, S_coverstory_failed]

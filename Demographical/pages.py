from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Mainpage(Page):
    form_model = 'player'
    form_fields = ['name', 'gender', 'age', 'ethics', 'occupation', 'religion', 'marriage', 'sexual', 'education']


class Others(Page):
    form_model = 'player'
    form_fields = ['phone_number', 'alipay_account', 'ID_card', 'faculty', 'email', 'student_id']


page_sequence = [Mainpage, Others]

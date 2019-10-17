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
    name_in_url = 'Demographical'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # demographic data.
    name = models.StringField(label='姓名')
    gender = models.IntegerField(
        label='性别',
        choices=[[1, '男'], [2, '女'], [3, '其他']],
        widget=widgets.RadioSelectHorizontal)
    age = models.IntegerField(label='年龄')
    ethics = models.StringField(label='民族')
    occupation = models.StringField(
        label='',
        choices=[
            '全日制学生',
            '生产人员',
            '销售人员',
            '市场/公关人员',
            '客服人员',
            '行政人员',
            '后勤人员',
            '人力资源',
            '财务审计人员',
            '文职/办事人员',
            '技术/研发人员',
            '管理人员',
            '教师',
            '顾问/咨询',
            '专业人员',
            '其他'],
        widget=widgets.RadioSelectHorizontal
    )
    religion = models.StringField(
        label='',
        choices=[
            '基督教',
            '佛教',
            '天主教',
            '伊斯兰教',
            '其他',
            '无宗教信仰'
        ],
        widget=widgets.RadioSelect
    )
    education = models.StringField(
        label='',
        choices=[
            '初中及以下',
            '高中',
            '本科学位',
            '硕士学位',
            '博士学位'
        ],
        widget=widgets.RadioSelect
    )
    marriage = models.StringField(
        label='',
        choices=[
            '已婚，或与某人共同居住，或有固定交往的对象',
            '单身，或没有固定交往的对象',
            '分手中 ',
            '离异，之前有固定的交往对象 ',
            '鳏寡(丈夫或妻子已过世)'
        ],
        widget=widgets.RadioSelect
    )
    sexual = models.StringField(
        label='',
        choices=[
            '完全异性恋',
            '主要异性恋，只偶有同性恋行为',
            '异性恋与同性恋倾向相同',
            '主要为同性恋，但也有异性恋行为',
            '主要为同性恋，之偶有异性恋行为',
            '完全同性恋',
            '无性恋'
        ],
        widget=widgets.RadioSelect
    )
    phone_number = models.StringField(label='您的电话(请填写真实电话，便于进行报酬的确认)')
    alipay_account = models.StringField(label='支付宝账号(请注意是否无误)')
    ID_card = models.StringField(label='身份证号(请务必保证准确，用于报销报酬)')
    faculty = models.StringField(label='工作单位(在校生填写就读学校，非在校学生请填写工作单位)')
    email = models.StringField(label='电子邮箱')
    student_id = models.StringField(label='北师大学生请填写学号，非北师大学生请填0')

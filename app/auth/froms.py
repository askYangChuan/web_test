#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: yangchuan
@time: $(DATE) $(TIME)
'''

__author__ = 'Yang Chuan'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField
from wtforms.validators import Required, DataRequired

class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = StringField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')

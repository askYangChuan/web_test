# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, DateTimeField
from wtforms.validators import Required, DataRequired
from .definition_internal import QueryIndexType

class QueryForm(FlaskForm):
    queryindex = SelectField(
        u'查询类别',
        validators=[DataRequired('请选择索引')],
        choices=[(QueryIndexType.QueryIndexHomeId, '家庭id'), (QueryIndexType.QueryIndexUserId, '用户id'), (QueryIndexType.QueryIndexSn, '设备sn')],
            coerce=int)
    querykey = StringField(u'关键字', validators=[DataRequired()])
    querymax = StringField(u'最多显示条数', validators=[DataRequired()], default='100')
    showper = StringField(u'每页显示条数', validators=[DataRequired()], default='20')
    querystart = DateTimeField(u'起始时间', validators=[DataRequired()], default=datetime.fromtimestamp(0))
    queryend = DateTimeField(u'结束时间', validators=[DataRequired()], default=datetime.fromtimestamp(0))
    submit = SubmitField('查询')

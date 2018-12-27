# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import current_app
from . import db
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 't_query_web_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    ctime = db.Column(db.DateTime)
    mtime = db.Column(db.DateTime)

    def __repr__(self):
        return 'User username %s' % self.username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, passwd):
        print self.password_hash
        print passwd
        return check_password_hash(self.password_hash, passwd)



class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

#这里的user_id是根据User.get_id得来的(默认UserMixin实现了)。如果表格没得id，那么就需要自己实现get_id函数
#def get_id(self):
# return unicode(self.user_id)
#这里user_id可以修改为username， 这样load_user这里传递的参数user_id实际上就是username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class FlowMsg(db.Model):
    __tablename__ = 't_linksrv_flow_msg'
    id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    sn = db.Column(db.BigInteger)
    msgstr = db.Column(db.String(64), default='')
    msg = db.Column(db.Integer)
    todo = db.Column(db.String(64), default='{}')
    ctime = db.Column(db.DateTime)

    def __repr__(self):
        return '<flow_msg home_id %d, user_id %d, sn %d, ctime: %s>' % (self.home_id, self.user_id, self.sn, self.ctime)


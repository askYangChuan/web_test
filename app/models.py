from flask import current_app
from . import db


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


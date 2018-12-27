# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
from flask import render_template, flash, session, redirect, url_for, request
from flask_login import login_required, current_user
from . import main
from .forms import QueryForm
from .definition_internal import QueryIndexType
from ..models import FlowMsg
from .todo_prase import todo_prase,FlowMsgPrase
from sqlalchemy import and_

def clearQuerySession():
    if session.get('queryindex'):
        session.pop('queryindex')
    if session.get('querykey'):
        session.pop('querykey')
    if session.get('querymax'):
        session.pop('querymax')
    if session.get('page'):
        session.pop('page')
    if session.get('showper'):
        session.pop('showper')
    if session.get('querystart'):
        session.pop('querystart')
    if session.get('queryend'):
        session.pop('queryend')

def check_querysession():
    if not session.get('queryindex') or not session.get('querykey') or not session.get('querymax') \
        or not session.get('showper'):
        return False
    return True

#limit(max_num).
def getMsgByHomeid(home_id, max_num):
    per_page = session.get('showper')
    startTime = session.get('querystart')
    endTime = session.get('queryend')
    if time.mktime(startTime.timetuple()) == 0 and time.mktime(endTime.timetuple()) == 0:
        flower_pagination = FlowMsg.query.filter_by(home_id=home_id).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    else:
        flower_pagination = FlowMsg.query.filter(and_(
            FlowMsg.home_id==home_id, FlowMsg.ctime.between(startTime, endTime))).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    return flower_pagination

def getMsgByUserid(user_id, max_num):
    per_page = session.get('showper')
    startTime = session.get('querystart')
    endTime = session.get('queryend')
    if time.mktime(startTime.timetuple()) == 0 and time.mktime(endTime.timetuple()) == 0:
        flower_pagination = FlowMsg.query.filter_by(user_id=user_id).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    else:
        flower_pagination = FlowMsg.query.filter(and_(
            FlowMsg.user_id==user_id, FlowMsg.ctime.between(startTime, endTime))).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    return flower_pagination

def getMsgBySn(sn, max_num):
    per_page = session.get('showper')
    startTime = session.get('querystart')
    endTime = session.get('queryend')
    if time.mktime(startTime.timetuple()) == 0 and time.mktime(endTime.timetuple()) == 0:
        flower_pagination = FlowMsg.query.filter_by(sn=sn).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    else:
        flower_pagination = FlowMsg.query.filter(and_(
            FlowMsg.sn==sn, FlowMsg.ctime.between(startTime, endTime))).order_by(FlowMsg.id.desc()).paginate(
            session.get('page'), per_page=int(per_page),error_out=False
        )
    return flower_pagination

def getMsg():
    queryindex = session.get("queryindex")
    if queryindex == QueryIndexType.QueryIndexHomeId:
        return getMsgByHomeid(session.get("querykey"), session.get("querymax"))
    elif queryindex == QueryIndexType.QueryIndexUserId:
        return getMsgByUserid(session.get("querykey"), session.get("querymax"))
    else:
        return getMsgBySn(session.get("querykey"), session.get("querymax"))


@main.route('/')
def index():
    clearQuerySession()
    return render_template('index.html')
    
    
@main.route('/query', methods=['GET', 'POST'])
@login_required
def query():
    form = QueryForm()
    if form.validate_on_submit():
        #flower = getMsg(form)
        #flash('queryindex %s querykey %s querymax %s showper %s start %s end %s' % (form.queryindex.data,
                        #form.querykey.data, form.querymax.data, form.showper.data, form.querystart.data,
                                                                         #form.queryend.data))
        session['queryindex'] = form.queryindex.data
        session['querykey'] = form.querykey.data
        session['querymax'] = form.querymax.data
        session['showper'] = form.showper.data
        session['querystart'] = form.querystart.data
        session['queryend'] = form.queryend.data
        return redirect(url_for('.showresult'))
    clearQuerySession()
    return render_template('query.html', form=form)


@main.route('/result')
@login_required
def showresult():
    if not check_querysession():
        flash('输入条件有误')
        return redirect(url_for('.query'))
    session['page'] = request.args.get('page', 1, type=int)
    pagination = getMsg()
    flowmsgs = pagination.items
    f = todo_prase(flowmsgs)
    return render_template('result.html', flowmsgs=f, pagination=pagination)


#!/usr/bin/env python
import os
import datetime
import time
from app import create_app, db
from app.models import FlowMsg
from flask_script import Manager, Shell
from sqlalchemy  import and_

#app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app(os.getenv('FLASK_CONFIG') or 'production')
manager = Manager(app)

def datetime_toTimestamp(dt):
    print("datetime_toTimestamp:", time.mktime(dt.timetuple()))


def do_test():
    s = '1970-01-01 08:00:00'
    e = '1970-01-01 08:00:00'
    s = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    datetime_toTimestamp(s)
    return
    s = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    e = datetime.datetime.strptime(e, "%Y-%m-%d %H:%M:%S")
    '''
    flower_pagination = FlowMsg.query.filter(FlowMsg.home_id==1 and
                                             FlowMsg.ctime>='1970-01-01 08:00:00' and
                                             FlowMsg.ctime <='1970-01-01 08:00:00').order_by(FlowMsg.id.desc()).paginate(
        1, per_page=10, error_out=False
    )
    '''
    print s
    flower_pagination = FlowMsg.query.filter(and_(FlowMsg.home_id==1,
                                                  FlowMsg.ctime.between('1970-01-01 08:00:00','1972-01-01 08:00:00'))).order_by(FlowMsg.id.desc()).paginate(
        1, per_page=10, error_out=False
    )

    #print FlowMsg.query.filter(FlowMsg.home_id==1).order_by(FlowMsg.id.desc()).limit(5)
    print flower_pagination
    print flower_pagination.items

@manager.command
def test():
    """Run the unit tests."""
    do_test()


if __name__ == '__main__':
    manager.run()

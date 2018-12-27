
"""
from app.main.todo_prase import  msg_prase
todo = '{"desc":"user role edit","action":2,"proc":"open-5.0.0 65234 <test_linklog.c 35 test_log_user_motifyrole>","home_id":1,"doer":2,"user_id":3,"utc":1544668037,"occur":"2018-12-13-10-27-17","ip":"0.1.226.64","roleid":4}'


t = msg_prase('LOG_USER_ROLE_MODIFY', todo)
print t
"""

from werkzeug.security import generate_password_hash
print generate_password_hash('1')



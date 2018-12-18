# -*- coding: utf-8 -*-

import json
from ..models import FlowMsg

class FlowMsgPrase(object):

    def __init__(self, msg, desc):
        self.flowmsg = msg
        self.desc = desc

    def __str__(self):
        print "<%s>" % self.desc

    __repr__ = __str__

def gethomename(j):
    if not j.has_key("homename") or j["homename"] == '':
        return j["home_id"]
    if j["homename"] == '':
        return u"我的家"
    return j["homename"]

def prase_log_user_modify(todo):
    j = json.loads(todo)
    return "用户 %s 编辑资料(用户名、uuid、密码)\n [操作userid %s %s (%s)]\n" \
           "oldpass: %s," \
           "newpass: %s" \
           % (j["user_id"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"],
              j["oldpass"], j["newpass"])

def prase_log_user_role_modify(todo):
    j = json.loads(todo)
    return "用户 %s 在家庭 %s 的角色roleid修改为%s\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["roleid"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])


def prase_log_user_phoneinfo_modify(todo):
    j = json.loads(todo)
    return "用户 %s 在家庭 %s 的昵称被修改, nickname: %s\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["nickname"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_user_widgetkey_modify(todo):
    j = json.loads(todo)
    return "用户 %s 的widgetkey被修改\n [操作userid %s %s (%s)]" \
           % (j["user_id"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_user_mail_bind(todo):
    j = json.loads(todo)
    return "用户 %s 绑定新邮箱%s\n [操作userid %s %s (%s)]" \
           % (j["user_id"], j["mail"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_user_mail_unbind(todo):
    j = json.loads(todo)
    return "用户 %s 取消绑定邮箱\n [操作userid %s %s (%s)]" \
           % (j["user_id"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_user_replace(todo):
    j = json.loads(todo)
    return "会话替换，弱用户 %s 替换为强用户 %s\n [操作userid %s %s (%s)]\n" \
           % (j["old_user"], j["new_user"], j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_create(todo):
    j = json.loads(todo)
    return "用户 %s 创建家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["doer"], gethomename(j), j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_delete(todo):
    j = json.loads(todo)
    return "用户 %s 删除家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["doer"], gethomename(j), j["doer"], "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_sn_join(todo):
    j = json.loads(todo)
    doer = j["user_id"] if j.has_key("user_id") else 0
    if doer == 0:
        doer = "ICE"
    return "设备 %s 加入家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["sn"], gethomename(j), doer, "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_sn_leave(todo):
    j = json.loads(todo)
    doer = j["user_id"] if j.has_key("user_id") else 0
    if doer == 0:
        doer = "ICE"
    return "设备 %s 离开家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["sn"], gethomename(j), doer, "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_sn_resetct_update(todo):
    j = json.loads(todo)
    doer = j["user_id"] if j.has_key("user_id") else 0
    if doer == 0:
        doer = "ICE"
    return "设备 %s 更新家庭 %s 恢复出厂次数为%s\n [操作userid %s %s (%s)]" \
           % (j["sn"], gethomename(j), j["reset_count"], doer, "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_sn_moditypasswd(todo):
    j = json.loads(todo)
    doer = j["user_id"] if j.has_key("user_id") else 0
    if doer == 0:
        doer = "ICE"
    return "设备 %s 更新家庭 %s 中自己的密码为%s\n [操作userid %s %s (%s)]" \
           % (j["sn"], gethomename(j), j["dev_passwd"], doer, "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_name_modity(todo):
    j = json.loads(todo)
    return "用户 %s 更新家庭 %s 的家庭名字(%s->%s)\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["oldname"], j["newname"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_owner_modity(todo):
    j = json.loads(todo)
    return "家庭 %s 的拥有者更新(%s->%s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["old_owner"], j["new_owner"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_master_modity(todo):
    j = json.loads(todo)
    return "用户 %s 更新家庭 %s 的lan master(%s->%s)\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["old_master"], j["new_master"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_approval_modity(todo):
    j = json.loads(todo)
    return "用户 %s 更新家庭 %s 的批准权限(%s->%s)\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["old_approval"], j["new_approval"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_user_leave(todo):
    j = json.loads(todo)
    return "用户 %s 离开家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_user_join(todo):
    j = json.loads(todo)
    return "用户 %s 加入家庭 %s\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_user_edit(todo):
    j = json.loads(todo)
    return "用户 %s 在家庭 %s 的信息被编辑\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_user_level_edit(todo):
    j = json.loads(todo)
    return "用户 %s 在家庭 %s 的等级修改(%s->%s)\n [操作userid %s %s (%s)]" \
           % (j["user_id"], gethomename(j), j["old_level"], j["new_level"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_linkage_add(todo):
    j = json.loads(todo)
    return "家庭 %s 添加规则(id: %s, index: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["rule_id"], j["index"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_linkage_edit(todo):
    j = json.loads(todo)
    return "家庭 %s 编辑规则(id: %s, index: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["rule_id"], j["index"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_linkage_del(todo):
    j = json.loads(todo)
    return "家庭 %s 删除规则(id: %s, index: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["rule_id"], j["index"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_linkage_exec(todo):
    j = json.loads(todo)
    return "家庭 %s 执行规则(id: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["rule_id"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_labeladd(todo):
    j = json.loads(todo)
    return "家庭 %s 添加标签(label_id: %s, label_name: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["label_id"], j["label_name"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_labeldel(todo):
    j = json.loads(todo)
    return "家庭 %s 删除标签(label_id: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["label_id"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_label_snadd(todo):
    j = json.loads(todo)
    return "家庭 %s 添加标签设备(label_id: %s, sn: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["label_id"], j["sn"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_label_sndel(todo):
    j = json.loads(todo)
    return "家庭 %s 删除标签设备(label_id: %s, sn: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["label_id"], j["sn"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_dictadd(todo):
    j = json.loads(todo)
    return "家庭 %s 添加字典(dict_key: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["dict_key"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])

def prase_log_home_dictdel(todo):
    j = json.loads(todo)
    return "家庭 %s 删除字典(dict_key: %s)\n [操作userid %s %s (%s)]" \
           % (gethomename(j), j["dict_key"], j["doer"],
              "【" + j["ip"] + "】" if j.has_key("ip") else "", j["occur"])


msgPraseProc = {
    "LOG_USER_MODIFY": prase_log_user_modify,
    "LOG_USER_ROLE_MODIFY": prase_log_user_role_modify,
    "LOG_USER_PHONEINFO_MODIFY": prase_log_user_phoneinfo_modify,
    "LOG_USER_WIDGETKEY_MODIFY": prase_log_user_widgetkey_modify,
    "LOG_USER_MAIL_BIND": prase_log_user_mail_bind,
    "LOG_USER_MAIL_UNBIND": prase_log_user_mail_unbind,
    "LOG_USER_REPLACE": prase_log_user_replace,
    "LOG_HOME_CREATE": prase_log_home_create,
    "LOG_HOME_DELETE": prase_log_home_delete,
    "LOG_HOME_SN_JOIN": prase_log_home_sn_join,
    "LOG_HOME_SN_LEAVE": prase_log_home_sn_leave,
    "LOG_HOME_SN_RESETCT_UPDATE": prase_log_home_sn_resetct_update,
    "LOG_HOME_SN_MODITYPASSWD": prase_log_home_sn_moditypasswd,
    "LOG_HOME_NAME_MODITY": prase_log_home_name_modity,
    "LOG_HOME_OWNER_MODITY": prase_log_home_owner_modity,
    "LOG_HOME_MASTER_MODITY": prase_log_home_master_modity,
    "LOG_HOME_APPROVAL_MODITY": prase_log_home_approval_modity,
    "LOG_HOME_USER_LEAVE": prase_log_home_user_leave,
    "LOG_HOME_USER_JOIN": prase_log_home_user_join,
    "LOG_HOME_USER_EDIT": prase_log_home_user_edit,
    "LOG_HOME_USER_LEVEL_EDIT": prase_log_home_user_level_edit,
    "LOG_HOME_LINKAGE_ADD": prase_log_home_linkage_add,
    "LOG_HOME_LINKAGE_EDIT": prase_log_home_linkage_edit,
    "LOG_HOME_LINKAGE_DEL": prase_log_home_linkage_del,
    "LOG_HOME_LINKAGE_EXEC": prase_log_home_linkage_exec,
    "LOG_HOME_LABELADD": prase_log_home_labeladd,
    "LOG_HOME_LABELDEL": prase_log_home_labeldel,
    "LOG_HOME_LABEL_SNADD": prase_log_home_label_snadd,
    "LOG_HOME_LABEL_SNDEL": prase_log_home_label_sndel,
    "LOG_HOME_DICTADD": prase_log_home_dictadd,
    "LOG_HOME_DICTDEL": prase_log_home_dictdel,

}


def msg_prase(msgstr, todo):
    return msgPraseProc[msgstr](todo)

def todo_prase(flowmsgs):
    f = []
    for msg in flowmsgs:
        f.append(FlowMsgPrase(msg, msg_prase(msg.msgstr, msg.todo)))
    return f

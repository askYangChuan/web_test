#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: yangchuan
@time: $(DATE) $(TIME)
'''

__author__ = 'Yang Chuan'

from . import auth
from .froms import LoginForm
from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, logout_user, login_required
from ..models import User

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("用户账号或密码错误")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
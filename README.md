练手项目 
nginx+uwsgi+flask+virtualenv


nginx的配置 是nginx_uwgi.conf
uwsgi的启动文件是 uwsgi.ini

启动uwsgi的命令是
./venv/bin/uwsgi --ini uwsgi.ini --uid uwsgi
这里uwsgi需要用虚拟环境下面安装的uwsgi来处理。
--uid是一个用户Id，可以专门创建 一个用户id来运行程序
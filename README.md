ssrr
====

Simple Stream Reflector for RTMP servers

Command execution example
=========================

Next example shows how to reflect streams from 10.1.1.12 host to
10.8.80.14 host::

 /usr/local/bin/ssrr  -L /var/log/ssrr/ssrr.log -i  10.1.1.12 -d 10.9.80.14


Logrotate rule example
======================

::

  /var/log/ssrr/*.log {
  daily
  missingok
  rotate 52
  compress
  delaycompress
  # notifempty
  create 640 root adm
  sharedscripts
  postrotate
    for i in `ps ax | grep /usr/local/bin/ssrr |  grep -v grep | awk '{print $1}'`
    do
      kill -HUP $i
    done
  endscript
  }



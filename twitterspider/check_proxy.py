# -*- coding: utf-8 -*-

import telnetlib
import requests
from twitterspider.ProgressBar import ProgressBar

def first_check():
    check_ip = '127.0.0.1'
    check_port = '1087'
    try:
        telnetlib.Telnet(check_ip, port=check_port, timeout=5)
    except Exception:
        print '本机%s端口不可用' % check_port
    else:
        print '第一道检测闸放行'
    check_ip_port_http = 'http://%s:%s' % (check_ip, check_port)
    check_ip_port_https = 'https://%s:%s' % (check_ip, check_port)
    return second_check(check_ip_port_http, check_ip_port_https)


def second_check(check_ip_port_http, check_ip_port_https):
    test_url = "https://www.google.com/"
    proxies = {
        'http': check_ip_port_http,
        'https': check_ip_port_https
    }
    print "第二道检测闸检测中..."
    try:
        response = requests.get(test_url, proxies=proxies)
        if response.status_code == 200:
            print "放行,代理可用！"
    except Exception:
        print "扣押,代理不可用"

if __name__ == '__main__':
    pb = ProgressBar(total=5)
    pb.progress()
    # first_check()
# coding=utf-8
import socket
import subprocess


def startappium():
    host = "127.0.0.1"
    port = "8888"
    bootstrap_port = "9999"
    appium_log_path = "/Users/netease/Documents/startAppiumLog/"
    errormsg = ""
    appium_server_url = ""
    print "hwjuehrkehwr"
    try:
        if port_is_free(host, port):
            """
            cmd = 'appium & ' + '-p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port) + \
                      ' --session-override --log ' \
                      + '"' + appium_log_path + '" --command-timeout 600'
            """
            cmd = 'appium & ' + ' --session-override --log ' + '"' + appium_log_path
            print cmd
            p = subprocess.call(cmd, shell=True, stdout=open("/Users/netease/Documents/startAppiumLog/logs.log", 'w'), stderr=subprocess.STDOUT)
            print p
            appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
            print appium_server_url
        else:
            print "port:%s is used!" % port
    except Exception, msg:
        errormsg = str(msg)
    return appium_server_url, errormsg


def port_is_free(host, port):
    soc = socket.socket()
    try:
        soc.connect_ex((host, int(port)))
        return True
    except:
        return False
    finally:
        soc.close()

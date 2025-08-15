#!/usr/bin/python
#coding: UTF-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from colorama import init, Fore, Back, Style
init(autoreset=True)
from .vtg_device_ import *
from collections import namedtuple
MPC = namedtuple('MprintalContents', ['Tag', 'Descriptions', 'Device', 'Tenant'])


class VTG_alarms:
    def __init__(self, *args, **kwargs):
        self.__ri_alarms_detail_urlpath = f"/api/operational/alarms/alarm-list/alarm"
        self.__ri_alarms_number_urlpath = f"/api/operational/alarms/alarm-list/number-of-alarms"
        self.__ri_alarms_event_urlpath  = f"/api/operational/alarms/alarm-list/alarm"

    def mail_print_(self, contents):
        host = 'smtp.163.com'
        sender = 'rpc_tvm@163.com'
        receivers = 'gu.jie@21viacloud.com'
        ## receivers = 'chen.xinfeng@21viacloud.com'
        subject = "Hey! Monprintal mail wrote by VegetableSoup ..."
        ccRecvs = 'chen.chaoqun.ext@99cloud.net,'
        ## ccRecvs = 'gu.jie@21viacloud.com,chen.chaoqun.ext@99cloud.net,'
        ## ccRecvs = 'chen.xinfeng@21viacloud.com,chen.chaoqun.ext@99cloud.net'
        authpassport = "DCYVVDRLIGISRQHE"
        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(sender, authpassport)
            contents = contents
            msgtents = '\n'.join(str(i) for i in contents)
            message = MIMEText(msgtents, 'plain', 'utf-8') # text
            # message = MIMEText(msgtents, 'html', 'utf-8') # html
            message["Subject"] = Header(subject, 'utf-8')
            message["Cc"] = ccRecvs
            server.sendmail(sender, receivers.split(",") + ccRecvs.split(",") , message.as_string())
        except smtplib.SMTPException:
            print("-- Error: Failed to mail_print_ ")
        finally:
            server.quit()
        #yagclient.send(to = "chen.xinfeng@21viacloud.com",
        #    cc = ["chen.chaoqun.ext@99cloud.net"],
        #    subject = "This is mail print from VTG_alarms_ ...",
        #    contents = contents)

    def event_of_alarms_(self, site):
        d, rn = Restinterface(self.__ri_alarms_event_urlpath, 0, 'get').action_restinterface_()
        data = json.loads(d)
        Alarm_ = [ alarm for alarm in data["alarm"] ]
        NodeEventSite_ = [ (a['device'], a['type'], a['status-change']) for a in Alarm_ if site == a['device'] ]
        return NodeEventSite_

    @property
    def number_of_alarms_(self):
        """ /api/operational/alarms/alarm-list/number-of-alarms """
        d, rn = Restinterface(self.__ri_alarms_number_urlpath, 0, 'get').action_restinterface_()
        data = json.loads(d)
        NoA = data["number-of-alarms"]
        return NoA

    @property
    def detail_of_alarms_(self):
        d, rn = Restinterface(self.__ri_alarms_detail_urlpath, 0, 'get').action_restinterface_()
        data = json.loads(d)
        devicesAlarm_ = [ alarm['device'] for alarm in data["alarm"] ]
        return devicesAlarm_


""" 
Mergeable Functions

"""
# 2022.4.19 MPC
# 2021.7.26 PRINT Fore.CYAN
# 2021.7.20 PRINT Fore.YELLOW
# 2021.7.12
def alarmprint_content_warn_(self):
    # WARN
    mpc = MPC(" [ WARN ] ", ' Descriptions: {} was down ! '.format(self.__text_intf_brief_), ' Device : {}'.format(self.__deviceName), ' Tenant : {}'.format(self.__deviceOrg) )
    self.__contents = list(mpc)
    # self.__contents.append(" [ WARN ] ")
    # self.__contents.append(' Descriptions: {} was down ! '.format(self.__text_intf_brief_))
    print(Fore.YELLOW + ' Descriptions: {} was down ! '.format(self.__text_intf_brief_))
    # self.__contents.append(' Device : {}'.format(self.__deviceName))
    # self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
    self.__ala.mail_print_(self.__contents)


def alarmprint_content_alert_(self):
    # ALERT
    mpc = MPC(" -[ ALERT ]- ", ' Descriptions: {} was stuck ! '.format(str(self.__text_intf_brief_.split(" ")[0])), ' Device : {}'.format(self.__deviceName), ' Tenant : {}'.format(self.__deviceOrg) )
    self.__contents = list(mpc)
    # self.__contents.append(" [ ALERT ] ")
    # self.__contents.append(' Descriptions: {} was stuck ! '.format(str(self.__text_intf_brief_.split(" ")[0])))
    print(Fore.CYAN + ' Descriptions: {} was stuck ! '.format(str(self.__text_intf_brief_.split(" ")[0])))
    # self.__contents.append(' Device : {}'.format(self.__deviceName))
    # self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
    # print(self.__contents)
    self.__ala.mail_print_(self.__contents)


def alarmprint_content_recipelx_(self):
    # RECIPELx
    mpc = MPC(" [ RECIPELx ] ", ' Device : {}'.format(self.__deviceName), ' Device : {}'.format(self.__deviceName), ' Tenant : {}'.format(self.__deviceOrg))
    self.__contents = list(mpc)
    # self.__contents.append(" [ RECIPELx ] ", ' Descriptions: {} : {} self-cure-function is workful ! '.format(self.__butt['vrf'], self.__butt['name']), )
    # self.__contents.append(' Descriptions: {} : {} self-cure-function is workful ! '.format(self.__butt['vrf'], self.__butt['name']))
    print(Fore.GREEN + ' Descriptions: {} : {} self-cure-function is workful ! '.format(self.__butt['vrf'], self.__butt['name']))
    # self.__contents.append(' Device : {}'.format(self.__deviceName))
    ## debug: self.__contents.append(' Tenant : {}'.format(self.__orgName))
    # self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
    # print(self.__contents)
    self.__ala.mail_print_(self.__contents)


def alarmprint_content_critical_(self, contents):
    # CRITICAL
    # print(" No Any Wan Online Info: " + self.__deviceName + ' ' + self.__deviceOrg)
    contents.append(" [ CRITICAL ] ")
    contents.append(" Descriptions: UNREACHABLE ( Null Wide Area Network In Link... ) ")
    print(Fore.RED + " Descriptions: UNREACHABLE ( Null Wide Area Network In Link... ) ")
    contents.append(' Device : {}'.format(self.__deviceName))
    contents.append(' Tenant : {}'.format(self.__deviceOrg))
    ## ala.mail_print_(contents)
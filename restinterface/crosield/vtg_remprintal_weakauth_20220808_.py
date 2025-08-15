#!/usr/bin/python
#coding: UTF-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from colorama import init, Fore, Back, Style
init(autoreset=True)
from collections import namedtuple
MPC = namedtuple('MprintalContents', ['Tag', 'Descriptions', 'Device', 'Tenant'])


class VTG_remprintal:

    VTG_remprintal = '/api/operational/alarms/alarm-list/alarm'

    host = 'smtp.163.com'
    sender = 'rpc_tvm@163.com'
    authpassport = "DCYVVDRLIGISRQHE"
    year = "2022"

    def __init__(self, *args, **kwargs):

        self.__detail_of_alarms_ = VTG_remprintal
        self.__number_of_alarms_ = '/api/operational/alarms/alarm-list/number-of-alarms'
        self.__event_of_alarms_  = VTG_remprintal


        self.__mb_html_c = "\
            \n<tr>\
              \n<td align=\"left\" style=\"padding-top:30px;line-height:24px;font-size:10px;color:#808080;font-family:Helvetica;padding:10px 0px 10px 0px\">\
                \n<p style=\"font-size: 10px\">(c) {} Powered by TSunx<br>\
                  \nThis is an automatically generated email by Vegetablesoup. Replies or queries are not monitored or answered.<br></p>\
              \n</td>\
            \n</tr>"

        self.__mb_html_b = "\
            \n<tr>\
              \n<td align=\"left\" style=\"padding-top:30px;line-height:24px;font-size:15px;color:#3c3c3c;font-family:Helvetica;padding:10px 0px 10px 0px\">\
                \n<p style=\"font-size: 13px;padding-top:0%;\"><span style=\"padding-right:5px;\">{}</span></p>\
              \n</td>\
            \n</tr>"


        self.__help = "\
            \n<tr>\
              \n<td align=\"left\" style=\"line-height:24px;font-size:15px;color:#3c3c3c;font-family:Helvetica;padding:5px 0px 5px 0px\"><p style=\"margin:0;line-height:24px;font-size:15px;color:#3c3c3c;font-family:Helvetica;word-spacing:0px;padding:5px 0px 0px 0px\">\
                \nTo offer a better maintenance experience, please contact gu.jie@99cloud.net</p></td>\
            \n</tr>"


    def mailbody_html_(self, contents):
        mailbody_html_ = "\
            \n<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\">\
              \n<tbody>"
        for i in contents:
            mb_html_b = self.__mb_html_b.format(i)
            mailbody_html_ += mb_html_b
        mailbody_html_ += "\
              \n</tbody>\
            \n</table>"
        mailbody_html_ += self.__mb_html_c.format(self.__class__.year)
        mailbody_html_ += self.__help
        return mailbody_html_


    def mailbody_str_(self, contents):
        mailbody_str_ = '\n'.join(str(i) for i in contents)
        return mailbody_str_


    async def mAil_printal_(self, contents, recvs, ccrecvs):
        host = self.__class__.host
        sender = self.__class__.sender
        receivers = recvs
        subject = "Hey! Mail Monitor Printer ( Yummy Stands ) Powered by TSunx"
        ccRecvs = ccrecvs
        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(sender, self.__class__.authpassport)
            contents = contents
            msgtents = self.mailbody_html_(contents)
            message = MIMEText(msgtents, 'html', 'utf-8')
            message["Subject"] = Header(subject, 'utf-8')
            message["Cc"] = ccRecvs
            server.sendmail(sender, receivers.split(",") + ccRecvs.split(",") , message.as_string())
            print("-- Succeed to mAil_printal_ ")
        except smtplib.SMTPException:
            print("-- Error: Failed to mail_print_ ")
        finally:
            server.quit()


    def mail_print_(self, contents):
        host = 'smtp.163.com'
        sender = 'rpc_tvm@163.com'
        # receivers = 'chen.xinfeng@21viacloud.com'
        receivers = 'gu.jie@21viacloud.com'
        subject = "Hey! Mail Print Powerby TSunx"
        # ccRecvs = 'chen.xinfeng@21viacloud.com,chen.chaoqun.ext@99cloud.net'
        ccRecvs = 'gu.jie@21viacloud.com,chen.chaoqun.ext@99cloud.net,'
        authpassport = "DCYVVDRLIGISRQHE"
        try:
            server = smtplib.SMTP()
            server.connect(host)
            server.login(sender, authpassport)
            contents = contents
            msgtents = self.mailbody_html_(contents)
            message = MIMEText(msgtents, 'html', 'utf-8')
            message["Subject"] = Header(subject, 'utf-8')
            message["Cc"] = ccRecvs
            server.sendmail(sender, receivers.split(",") + ccRecvs.split(",") , message.as_string())
        except smtplib.SMTPException:
            print("-- Error: Failed to mail_print_ ")
        finally:
            server.quit()


    def event_of_alarms_(self, site):
        d, _ = Restinterface(self.__event_of_alarms_, 0, 'get').action_restinterface_()
        data = json.loads(d)
        Alarm_ = [ alarm for alarm in data["alarm"] ]
        return [ (a['device'], a['type'], a['status-change']) for a in Alarm_ if site == a['device'] ]


    def number_of_alarms_(self):
        #/api/operational/alarms/alarm-list/number-of-alarms
        d, _ = Restinterface(self.__number_of_alarms_, 0, 'get').action_restinterface_()
        data = json.loads(d)
        return data["number-of-alarms"]


    def detail_of_alarms_(self):
        d, _ = Restinterface(self.__detail_of_alarms_, 0, 'get').action_restinterface_()
        data = json.loads(d)
        devicesAlarm_ = [ alarm['device'] for alarm in data["alarm"] ]
        return devicesAlarm_


""" 
Mergable Functions

"""
# 2022.8.2  mAil_printal
# 2021.7.26 PRINT Fore.CYAN
# 2021.7.20 PRINT Fore.YELLOW
# 2021.7.12
def alarmprint_content_warn_(self):
        # WARN
        self.__contents.append(" [ WARN ] ")
        self.__contents.append(' Descriptions: {} was down ! '.format(self.__text_intf_brief_))
        print(Fore.YELLOW + ' Descriptions: {} was down ! '.format(self.__text_intf_brief_))
        self.__contents.append(' Device : {}'.format(self.__deviceName))
        self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
        self.__ala.mail_print_(self.__contents)
        # self.__ala.mAil_printal_(self.__contents, 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')


def alarmprint_content_alert_(self):
        # ALERT
        self.__contents.append(" [ ALERT ] ")
        self.__contents.append(' Descriptions: {} was stuck ! '.format(str(self.__text_intf_brief_.split(" ")[0])))
        print(Fore.CYAN + ' Descriptions: {} was stuck ! '.format(str(self.__text_intf_brief_.split(" ")[0])))
        self.__contents.append(' Device : {}'.format(self.__deviceName))
        self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
        self.__ala.mail_print_(self.__contents)
        # self.__ala.mAil_printal_(self.__contents, 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')


def alarmprint_content_recipelx_(self):
        # RECIPELx
        self.__contents.append(" [ RECIPELx ] ")
        self.__contents.append(' Descriptions: {} : {} self-cure-function is workful ! '.format(self.__butt['vrf'], self.__butt['name']))
        print(Fore.GREEN + ' Descriptions: {} : {} self-cure in function ! '.format(self.__butt['vrf'], self.__butt['name']))
        self.__contents.append(' Device : {}'.format(self.__deviceName))
        self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
        self.__ala.mail_print_(self.__contents)
        # self.__ala.mAil_printal_(self.__contents, 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')


def alarmprint_content_critical_(self):
        # CRITICAL
        # print(" No Any Wan Online Info: " + self.__deviceName + ' ' + self.__deviceOrg)
        self.__contents.append(" [ CRITICAL ] ")
        self.__contents.append(" Descriptions: UNREACHABLE ( Null Wide Area Network In Environlink... ) ")
        print(Fore.RED + " Descriptions: UNREACHABLE ( Null Wide Area Network In Environlink... ) ")
        self.__contents.append(' Device : {}'.format(self.__deviceName))
        self.__contents.append(' Tenant : {}'.format(self.__deviceOrg))
        self.__ala.mail_print_(self.__contents)
        # print(" Alarm mail sent: ", device)
        # await ala.mAil_printal_(contents, 'wuclv@navimentum.com', 'wuclv@navimentum.com,Jerry.Liu@YumChina.com,chen.chaoqun.ext@99cloud.net,')
        # await ala.mAil_printal_(self.__contents, 'wuclv@navimentum.com', 'wuclv@navimentum.com,Jerry.Liu@YumChina.com,')
        # self.__ala.mAil_printal_(self.__contents, 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')


async def alarmprintal_content_critical_(ala, deviceName, deviceOrg):
    # CRITICAL
    mpc = MPC(" [ CRITICAL ] ", 
              ' Descriptions: UNREACHABLE ( Null Wide Area Network In Environlink... ) ',
              ' Device : {}'.format(deviceName), 
              ' Tenant : {}'.format(deviceOrg))
    # print(" Alarm mail sent: ", device)
    # await ala.mAil_printal_(contents, 'wuclv@navimentum.com', 'wuclv@navimentum.com,Jerry.Liu@YumChina.com,chen.chaoqun.ext@99cloud.net,')
    # await ala.mAil_printal_(self.__contents, 'wuclv@navimentum.com', 'wuclv@navimentum.com,Jerry.Liu@YumChina.com,')
    await ala.mAil_printal_(list(mpc), 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')
    '''
    if ("-TJ-" in device):
        await ala.mAil_printal_(list(mpc), 'peikun.song@yumchina.com', 'peikun.song@yumchina.com,boyu.li@yumchina.com,chen.chaoqun.ext@99cloud.net,')
    '''
    print(Fore.RED + " Descriptions: UNREACHABLE ( Null Wide Area Network In Environlink... ) ")


async def alarmprintal_content_recipelx_(ala, deviceName, deviceOrg, butt):
    # RECIPELx
    mpc = MPC(" [ RECIPELx ] ", 
              ' Descriptions: {} : {} self-cure-function is workful ! '.format(butt['vrf'], butt['name']),
              ' Device : {}'.format(deviceName), 
              ' Tenant : {}'.format(deviceOrg))
    await ala.mAil_printal_(list(mpc), 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')
    print(Fore.GREEN + ' Descriptions: {} : {} self-cure in function ! '.format(butt['vrf'], butt['name']))


async def alarmprintal_content_alert_(ala, deviceName, deviceOrg, text_intf_brief_):
    # ALERT
    mpc = MPC(" [ ALERT ] ", 
              ' Descriptions: {} was stuck ! '.format(str(text_intf_brief_.split(" ")[0])),
              ' Device : {}'.format(deviceName), 
              ' Tenant : {}'.format(deviceOrg))
    await ala.mAil_printal_(list(mpc), 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')
    print(Fore.CYAN + ' Descriptions: {} was stuck ! '.format(str(text_intf_brief_.split(" ")[0])))


async def alarmprintal_content_warn_(ala, deviceName, deviceOrg, text_intf_brief_):
    # WARN
    mpc = MPC(" [ WARN ] ", 
              ' Descriptions: {} was down ! '.format(text_intf_brief_),
              ' Device : {}'.format(deviceName), 
              ' Tenant : {}'.format(deviceOrg))
    await ala.mAil_printal_(list(mpc), 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')
    print(Fore.YELLOW + ' Descriptions: {} was down ! '.format(text_intf_brief_))


async def alarmprintal_content_park_(ala, deviceName, deviceOrg, text_intf_brief_):
    # PARK
    mpc = MPC(" [ PARK ] ", 
              ' Descriptions: {} is trafficless ! '.format(text_intf_brief_),
              ' Device : {}'.format(deviceName), 
              ' Tenant : {}'.format(deviceOrg))
    await ala.mAil_printal_(list(mpc), 'chen.chaoqun.ext@99cloud.net', 'chen.chaoqun.ext@99cloud.net,')
    print(Fore.BLUE + ' Descriptions: {} was trafficless ! '.format(text_intf_brief_))                            
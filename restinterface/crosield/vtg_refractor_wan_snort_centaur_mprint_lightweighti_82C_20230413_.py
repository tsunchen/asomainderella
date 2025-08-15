#!/usr/bin/python
#coding: UTF-8
import time, os
from .vtg_alarms_weakauth_ import *
from ...director.refractor_ import VTGThread_refractor
from .vtg_device_ import *
from .vtg_routines_ import *
import collections
from .vtg_appliance_ import *

sc = Softcohesion()

#     --  ----------  --
#    ( ( ( ( ( ( ( ( ( ( Steak
#     --  ----------  --

#    aspect distributer(threadTab) 切面分配器（牛排）

#    spectrum runner(orgIntfs_) 层次运作者（切牛排）

#    igniter(runny) 点火器（炉灶点火）

#    routines(taster_, attendant) 协程流（品尝者与厨师模式）vtg_routines_

@sc.secit()
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_critical_", alarmprint_content_critical_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_warn_", alarmprint_content_warn_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_alert_", alarmprint_content_alert_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_recipelx_", alarmprint_content_recipelx_)
@sc.pointmerge(VTGThread_refractor, "attendant", attendant)
@sc.pointmerge(VTGThread_refractor, "taster_", taster_)
@sc.pointmerge(VTGThread_refractor, "keydefval_", keydefval_)
def wan_snortry(self):
    setattr(VTG_interface, "default_wan_table_", default_wan_table_)
    # thread_posted = threading.current_thread().getName()
    self.__delay = threading.current_thread().delay
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    # print(self.__delay)
    # time.sleep(int(self.__delay))
    ## print("[%s]" % threading.current_thread().getName())
    dev = VTG_device(devicename = self.__deviceName)
    # 2020.4.9 devicesName -> org_ping
    # intfs = VTG_interfaces(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
    intf = VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
    # 2021.5.13 hostName -> intfs.default_wan_table_
    rc, unit = intf.unit_
    # 2020.12.21
    contents = []
    if (200 == rc):
        setattr(VTGThread_refractor, "run", orgIntfs_)

        thread_list = [ threadTab(text_intf_ = "", text_intf_brief_ = "", threadItem = butt, 
                        dev = dev, hostName = intf.default_wan_table_, deviceName = self.__deviceName, 
                        deviceOrg = self.__deviceOrg, contents = contents, ala = VTG_alarms()) for butt in unit['org_intf'] ]

        # 2021.6.15
        d = collections.deque(thread_list)

        lLeft = threading.Thread(target = runny, args = ('left', d.popleft))
        rRight = threading.Thread(target = runny, args = ('right', d.pop))

        lLeft.start()
        rRight.start()

        lLeft.join()
        rRight.join()

        print("")
    else:        
        # " No Any Wan Online Info: "
        # critical alarm-printing
        self.alarmprint_content_critical_(contents)


""" igniter """
def runny(direction, nextfoo):
    while True:
        try:
            value = nextfoo()
        except IndexError:
            break
        else:
            # print('{:>8}:{}'.format(direction, value))
            value.start()
    # print('{:>8} launch...'.format(direction))


""" aspect distributer """
def threadTab(**kwargs):
    delay = "0"
    thread_post = kwargs['threadItem']
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("text_intf_", kwargs['text_intf_'])
    refrac.__setattr__("text_intf_brief_", kwargs['text_intf_brief_'])
    refrac.__setattr__("butt", kwargs['threadItem'])
    refrac.__setattr__("dev", kwargs['dev'])
    refrac.__setattr__("hostName", kwargs['hostName'])
    refrac.__setattr__("deviceName", kwargs['deviceName'])
    refrac.__setattr__("deviceOrg", kwargs['deviceOrg'])
    refrac.__setattr__("contents", kwargs['contents'])
    refrac.__setattr__("ala", kwargs['ala'])
    return refrac

""" spectrum runner """
def orgIntfs_(self):
    self.delay = threading.current_thread().delay
    self.text_intf_ = threading.current_thread().text_intf_
    self.text_intf_brief_ = threading.current_thread().text_intf_brief_
    self.butt = threading.current_thread().butt
    self.dev = threading.current_thread().dev
    self.hostName = threading.current_thread().hostName
    self.deviceName = threading.current_thread().deviceName
    self.deviceOrg = threading.current_thread().deviceOrg
    self.contents = threading.current_thread().contents
    self.ala = threading.current_thread().ala
    # time.sleep(int(self.__delay))
    if ("wan" == self.butt['type'] and "MPLS" not in self.butt['vrf'].upper()):
        tasting = self.taster_()
        self.attendant(tasting)


""" inspector model (Aurora ( admin ) MPrintal) """
def item_event_detail_stateinspector_Model82(orgName):
    setattr(VTGThread_refractor, "run", wan_snortry)
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    # hub internet, cpe internet
    # devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    thread_table = [ threadTab_item_event_detail_stateinspector_Model82(item, orgName) for item in devicesName_ ]
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    ##self.file_message(' State inspect on : ' + orgName +  ' execute during ' + str((eT - sT).seconds) + ' sec')

def threadTab_item_event_detail_stateinspector_Model82(threadItem, org):
    delay = "0"
    thread_post = threadItem
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("deviceName", threadItem)
    refrac.__setattr__("deviceOrg", org)
    return refrac


""" inspector model Recipelx interface """
def item_event_detail_recipelxintf_Model(devName, orgName):
    setattr(VTGThread_refractor, "run", wan_snortry)
    devicesName_ = [ devName ]
    thread_table = [ threadTab_item_event_detail_recipelxintf_(item, orgName) for item in devicesName_ ]
    print(thread_table)
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    print(' Refractory Recipelx Wan interfaces on : ' + orgName +  ' executed. ')
    ##tkinter.messagebox.showinfo("Recipelx", ' Refractory Recipelx Wan-interfaces on : ' + devName +  ' is executed. ')

def threadTab_item_event_detail_recipelxintf_(threadItem, org):
    delay = "0"
    thread_post = threadItem
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("deviceName", threadItem)
    refrac.__setattr__("deviceOrg", org)
    return refrac
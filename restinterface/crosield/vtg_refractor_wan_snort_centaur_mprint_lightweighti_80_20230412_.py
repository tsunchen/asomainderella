#!/usr/bin/python
#coding: UTF-8
import time, os
from .vtg_alarms_weakauth_ import *
from ...director.refractor_ import VTGThread_refractor
from .vtg_device_ import *
from .vtg_routines_ import *
import collections
from .vtg_appliance_ import *
from pprint import pprint

threadIter = collections.namedtuple('threadIter', [
            'text_intf_',
            'text_intf_brief_',
            'threadItem',
            'dev',
            'hostName',
            'deviceName',
            'deviceOrg',
            'contents',
            'ala'])

sc = Softcohesion()

@sc.secit()
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_alert_", alarmprint_content_alert_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_critical_", alarmprint_content_critical_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_warn_", alarmprint_content_warn_)
@sc.pointmerge(VTGThread_refractor, "alarmprint_content_recipelx_", alarmprint_content_recipelx_)
@sc.pointmerge(VTGThread_refractor, "mprintal", bool(False)) # 2022.5.29 mprintal default setting is false
@sc.pointmerge(VTGThread_refractor, "arrange_", arrange_)
@sc.pointmerge(VTGThread_refractor, "step_", step_)
@sc.pointmerge(VTGThread_refractor, "once_", once_)
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
    intf = VTG_interface(devicename = self.__deviceName, deviceorg = self.__deviceOrg)
    # 2021.5.13 hostName -> intfs.default_wan_table_
    rc, unit = intf.unit_
    # 2020.12.21
    if (200 == rc):

        iThread = [ threadIter(text_intf_ = "", text_intf_brief_ = "", threadItem = butt, dev = dev, hostName = intf.default_wan_table_, deviceName = self.__deviceName, deviceOrg = self.__deviceOrg, contents = [], ala = VTG_alarms()) for butt in unit['org_intf'] ]
        # pprint(iThread)

        # 2021.6.15
        d = collections.deque(list(map(threadTab, iThread)))
        # pprint(d)

        setattr(VTGThread_refractor, "run", orgIntfs_)

        rRight = threading.Thread(target = runny, args = ('right', d.pop))
        lLeft = threading.Thread(target = runny, args = ('left', d.popleft))

        rRight.start()
        lLeft.start()

        lLeft.join()
        rRight.join()

        print("")
    else:        
        # " No Any Wan Online Info: "
        # critical alarm-printing
        self.alarmprint_content_critical_([])

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
def threadTab(threadIter):
    delay = "0"
    thread_post = threadIter.threadItem
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("text_intf_", threadIter.text_intf_)
    refrac.__setattr__("text_intf_brief_", threadIter.text_intf_brief_)
    refrac.__setattr__("butt", threadIter.threadItem)
    refrac.__setattr__("dev", threadIter.dev)
    refrac.__setattr__("hostName", threadIter.hostName)
    refrac.__setattr__("deviceName", threadIter.deviceName)
    refrac.__setattr__("deviceOrg", threadIter.deviceOrg)
    refrac.__setattr__("contents", threadIter.contents)
    refrac.__setattr__("ala", threadIter.ala)
    return refrac


""" spectrum runner """
def orgIntfs_(self):
    # time.sleep(int(self.__delay))
    self.delay = threading.current_thread().delay
    self.__text_intf_ = threading.current_thread().text_intf_
    self.__text_intf_brief_ = threading.current_thread().text_intf_brief_
    self.__butt = threading.current_thread().butt
    self.__dev = threading.current_thread().dev
    self.__hostName = threading.current_thread().hostName
    self.__deviceName = threading.current_thread().deviceName
    self.__deviceOrg = threading.current_thread().deviceOrg
    self.contents = threading.current_thread().contents
    self.__ala = threading.current_thread().ala
    if ("wan" == self.__butt['type'] and "MPLS" not in self.__butt['vrf'].upper()):
        """ Arrange Step Once """
        ASO(self.once_()).run()

""" inspector model (Aurora ( admin ) MPrintal) """
def item_event_detail_stateinspector_Model(orgName):
    appliance = VTG_appliance(deviceorg = orgName)
    _, d = appliance.location_
    data = json.loads(d)
    print(json.dumps(data, indent = 4))
    # hub internet, cpe internet
    # devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' and tc['type'] != 'hub' ]
    devicesName_ = [ tc['applianceName'] for tc in data["List"]['value'] if tc['type'] != 'controller' ]
    setattr(VTGThread_refractor, "run", wan_snortry) # 2022.5.29 found run using stateinspector then recipelx start up, might run wan_snortry having more function
    thread_table = [ threadTab_item_event_detail_(item, orgName) for item in devicesName_ ]
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    ## self.file_message(' State inspect on : ' + orgName +  ' execute during ' + str((eT - sT).seconds) + ' sec')

""" inspector model Recipelx interface """
def item_event_detail_recipelxintf_Model(devName, orgName):
    devicesName_ = [ devName ]
    setattr(VTGThread_refractor, "run", wan_snortry)
    thread_table = [ threadTab_item_event_detail_(item, orgName) for item in devicesName_ ]
    print(thread_table)
    for thread in thread_table:
        thread.start()
    for thread in thread_table:
        thread.join()
    print(' Refractory Recipelx Wan interfaces on : ' + orgName +  ' executed. ')
    ## tkinter.messagebox.showinfo("Recipelx", ' Refractory Recipelx Wan-interfaces on : ' + devName +  ' is executed. ')

""" thread table """
def threadTab_item_event_detail_(threadItem, org):
    delay = "0"
    thread_post = threadItem
    refrac = VTGThread_refractor(thread_name = ("%s" % thread_post))
    refrac.__setattr__("delay", delay)
    refrac.__setattr__("deviceName", threadItem)
    refrac.__setattr__("deviceOrg", org)
    return refrac
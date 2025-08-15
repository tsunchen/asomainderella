from .tsx_popitem_ import ( 
    cohoMethod,
    popitem_pathmetric,
    popitem_event,
    popitem_assource,
    popitem_interfaces,
    popitem_interentries,
    popitem_recipelxintf,
    popitem_carrier,
    popitem_httpsconft,
    popitem_renewal,
    popitem_hardware,
)
import tkinter as tk
from ...director.cohesionar_ import (
    Softcohesion, 
    seco_string_,
    step_str,
)
from .vtg_refractor_wan_snort_centaur_mprint_lightweighti_80_ import (
    item_event_detail_stateinspector_Model
)
from .vtg_refractor_wan_snort_centaur_mprint_lightweighti_82C_ import (
    item_event_detail_stateinspector_Model82,
    item_event_detail_recipelxintf_Model,
)
from .vtg_refractor_devspoke_passpertotalplus_ import (
    devspokepasspertotal10sinspectorModel
)
from .vtg_refractor_devspoke_passpertotal_ import (
    devspokepasspertotalinspectorModel
)
from .vtg_refractor_devspoke_priority_ import (
    devspokepriorityinspectorModel
)
from .vtg_reflection_deco_devslapathmetrics_ import (
    devslainspectorModel
)
from .vtg_reflection_deco_devspoke_sum_ import (
    devspokesuminspectorModel
)
from .vtg_reflection_deco_devspoke_ import (
    devspokeinspectorModel
)
from .vtg_refractor_devspoke_summary_ import (
    devspokesumminspectorModel
)
from .vtg_refractor_cpn_snort_centaur_ import (
    cpninspectorModel
)
from .vtg_refractor_wan_snort_centaur_aoi_ import (
    waninspectorModelaoi
)
from .vtg_reflection_deco_path_ import (
    pathmplsinspectorModel,
    pathmetricsinspectorModel
)
from .vtg_refractor_wan_snort_centaur_ import (
    waninspectorModel
)
from .vtg_reflection_deco_interface_aurora_ import (
    interfaceinspectorModel
)
from .vtg_reflection_deco_lans_ import (
    lanorginspectorModel
)
from .vtg_refractor_lan_parse_centaur_ import (
    lanparseModel
)
from .vtg_refractor_lan_snort_centaur_ import (
    laninspectorModel
)
from .vtg_refractor_lan_snort_centauraio_ import (
    aiolaninspectorModel
)
from .vtg_refractor_lan_snort_acentaur_ import (
    alaninspectorModel
)
from .vtg_refractor_lan_camouflage_acentaur_ import (
    alanreliableModel
)
from .vtg_refractor_lan_suspend_centaur_ import (
    lansuspendsoryModel
)
from .vtg_reflection_deco_serialnumber_ import (
    snorginspectorModel
)
from .vtg_reflection_deco_hardwareidnumber_ import (
    hinorginspectorModel
)
from .vtg_refractor_hardware_id_numbers_ import (
    hwidnumsinspectorModel
)
from .vtg_reflection_deco_devspecificservicetemplate_ import (
    devsstinspectorModel
)
from tkinter import *
from .vtg_org_ import VTG_org
import json
from .vtg_system_ import VTG_system
import tkinter
import tkinter.ttk
from .vtg_appliance_ import VTG_appliance
#from .__init__ import *
from .vtg_interface_ import VTG_interface
from .vtg_device_ import VTG_device
from .vtg_template_ import VTG_template
import yaml
from .vtg_spokegroup_ import VTG_spokegroup
from .vtg_vrouter_ import VTG_vrouter
from .vtg_sdwan_ import (
    VTG_sdwan
)
#from .vtg_refractor_devspoke_passpertotalplus_llm_ import (
#    devspokepasspertotal10sinspectorModel_llm
#)
import re


@cohoMethod(popitem_pathmetric)
@cohoMethod(popitem_event)
@cohoMethod(popitem_assource)
@cohoMethod(popitem_interfaces)
@cohoMethod(popitem_interentries)
@cohoMethod(popitem_recipelxintf)
@cohoMethod(popitem_carrier)
@cohoMethod(popitem_httpsconft)
@cohoMethod(popitem_renewal)
@cohoMethod(popitem_hardware)
class StatusField(tk.Frame):

    def __init__(self, master = None):
        self.__root = ""
        self.__title = " _Status Field_ Powerby TSunx @ V.T.G.A "
        self.style = "" # flash treeview
        self.last_command = None # Initialize the list with None to track the last command
        # Button to execute the last executed command 2024.7.31
        self.btn_last_command = None # self.btn_last_command.pack(pady=10)


    def create_widgets(self):
        window = tk.Tk()
        window.title(self.__title)

        self.sourceaddressvrf = StringVar()
        self.targetaddressvrf = StringVar()
        self.fetchhubByitem_brief = StringVar()
        self.fetchdevicenameByitem_brief = StringVar()
        self.fetchhubByitem_event = StringVar()
        self.fetchdevicenameByitem_event = StringVar()
        self.pulldevicenameByTenant = StringVar()
        self.fetchdeviceuuidByitem_brief = StringVar()
        self.pushfilename = StringVar()

        root = tk.Frame(window)
        root.pack(fill = BOTH, expand = 1)

        self.__root = root

        Label(root, text = ' Tenants ').grid(row = 6, column = 3)

        Label(root, text = '  -  Virtual Transmit Gearing Appliances  -  ').grid(row = 6, column = 0, columnspan = 2)
        self.organizations()
        self.org_combobox = tkinter.ttk.Combobox(root, values = self.orgName_tuple, width = 24)
        self.org_combobox.bind("<<ComboboxSelected>>", self.orgValue)
        self.org_combobox.current(0)
        self.org_combobox.grid(row = 7, column = 3, sticky = 'NEW', rowspan = 2)

        self.vbar = tkinter.ttk.Scrollbar(root, orient = 'vertical')
        self.treeview = tkinter.ttk.Treeview(root, columns = ("type", "name", "uuid", "event"), show = "headings", height = 13, padding = (10, 5, 10, 5), yscrollcommand = self.vbar.set)
        self.vbar['command'] = self.treeview.yview
        self.vbar.grid(row = 7, column = 2, sticky = 'NS')

        self.treeview.heading(column = "type", text = "Type")
        self.treeview.heading(column = "name", text = "Name")
        self.treeview.heading(column = "uuid", text = "UUid")
        self.treeview.heading(column = "event", text = "Event")
        self.treeview.column("type", width = 100, anchor = tkinter.CENTER)
        self.treeview.column("name", width = 340, anchor = tkinter.CENTER)
        self.treeview.column("uuid", width = 300, anchor = tkinter.CENTER)
        self.treeview.column("event", width = 60, anchor = tkinter.CENTER)
        self.treeview.bind("<Double-Button-1>", self.item_brief)
        self.treeview.bind("<Double-Button-2>", self.item_hardware)
        self.treeview.grid(row = 7, column = 0, columnspan = 2)

        self.pop_menu = tkinter.Menu(root, tearoff = False)
        self.pop_menu.add_command(label = "Recommandation based by metric ", command = self.popitem_pathmetric)
        self.pop_menu.add_command(label = "Events on the past perfect tense ", command = self.popitem_event)
        self.pop_menu.add_command(label = "Step in deep... ", command = self.popitem_assource)
        self.pop_menu.add_command(label = "    - Interfaces ", command = self.popitem_interfaces)
        self.pop_menu.add_command(label = "    - Interentries ", command = self.popitem_interentries)
        self.pop_menu.add_command(label = "    - Recipelxal ", command = self.popitem_recipelxintf)
        self.pop_menu.add_command(label = "    - LTE carrier ", command = self.popitem_carrier)
        self.pop_menu.add_command(label = "Conf termial over https ", command = self.popitem_httpsconft)
        self.pop_menu.add_command(label = "Renewal flow ", command = self.popitem_renewal)
        self.pop_menu.add_command(label = "Hardware info ", command = self.popitem_hardware)

        menu = tkinter.Menu(self.__root)
        window.config(menu = menu)

        action = tkinter.Menu(menu)
        action.add_command(label = 'Exit', command = root.quit)
        action.add_separator()
        action.add_command(label = 'Overlay Ping < ', command = self.item_event_lanpings_b2b_)
        action.add_command(label = 'Overlay Ping > (Reversal) ', command = self.item_event_lanpings_b2b_reversal_)

        # 2021.5.7 enable Moirae in emergency
        emergency = tkinter.Menu(menu)
        emergency.add_command(label = 'Moirae（shift on properly and implicitly）', command = self.item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2b_hopper_by_hub_)
        emergency.add_command(label = 'Führung（out of service on the local flow）', command = self.lansuspendory)

        spokes = tkinter.Menu(menu)
        spokes.add_command(label = 'MPLS Reachablility ', command = self.pathmplsinspector)
        spokes.add_command(label = 'IPSec.Stats ', command = self.item_event_detail_ipsec_stats_)
        subSpokes_topologic = tkinter.Menu(spokes, tearoff = 0)
        subSpokes_topologic.add_command(label = 'Priority ( Customer Experience ) ', command = self.devspokepriorityinspector)
        subSpokes_topologic.add_command(label = 'Visibility ', command = self.devslainspector)
        subSpokes_topologic.add_command(label = 'Pass-per-Total ( Customer Experience ) ', command = self.devspokepasspertotalinspector)
        subSpokes_topologic.add_command(label = 'Pass-per-Total+ ( Customer Experience ) ', command = self.devspokepasspertotal10sinspector)
        # subSpokes_topologic.add_command(label = 'Pass-per-Total+llm ( Customer Experience ) ', command = self.devspokepasspertotal10sinspectorllm)
        spokes.add_command(label = 'Sum ', command = self.devspokesuminspector)
        spokes.add_command(label = 'Listing ', command = self.devspokeinspector)
        spokes.add_command(label = 'Summary ', command = self.devspokesumminspector)

        branch = tkinter.Menu(menu)
        subBranch_visibility = tkinter.Menu(branch, tearoff = 0)
        subBranch_visibility.add_command(label = 'Branch.2.Hub ', command = self.item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2b_by_hub_)
        subBranch_visibility.add_command(label = 'Tube ', command = self.item_event_detail_sdwan_slapathmetrics_objects_devslainspector_)
        branch.add_command(label = 'SLA Path metrics ', command = self.item_event_detail_sdwan_slapathmetrics_objects_spokegrouphubs_)
        branch.add_command(label = 'Spoke group hubs devtemplate ', command = self.item_event_detail_spokegrouphubs_devtemplate_)
        branch.add_command(label = 'Site BGP neighbor lan ', command = self.item_event_detail_bgp_neighbor_lan_)

        # 2024.7.31 self.btn_last_command.pack(pady=10)
        self.btn_last_command = Button(root, text="Centaur Button", command = self.execute_last_command, fg = "Gray")
        self.btn_last_command.grid(row = 2, column = 3)

        infor = tkinter.Menu(menu)
        infor.add_command(label = 'Centauraoic ( operate )  ', command = self.waninspectoraoi)
        infor.add_command(label = 'C.O.N.N ', command = self.item_event_connstate_b2b_)
        infor.add_command(label = 'Aurora ( admin ) MPrintal ', command = self.item_event_detail_stateinspector_)
        infor.add_command(label = 'Aurora ( admin ) MPrintal 82 ', command = self.item_event_detail_stateinspector82_)
        infor.add_command(label = 'Serial number ', command = self.snorginspector)
        infor.add_command(label = 'CSV Path metrics ', command = self.pathmetricsinspector)
        infor.add_command(label = 'Hardware ID Number ', command = self.hinorginspector)
        infor.add_command(label = 'Hardware ID Number with table ', command = self.hardwareidnumbers)
        infor.add_command(label = 'Specific service ', command = self.devsstinspector)
        subInfor_lan = tkinter.Menu(infor, tearoff = 0)
        subInfor_lan.add_command(label = 'Availabilities ', command = self.laninspector)
        subInfor_lan.add_command(label = 'Parse ', command = self.lanparse)
        subInfor_lan.add_command(label = 'Table ', command = self.lanorginspector)
        subInfor_lan.add_command(label = 'Availabilitiesaoic ', command = self.aiolaninspector)
        subInfor_lan.add_command(label = 'The Availability ', command = self.alaninspector)
        subInfor_lan.add_command(label = 'Reliability ', command = self.alanreliable)

        cloudprivatenetwork = tkinter.Menu(menu)
        cloudprivatenetwork.add_command(label = 'Cloudviron ', command = self.cpninspector)

        menu.add_cascade(label = 'Act', menu = action)
        menu.add_cascade(label = 'Deus ex Machina', menu = emergency)
        menu.add_cascade(label = 'Branch', menu = branch)
        branch.add_cascade(label = 'Visibility', menu = subBranch_visibility)
        menu.add_cascade(label = 'Spokes', menu = spokes)
        spokes.add_cascade(label = 'Topologic', menu = subSpokes_topologic)
        menu.add_cascade(label = 'Information', menu = infor)
        infor.add_cascade(label = 'i.L.A.N', menu = subInfor_lan)
        menu.add_cascade(label = 'Private', menu = cloudprivatenetwork)

        window.mainloop()


    """ Execute Last Command """
    def execute_last_command(self):
        if self.last_command:
            getattr(self, self.last_command)()
        else:
            print(" - No cloned command executed yet. - ")


    """ renewal pushing filename """
    def selectPushFile(self):
        filepath = askopenfilename()
        self.pushfilename.set(filepath)


    """
    POPITEM
    """
    def pop_handle(self, event):
        self.pop_menu.post(event.x_root, event.y_root)


    """
    overlay conn state
    """
    def item_event_connstate_b2b_(self):
        """ overlay conn state """
        print("rDoubleclick: ", self.fetchdevicenameByitem_event)
        print()
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            org = VTG_org(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get())
            _, d = org.sdwan_slamonitor_stats_path_(target = self.fetchdevicenameByitem_brief)
            res = d
            tkinter.messagebox.showinfo("Overlay Conn State Result", "More org sdwan sla-monitor stats path detail to see on the data window. ")
        else:
            print("[Needing Parameter]: Branch to Branch Overlay Conn State")


    """
    IPSec
    """
    def item_event_detail_ipsec_stats_(self):
        """ IPSec """
        print(self.fetchdevicenameByitem_event)
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event)):
            sec = VTG_ipsec(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get())
            _, d = sec.vpn_stats_()
            print(d)
        else:
            print("[Needing Parameter]: IPSec Stats Info")


    """
    Stateinspector
    """
    # @Softcohesion.secit()
    # @Softcohesion.Intention_IFELSE( model = item_event_detail_stateinspector_Model )
    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = item_event_detail_stateinspector_Model, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def item_event_detail_stateinspector_(self, *args, **kwargs):
        """ State Inspector """
        ...


    """
    Stateinspector82
    """
    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = item_event_detail_stateinspector_Model82, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def item_event_detail_stateinspector82_(self, *args, **kwargs):
        """ State Inspector82 """
        ...


    """
    Intercarrier
    """
    def item_event_detail_interfacescarrier_info_(self):
        """ Intercarrier """
        # print(self.fetchdevicenameByitem_event)
        # print(self.fetchdeviceuuidByitem_brief)
        _, d = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).carrier_(self.fetchdeviceuuidByitem_brief)
        carrier_100_ = json.loads(d)
        print(json.dumps(carrier_100_["collection"]["interfaces:carrier-brief"][0], indent = 4))
        tkinter.messagebox.showinfo("Carrier vni0/100 ", " Signal: {} ".format(json.dumps(carrier_100_["collection"]["interfaces:carrier-brief"][0]["signal"])) )


    """
    Recipelxintf
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IF( model = item_event_detail_recipelxintf_Model )
    def item_event_detail_recipelxintf_(self, *args, **kwargs):
        """ Recipelx Interfaces """
        ...


    """
    Popitem.Interentries
    """
    def item_event_detail_interfacesentry_info_(self):
        """ Interentry """
        print(self.fetchdevicenameByitem_event)
        dev = VTG_device(devicename = self.fetchdevicenameByitem_event)
        _, d = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).entry_
        data_yaml = yaml.dump(json.loads(d))
        dict_yaml_ = yaml.load(data_yaml, Loader = yaml.BaseLoader)
        for item in dict_yaml_["collection"]["arp:interface"]:
            dict_yaml__ = yaml.dump(item)
            dict_yaml_arpentry_ = yaml.load(dict_yaml__, Loader = yaml.BaseLoader)
            value = dict(dict_yaml_arpentry_).values()
            l_value = list(value)
            if ( 2 == len(l_value) ):
                nolan_pageJson_pings_, lan_pageJson_pings_ = [], []
                print("- interport: [" + l_value[1] + "]")
                for item in l_value[0]:

                    pageJson_pings_ = dev.pingx_(hostname = item["ip"], routingInstance = item["routing-instance"], count = 8, packetSize = 45454)

                    if ( "LAN" in item['routing-instance'].upper() ):
                        if "success" == pageJson_pings_.get('status'):
                            lan_pageJson_pings_.append(item['ip'])
                            # print(pageJson_pings_)
                            match = re.search(r'(\d+)% packet loss', pageJson_pings_['result'])
                            if match:
                                packet_loss = match.group(1) + '%'
                                # print("Packet loss:", packet_loss)
                                print('- lan_res : {}@{}={}({})'.format( item["routing-instance"], item["ip"], pageJson_pings_.get('status'), packet_loss ))
                        else:
                            print('- lan_res : {}@{}={}'.format( item["routing-instance"], item["ip"], pageJson_pings_.get('status') ))
                    else:
                        if "success" == pageJson_pings_.get('status'):
                            nolan_pageJson_pings_.append(item['ip'])
                        print('- nolan_res : {}@{}={}'.format( item["routing-instance"], item["ip"], pageJson_pings_.get('status') ))

                try:
                    assert 1 != len(lan_pageJson_pings_)
                except:
                    print(" ! No more than one entry over the local area network ! ")
                else:
                    if 0 != len(lan_pageJson_pings_):
                        print(' @ Healthy LAN-Entries of Number = {},{}'.format(len(lan_pageJson_pings_), lan_pageJson_pings_))
                    elif 0 != len(nolan_pageJson_pings_):
                        print(' @ Healthy No-LAN-Entries of Number = {},{}'.format(len(nolan_pageJson_pings_), nolan_pageJson_pings_))


    """
    P.I.N.G
    """
    """
    overlay lan
    """
    def item_event_lanpings_b2b_reversal_(self):
        """ Reversal Overlay Lan Ping """
        # -d  WanGuo-Demo-HA-1 -g WANGUO-SH-POP
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            device = VTG_device(devicename = self.fetchdevicenameByitem_brief)
            self.sourceaddress = self.targetaddressvrf.get().split('@')[0]
            self.sourceroutingInstance = self.targetaddressvrf.get().split('@')[1]
            self.targetaddress = self.sourceaddressvrf.get().split('@')[0]
            _, d = device.pingi_(hostname = self.targetaddress, routingInstance = self.sourceroutingInstance, source = self.sourceaddress, count = 8, deviceName = self.fetchdevicenameByitem_brief)
            output = d.split("\n")[:1] + d.split("\n")[-4:]
            res = '\n'.join(output)
            tkinter.messagebox.showinfo("Reversal Overlay Lans Ping Result ", res)
        else:
            # print("[Needing Parameter]: Branch to Branch Overlay Lans Ping")
            tkinter.messagebox.showinfo("Reversal Overlay Lans Ping ", "[Needing Parameter]: Branch to Branch Overlay Lans Ping")


    def item_event_lanpings_b2b_(self):
        """ Overlay Lan Ping """
        print("rDoubleclick: ", self.fetchdevicenameByitem_event)
        print()
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        # -d  WanGuo-Demo-HA-1 -g WANGUO-SH-POP
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            device = VTG_device(devicename = self.fetchdevicenameByitem_event)
            # -d CPE-01 -p 10.122.133.254 -o Customer -s 192.168.123.1
            self.sourceaddress = self.sourceaddressvrf.get().split('@')[0]
            self.sourceroutingInstance = self.sourceaddressvrf.get().split('@')[1]
            self.targetaddress = self.targetaddressvrf.get().split('@')[0]
            _, d = device.pingi_(hostname = self.targetaddress, routingInstance = self.sourceroutingInstance, source = self.sourceaddress, count = 8, deviceName = self.fetchdevicenameByitem_event)
            output = d.split("\n")[:1] + d.split("\n")[-4:]
            res = '\n'.join(output)
            tkinter.messagebox.showinfo("Overlay Lans Ping Result ", res)
        else:
            # print("[Needing Parameter]: Branch to Branch Overlay Lans Ping")
            tkinter.messagebox.showinfo("Overlay Lans Ping ", "[Needing Parameter]: Branch to Branch Overlay Lans Ping")


    def lanvni(self, varbool, deviceName, orgName, col, variable):
        if varbool:
            tkinter.messagebox.showinfo("Overlay Lan Pings", "[Needing Parameter]: Branch to Branch Overlay Lan Pings")
        else:
            print(deviceName, ' ', orgName)
            rc, vni = VTG_interface(devicename = deviceName, deviceorg = orgName).unit_
            if (200 == rc):
                Intf, Intf_ini = " " * 98, 300
                for i in range(Intf_ini, Intf_ini + 8):
                    if col:
                        Label(self.__root, text = Intf).grid(row = i, column = col)
                        Label(self.__root, text = Intf).grid(row = i, column = col - 1)
                    else:
                        Label(self.__root, text = Intf).grid(row = i, column = col)
                i = Intf_ini
                Label(self.__root, text = deviceName).grid(row = i, column = col)
                for butt in vni['org_intf']:
                    if ("lan" == butt['type'] or "LAN" in butt['vrf'].upper()):
                        i = i + 1
                        valueButt = butt['address'][0]['ip'].split('/')[0]+'@'+butt['vrf']
                        Intf = Radiobutton(self.__root, text = butt['address'][0]['ip'].split('/')[0]+'@'+butt['name'], value = valueButt, variable = variable) if "up" == butt['if-oper-status'] else Radiobutton(self.__root, text = ' -?- ' + butt['address'][0]['ip'].split('/')[0], value = valueButt, variable = variable)
                        variable.set(valueButt)
                        Intf.grid(row = i, column = col)
            else:
                self.formal_message('interface lanlink scan no content')


    @step_str()
    def vnilantar(self):
        self.lanvni("PY_VAR3" == str(self.fetchdevicenameByitem_brief), self.fetchdevicenameByitem_brief, self.pulldevicenameByTenant.get(), 0, self.targetaddressvrf)


    def vnilan(self):
        self.lanvni("PY_VAR5" == str(self.fetchdevicenameByitem_event), self.fetchdevicenameByitem_event, self.pulldevicenameByTenant.get(), 1, self.sourceaddressvrf)


    """
    slapathmetrics by hub 2021.5.18
    """
    def item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2b_by_hub_(self):
        print("rDoubleclick: ", self.fetchdevicenameByitem_event)
        print()
        print("lDoubleclick: ", self.fetchhubByitem_brief)
        print()
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchhubByitem_brief)):
            hub = self.fetchhubByitem_brief
            sg = VTG_spokegroup( deviceorg = self.pulldevicenameByTenant.get() )
            sg.orgspokegroups_()
            sg.devspokegroups_()
            sg.devspokegroups_hubs_priority_()
            hubdevspokegroupshub_priority = sg.devspokegroups_hub_hub_(hub)
            print(hubdevspokegroupshub_priority)
            #
            if ([] != hubdevspokegroupshub_priority):
                hubdevSpoke = hubdevspokegroupshub_priority[0]
                print()
                # HUBDEV with DEV
                sdn = VTG_sdwan(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get())
                print(hub)
                print()
                # 2021.5.18 Metrics before Hopping
                qualityofTunn = sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_([hub])
                print(qualityofTunn)
                print()
            else:
                print("[Needing Parameter]: Branch by Hub Tube Visibility")


    """
    telepathic_active_slapathmetrics by hub
    """
    def item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2b_hopper_by_hub_(self):
        print("rDoubleclick: ", self.fetchdevicenameByitem_event)
        print()
        # self.fetchhubByitem_brief
        print("lDoubleclick: ", self.fetchhubByitem_brief)
        print()
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchhubByitem_brief)):
            hub = self.fetchhubByitem_brief
            sg = VTG_spokegroup( deviceorg = self.pulldevicenameByTenant.get() )
            sg.orgspokegroups_()
            sg.devspokegroups_()
            sg.devspokegroups_hubs_priority_()
            hubdevspokegroupshub_priority = sg.devspokegroups_hub_hub_(hub)
            print(hubdevspokegroupshub_priority)
            if ([] != hubdevspokegroupshub_priority):
                hubdevSpoke = hubdevspokegroupshub_priority[0]
                print()
                # HUBDEV with DEV
                sdn = VTG_sdwan(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get())
                print(hub)
                # 2021.5.18 Metrics before Hopping
                vtunn = sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_([hub])
                print()
                if (self.formal_message(' PoP (' + hubdevSpoke + ') \n<<< ' + vtunn + '<<<\nBranch (' + self.fetchdevicenameByitem_event +  ')\n\nExecute ... [Y/N]')):
                    print("\" Run -d %s -g %s \"" % (self.fetchdevicenameByitem_event, hubdevSpoke))
                    device_event = VTG_device(devicename = self.fetchdevicenameByitem_event)
                    _, devtemplateName = device_event.templateName_()
                    template = VTG_template(pst = devtemplateName)
                    _, d = template.update_(spokegroup = hubdevSpoke)
                    _, d = template.deploy_()
                    _, d = template.commit_(self.fetchdevicenameByitem_event)
                    data = json.loads(d)
                    print(json.dumps(data, indent = 4))
                else:
                    print("\" Codename -d %s -g %s \"" % (self.fetchdevicenameByitem_event, hubdevSpoke))
                    print("Please copy and paste the above sentences in file for shifting the spoke in emergency.")
            else:
                print("No Spoke Group Created")
        else:
            print("[Needing Parameter]: Branch by Hub Tube Hopper")


    """
    slapathmetrics
    """
    def item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2b_hopper_(self):
        print("rDoubleclick: ", self.fetchdevicenameByitem_event)
        print()
        print("lDoubleclick: ", self.fetchdevicenameByitem_brief)
        print()
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event) and "PY_VAR3" != str(self.fetchdevicenameByitem_brief)):
            hubDev = VTG_device(devicename = self.fetchdevicenameByitem_brief)
            _, devtemplateName = hubDev.templateName_()
            template = VTG_template(pst = devtemplateName)
            _, devSpoke = template.spoke_()
            hubdevSpoke = devSpoke
            sg = VTG_spokegroup(deviceorg = self.pulldevicenameByTenant.get())
            _, sgdev = sg.devspokegroup_(hubdevSpoke)
            hubdevspokegrouphub_priority = sg.devspokegroup_hub_priority_()
            # print(json.dumps(sgdev, indent = 4))
            print()
            # HUBDEV with DEV
            sdn = VTG_sdwan(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get())
            print(sdn.devsla_path_metrics_aggregated_last_1m_brief_prime_(hubdevspokegrouphub_priority))
            print()
            if (self.formal_message(' Hub (' + hubdevSpoke + ') <<< Branch (' + self.fetchdevicenameByitem_event +  ')\n execute ... [Y/N]')):
                print("\" Run -d %s -g %s \"" % (self.fetchdevicenameByitem_event, hubdevSpoke))
                device_event = VTG_device(devicename = self.fetchdevicenameByitem_event)
                _, devtemplateName = device_event.templateName_()
                template = VTG_template(pst = devtemplateName)
                _, d = template.update_(spokegroup = hubdevSpoke)
                _, d = template.deploy_()
                _, d = template.commit_(self.fetchdevicenameByitem_event)
                data = json.loads(d)
                print(json.dumps(data, indent = 4))
            else:
                print("\" Codename -d %s -g %s \"" % (self.fetchdevicenameByitem_event, hubdevSpoke))
                print("Please copy and paste the above sentences in file for shifting the spoke in emergency.")
        else:
            print("[Needing Parameter]: Branch to Branch Tube Hopper")


    """ Popitem.Interfaces """
    def item_event_detail_interfaces_info_(self):
        print(self.fetchdevicenameByitem_event)
        _, d = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).unit_
        data_yaml = yaml.dump(d)
        print(data_yaml)


    """ Branch Tube """
    def item_event_detail_sdwan_slapathmetrics_objects_devslainspector_b2h_(self):
        print(self.fetchdevicenameByitem_event)
        print()
        print(self.fetchhubByitem_event)
        print()
        if ("PY_VAR3" != str(self.fetchdevicenameByitem_event) and "PY_VAR5" != str(self.fetchhubByitem_event)):
            sg = VTG_spokegroup(deviceorg = self.pulldevicenameByTenant.get())
            # print(json.dumps(sgdev, indent = 4))
            print()
            hubspokegroupdev = sg.hubspokegroup_dev_priority_(self.fetchhubByitem_event)
            print(hubspokegroupdev)
            print()
        else:
            print("[Needing Parameter]: Branch to Hub Tube Visibility")


    def item_event_detail_sdwan_slapathmetrics_objects_devslainspector_(self):
        print(self.fetchdevicenameByitem_event)
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event)):
            device = VTG_device(devicename = self.fetchdevicenameByitem_event)
            _, devtemplateName = device.templateName_()
            template = VTG_template(pst = devtemplateName)
            _, devSpoke = template.spoke_()
            if (None != devSpoke):
                sg = VTG_spokegroup(deviceorg = self.pulldevicenameByTenant.get())
                _, sgdev = sg.devspokegroup_(devSpoke)
                # print(json.dumps(sgdev, indent = 4))
                print()
                devspokegrouphubs = sg.devspokegroup_hubs_()
                print(devspokegrouphubs)
                sdn = VTG_sdwan(deviceorg = self.pulldevicenameByTenant.get(), devicename = self.fetchdevicenameByitem_event)
                sdn.devsla_path_metrics_aggregated_last_1m_brief_(devspokegrouphubs)
            else:
                print("( No Spoke Found ) ")
        else:
            print("[Needing Parameter]: Tube Visibility")


    def item_event_detail_sdwan_slapathmetrics_objects_spokegrouphubs_(self):
        print(self.fetchdevicenameByitem_event)
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event)):
            device = VTG_device(devicename = self.fetchdevicenameByitem_event)
            _, devtemplateName = device.templateName_()
            template = VTG_template(pst = devtemplateName)
            _, devSpoke = template.spoke_()
            sg = VTG_spokegroup(deviceorg = self.pulldevicenameByTenant.get())
            _, sgdev = sg.devspokegroup_(devSpoke)
            # print(json.dumps(sgdev, indent = 4))
            print()
            devspokegrouphubs = sg.devspokegroup_hubs_()
            print(devspokegrouphubs)
            sdn = VTG_sdwan(deviceorg = self.pulldevicenameByTenant.get(), devicename = self.fetchdevicenameByitem_event)
            sdn.devsla_path_metrics_aggregated_last_1m_detail_(devspokegrouphubs)
        else:
            print("[Needing Parameter]: SLA Path Metrics")


    """
    P.o.P
    """
    def item_event_detail_spokegrouphubs_devtemplate_(self):
        print(self.fetchdevicenameByitem_event)
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event)):
            device = VTG_device(devicename = self.fetchdevicenameByitem_event)
            _, devtemplateName = device.templateName_()
            template = VTG_template(pst = devtemplateName)
            _, devSpoke = template.spoke_()
            sg = VTG_spokegroup(deviceorg = self.pulldevicenameByTenant.get())
            _, sgdev = sg.devspokegroup_(devSpoke)
            print(json.dumps(sgdev, indent = 4))
            print()
            devspokegrouphubs = sg.devspokegroup_hubs_()
            print(devspokegrouphubs)
        else:
            print("[Needing Parameter]: Spoke Group Hubs Devtemplate")


    """
    B.G.P
    """
    def item_event_detail_bgp_neighbor_lan_(self):
        print(self.fetchdevicenameByitem_event)
        if ("PY_VAR5" != str(self.fetchdevicenameByitem_event)):
            appliance = VTG_vrouter(deviceorg = self.pulldevicenameByTenant.get(), devicename = self.fetchdevicenameByitem_event)
            _, d = appliance.fetch_bgp_neighbor_lan_()
            print(d)
        else:
            print("[Needing Parameter]: BGP Neighbor Lan")


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devspokepasspertotal10sinspectorModel )
    def devspokepasspertotal10sinspector(self, *args, **kwargs):
        ...


    # llm 2025.2
    #@Softcohesion.secit()
    #@Softcohesion.Intention_IFELSE( model = devspokepasspertotal10sinspectorModel_llm )
    #def devspokepasspertotal10sinspectorllm(self, *args, **kwargs):
    #    ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devspokepasspertotalinspectorModel )
    def devspokepasspertotalinspector(self, *args, **kwargs):
        ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devspokepriorityinspectorModel )
    def devspokepriorityinspector(self, *args, **kwargs):
        ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devslainspectorModel )
    def devslainspector(self, *args, **kwargs):
        ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devspokesuminspectorModel )
    def devspokesuminspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.Intention_IFELSE( model = devspokeinspectorModel )
    def devspokeinspector(self, *args, **kwargs):
        ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devspokesumminspectorModel )
    def devspokesumminspector(self, *args, **kwargs):
        ...


    def item_detail_bgp_neighbor_lan_(self, event):
        for index in self.treeview.selection():
            value = self.treeview.item(index, "values")
            appInfo = "Interface: %s, Type: %s, Name: %s, UUid: %s, Event: %s" % value
            self.formal_message("BGP Detail: " + value[2])
            appliance = VTG_vrouter(deviceorg = self.pulldevicenameByTenant.get(), devicename = value[2])
            _, d = appliance.fetch_bgp_neighbor_lan_()
            print(d)


    """
    Cloudviron
    """
    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = cpninspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def cpninspector(self, *args, **kwargs):
        ...


    """
    W.A.N
    """
    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = waninspectorModelaoi, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def waninspectoraoi(self, *args, **kwargs):
        ...


    """
    H.W.ID
    """
    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = hwidnumsinspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def hardwareidnumbers(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = pathmplsinspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def pathmplsinspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = waninspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def waninspector(self, *args, **kwargs):
        ...


    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = interfaceinspectorModel )
    def interfaceinspector(self, *args, **kwargs):
        ...


    """
    L.A.N
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = lanorginspectorModel ) 
    def lanorginspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = lanparseModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def lanparse(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = laninspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def laninspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = aiolaninspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def aiolaninspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = alaninspectorModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def alaninspector(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = alanreliableModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def alanreliable(self, *args, **kwargs):
        ...


    @Softcohesion.seco_str(seco_string_)
    @Softcohesion.INTENT_IFELSE( model = lansuspendsoryModel, condition = (">> Please select <<", "...", ""), filter_message = " Just a little confused about tenant is empty " )
    def lansuspendory(self, *args, **kwargs):
        ...


    """
    deviceSpecificServiceTemplates
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = devsstinspectorModel )
    def devsstinspector(self, *args, **kwargs):
        ... 


    """
    Serial Number
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = snorginspectorModel )
    def snorginspector(self, *args, **kwargs):
        ...


    """
    Path Metrics
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = pathmetricsinspectorModel )
    def pathmetricsinspector(self, *args, **kwargs):
        ...


    """
    Hardware ID Number
    """
    @Softcohesion.secit()
    @Softcohesion.Intention_IFELSE( model = hinorginspectorModel )
    def hinorginspector(self, *args, **kwargs):
        ...


    def item_event(self, event):
        for index in self.treeview.selection():
            value = self.treeview.item(index, "values")
            # 2020.12.8 number,event of alarms
            ala = VTG_alarms()
            noa = ala.number_of_alarms_()
            nes_ = []
            if noa != 0:
                nes_ = ala.event_of_alarms_(value[1])
            appInfo = "Type: %s, Name: %s, UUid: %s, Event: %s" % value
            self.formal_message("Event: " + value[1])
            # 2020.10.29 Type
            if ("branch" == value[0]):
                self.fetchdevicenameByitem_event = value[1]
                print("branch: ", self.fetchdevicenameByitem_event)
                # 2020.10.30 devSpoke
                device = VTG_device(devicename = self.fetchdevicenameByitem_event)
                _, devtemplateName = device.templateName_()
                template = VTG_template(pst = devtemplateName)
                _, devSpoke = template.spoke_()
                print("branchSpoke: ", devSpoke)
            elif ("hub" == value[0]):
                self.fetchhubByitem_event = value[1]
                print("hub: ", self.fetchhubByitem_event)
            print(json.dumps(nes_, indent = 4))


    def item_hardware(self, event):
        for index in self.treeview.selection():
            value = self.treeview.item(index, "values")
            try:
                appInfo = "Type: %s, Name: %s, UUid: %s, Event: %s, Location: %s, Latitude: %s, Longitude: %s" % value
                self.formal_message("Hardware: " + value[1])
                appliance = VTG_appliance(deviceorg = self.pulldevicenameByTenant.get())
                _, d = appliance.hardware_(value[2])
                data = json.loads(d)
                print(json.dumps(data, indent=4))
                return data
            except Exception:
                ...


    def item_brief(self, event):
        for index in event.widget.selection():
            value = self.treeview.item(index, "values")
            try:
                appInfo = "Type: %s, Name: %s, UUid: %s, Event: %s, Location: %s, Latitude: %s, Longitude: %s" % value
                self.formal_message("Status Brief: " + value[1])
                appliance = VTG_appliance(deviceorg = self.pulldevicenameByTenant.get())
                _, d = appliance.status_(value[2])
                dataApp = json.loads(d)
                # 2020.10.29 Type
                if ("branch" == value[0]):
                    self.fetchdevicenameByitem_brief = value[1]
                    self.fetchdeviceuuidByitem_brief = value[2]
                    print("branch: ", self.fetchdevicenameByitem_brief)
                    print("branch@ ", self.fetchdeviceuuidByitem_brief)
                    # 2020.10.30 devSpoke
                    _, devtemplateName = VTG_device(devicename = self.fetchdevicenameByitem_brief).templateName_()
                    _, devSpoke = VTG_template(pst = devtemplateName).spoke_()
                    print("branchSpoke: ", devSpoke)
                    self.vnilantar()
                    # 2022.3.15 Alarm ( Brief, Ipsec, Interface )
                    # Brief
                    _, dBr = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).briefStatisticsAlarms_(self.fetchdeviceuuidByitem_brief)
                    print(json.dumps(json.loads(dBr), indent = 4))
                    # IpsecTunnel_
                    _, dIpsec = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).detailStatisticsAlarms_IpsecTunnel_(self.fetchdeviceuuidByitem_brief)
                    print(json.dumps(json.loads(dIpsec), indent = 4))
                    # Interface
                    _, dIntf = VTG_interface(devicename = self.fetchdevicenameByitem_event, deviceorg = self.pulldevicenameByTenant.get()).detailStatisticsAlarms_Interface_(self.fetchdeviceuuidByitem_brief)
                    print(json.dumps(json.loads(dIntf), indent = 4))
                elif ("hub" == value[0]):
                    self.fetchhubByitem_brief = value[1]
                    print("hub: ", self.fetchhubByitem_brief)
                # print(json.dumps(dataApp, indent = 4))
                tkinter.messagebox.showinfo("Item Brief", json.dumps(dataApp['versanms.ApplianceStatus']['sync-status'] + " & " + dataApp['versanms.ApplianceStatus']['services-status'], indent = 4))
            except Exception as e:
                ... # print(e)


    @Softcohesion.secit()
    def applianceLocation(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        # 2021.1.14
        deviceOrg = self.pulldevicenameByTenant.get()
        if ">> Please select <<" != deviceOrg:
            appliance = VTG_appliance(deviceorg = deviceOrg)
            t_ = appliance.types_
            n_ = appliance.names_
            uuid_ = appliance.uuids_
            loc_ = appliance.locationids_
            lati_ = appliance.latitudes_
            longi_ = appliance.longitudes_
            try:
                # al_ = [ VTG_alarms().detail_of_alarms_.count(n) for n in n_ ]
                # tNUuidAl_ = zip(t_, n_, uuid_, al_, loc_, lati_, longi_)
                tNUuidAl_ = zip(t_, n_, uuid_, t_, loc_, lati_, longi_)
            except TypeError as e:
                print(f" - Please wait unitl branch appliance and uuid created successfully. \n {e}")
            else:
                for item in sorted(tNUuidAl_):
                    typeName_tup = tuple(item)
                    rowIt = self.treeview.insert(parent = "", index = tkinter.END, values = typeName_tup, tags = typeName_tup[2])
                    # self.treeview.tag_configure(typeName_tup[2], background = "#ffffff")
                    # self.treeview.tag_configure(typeName_tup[2], background = "lightblue")
                    # assert typeName_tup[0] == "['branch']"
                    if typeName_tup[0] == ['branch']:
                        self.treeview.tag_bind(typeName_tup[2], sequence = '<Double-Button-3>', callback = self.pop_handle)
                    ## loc_rowIt = self.treeview.insert(parent = rowIt, index = tkinter.END, values = typeName_tup[4])
                    ## self.treeview.insert(parent = loc_rowIt, index = tkinter.END, values = ("Latitude: " + str(typeName_tup[5])) )
                    ## self.treeview.insert(parent = loc_rowIt, index = tkinter.END, values = ("Longitude: " + str(typeName_tup[6])) )
                    # print(self.treeview.tag_configure(typeName_tup[2]))
                '''
                for item in self.treeview.get_children():
                    print(self.treeview.item(item, "values"))
                '''
        else:
            self.formal_message(" Select the tenant priorly, please. ")
        IntfTar, Intf = " " * 80, " " * 80
        for i in range(300, 307):
            Label(self.__root, text = IntfTar).grid(row = i, column = 0)
            Label(self.__root, text = Intf).grid(row = i, column = 1)


    def orgValue(self, event):
        # self.orgContent.set("Organization: %s" % self.org_combobox.get())
        self.pulldevicenameByTenant.set(self.org_combobox.get())
        self.applianceLocation()


    def organizations(self):
        """ http://patorjk.com/software/taag/#p=display&h=3&f=Graffiti&t=StatusField """
        print()
        print(r'  _________ __          __              __________.__       .__      .___')
        print(r' /   ______/  |______ _/  |_ __ __ _____\_   _____|__| ____ |  |   __| _/')
        print(r' \_____  \\   __\__  \\   __|  |  /  ___/|    __) |  _/ __ \|  |  / __ | ')
        print(r' /        \|  |  / __ \|  | |  |  \___ \ |     \  |  \  ___/|  |_/ /_/ | ')
        print(r'/_______  /|__| (____  |__| |____/____  >\___  /  |__|\___  |____\____ | ')
        print(r'        \/           \/               \/     \/           \/          \/ ')
        print()
        '''
        # 2023.3.4
        oau = VTG_oauth()
        _, oauth_bearer_ = oau.oauth_bearer_
        data = json.loads(oauth_bearer_)
        # print(json.dumps(data, indent = 4))
        print(data['access_token'])
        '''
        # 2021.1.14
        tenantname = "shct"
        # 2021.5.11
        org = VTG_org(devicename = "0.0.0.0", deviceorg = tenantname)
        # _, d = org.tenantallchildren(data['access_token'])
        _, d = org.tenantallchildren_
        data = json.loads(d)
        if isinstance(data.get('List').get('value'), list):
            orgName_ = [ org for org in data.get('List').get('value') ]
        else:
            orgName_ = []
            orgName_.append(data.get('List').get('value'))
        orgName_.append('>> Please select <<')
        # print(orgName_)
        self.orgName_tuple = tuple(sorted(orgName_))
        license = VTG_system(devicename = "vD")
        license.license_count_
        license.license_status_
        license.license_cookie_
        license.headEnd_status_
        '''
        # curl -i -k 'https://:9183/vnms/dashboard/tenant/shct/allchildren' -X GET -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization:Bearer <>"
        '''


    def formal_message(self, msg):
        result = tkinter.messagebox.askokcancel(title = 'message', message = msg)
        return result


    def tag_reverse(self, event):
        """ Triggered when the mouse enters the component 2023.3.14 """
        widget_location = self.__root.winfo_children().index(event.widget)
        widget_location_list = [ i for i in range(widget_location - 2, widget_location + 3) ]

        print('widget: Treeview %s %s ' % (widget_location, widget_location_list))
        # print('widget: Treeview %s %s ' % (event.widget.cget('tagname'), widget_location_list))


    def fixed_map(self, option):
        return [elm for elm in self.style.map("Treeview", query_opt = option) if elm[:2] != ("!disabled", "!selected") ]


# Aha, there's no more content after this line.
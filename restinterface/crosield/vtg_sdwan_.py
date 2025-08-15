#!/usr/bin/python
#coding: UTF-8
from .cfue_shct_ import *
from .aoicfu_ import *


def process_bar(value, bar):
    print("\r[%d%% %s] %s\n" % ( 100-value, ''.rjust(value, bar) , "100%"))


def string_process_bar(value, bar):
    return (str(" %d%%%s %s ") % ( 100-value, ''.ljust(value, bar) , ""))


class VTG_sdwan:

    __slots__ = ( '__slaPathMetrics',
                  '__forwardingConfig',
                  '__json_d_circuit_plrs',
                  '__forwardingconfig_rule',
                  '__forwardingconfig_fp',
                  '__ruleName',
                  '__policyName',
                  '__forwardingProfileName',
                  '__deviceName',
                  '__orgName',
    )

    def __init__(self, *args, **kwargs):
        self.__orgName = kwargs['deviceorg']
        self.__deviceName = kwargs['devicename']
        self.__forwardingProfileName = "forwardingProfileName"
        self.__policyName = "policyName"
        self.__ruleName = "ruleName"
        self.__forwardingconfig_fp = "forwardingconfig_fp"
        self.__forwardingconfig_rule = "forwardingconfig_rule"
        self.__json_d_circuit_plrs = "json_d_circuit_plrs"
        self.__forwardingConfig = {"forwarding-config": {"forwarding-profiles": {"forwarding-profile": "fpcontent"}, "Default-Policy": {"rule": "rulecontent"} } }
        self.__slaPathMetrics = []


    async def devsla_path_metrics_aggregated_last_10s_brief_prime_spokegrouphub_(self, spokegrouphub):
        string_item_last_stats = ""
        # 2023.5.11 spokegrouphub
        ri_sdwan_slapathmetrics_fetchall_urlpath = '/api/operational/devices/device/{}/live-status/orgs/org/{}/sd-wan/sla-monitor/metrics/last-10s/{}/last-stats'.format(self.__deviceName, self.__orgName, spokegrouphub)
        sessicfueget = Aoicfu(ri_sdwan_slapathmetrics_fetchall_urlpath, json.dumps(0), 'fetches')
        data, rc = await sessicfueget.action_restinterface_()
        if (400 == rc):
            print("Data Unavailable : Tunnel Yield + ", self.__deviceName)
            # print("Data Unavailable : devsla_path_metrics_aggregated_last_10s_brief_prime_", self.__deviceName)
        else:
            # 2021.5.11 except
            try:
                for item_last_stats in data["last-stats"]:
                    tubevisi = int(float(item_last_stats['pdu-loss-ratio']))  # float() ver21
                    ## print(self.__deviceName, spokegrouphub, item_last_stats["local-wan-link"])
                    # 2024.2.15
                    string_item_last_stats += item_last_stats["local-wan-link"] + '!' + str(100 - tubevisi) + '!' if (0 != tubevisi) else '-' + item_last_stats["local-wan-link"] + '-'
                    # string_item_last_stats += item_last_stats["local-wan-link"] + '!' + str(100 - tubevisi) + '!'  if (0 != tubevisi) else item_last_stats["local-wan-link"] + "$=$"
            except Exception as e:
                if "Expecting value: line 1 column 1 (char 0)" == str(e):
                    print(f" - {self.__deviceName} might be unreachable. ")
                    print()
                else:
                    print(" - Tunnel Yield + : %s got Error: \"%s\" " % (self.__deviceName, e) )
                    # print("devsla_path_metrics_aggregated_last_10s_brief_prime_ : %s got Error: \"%s\" " % (self.__deviceName, e) )
        return str(string_item_last_stats)


    async def devsla_path_metrics_aggregated_last_1m_brief_prime_spokegrouphub_(self, spokegrouphub):
        string_item_last_stats = ""
        # 2023.5.11 spokegrouphub
        ri_sdwan_slapathmetrics_fetchall_urlpath = '/api/operational/devices/device/{}/live-status/orgs/org/{}/sd-wan/sla-monitor/metrics/last-1m/{}/last-stats'.format(self.__deviceName, self.__orgName, spokegrouphub)
        sessicfueget = Aoicfu(ri_sdwan_slapathmetrics_fetchall_urlpath, json.dumps(0), 'fetches')
        data, rc = await sessicfueget.action_restinterface_()
        if (400 == rc):
            print("Data Unavailable : Tunnel Yield ", self.__deviceName)
            # print("Data Unavailable : devsla_path_metrics_aggregated_last_1m_brief_prime_", self.__deviceName)
        else:
            # 2021.5.11 except
            try:
                for item_last_stats in data["last-stats"]:
                    tubevisi = int(float(item_last_stats['pdu-loss-ratio']))  # float() ver21
                    ## print(self.__deviceName, spokegrouphub, item_last_stats["local-wan-link"])
                    if (0 != tubevisi):
                        string_item_last_stats += item_last_stats["local-wan-link"] + '(' + str(100-tubevisi) + "+)" 
                        # print(self.__deviceName, spokegrouphub, item_last_stats["local-wan-link"])
                    else:
                        string_item_last_stats += item_last_stats["local-wan-link"] + "(-)"
                        # print(self.__deviceName, spokegrouphub, item_last_stats["local-wan-link"])
            except Exception as e:
                if "Expecting value: line 1 column 1 (char 0)" == str(e):
                    print(f" - {self.__deviceName} might be unreachable. ")
                    print()
                else:
                    print(" - Tunnel Yield : %s got Error: \"%s\" " % (self.__deviceName, e) )
                    # print("devsla_path_metrics_aggregated_last_1m_brief_prime_ : %s got Error: \"%s\" " % (self.__deviceName, e) )
        return str(string_item_last_stats)


    def devsla_path_metrics_aggregated_last_1m_brief_prime_(self, spokegrouphubs):
        for item in spokegrouphubs:
            string_item_last_stats = ""
            # print(self.__deviceName, item)
            # 2020.12.21 intfer
            d, rc = self.sla_path_metrics_aggregated_last_1m_detail_intfer_(item)
            # 2020.11.29 Metrics_NoData
            if (400 == rc):
                print("Data Unavailable : devsla_path_metrics_aggregated_last_1m_brief_prime_", self.__deviceName)
            else:
                # 2021.5.11 except
                try:
                    data = json.loads(d)
                    for item_last_stats in data["last-stats"]:
                        tubevisi = int(float(item_last_stats['pdu-loss-ratio']))  # float() ver21
                        print(self.__deviceName, item, item_last_stats["local-wan-link"])
                        if (0 != tubevisi):
                            string_item_last_stats += item_last_stats["local-wan-link"] + str(100-tubevisi) + "+" 
                            # print(self.__deviceName, item, item_last_stats["local-wan-link"])
                        else:
                            string_item_last_stats += item_last_stats["local-wan-link"] + "-"
                            # print(self.__deviceName, item, item_last_stats["local-wan-link"])
                except Exception as e:
                    if "Expecting value: line 1 column 1 (char 0)" == str(e):
                        print(self.__deviceName + " may be unreachable. ")
                        print()
                    else:
                        print("devsla_path_metrics_aggregated_last_1m_brief_prime_ : %s got Error: \"%s\" " % (self.__deviceName, e) )
            return str(string_item_last_stats)


    def devsla_path_metrics_aggregated_last_1m_brief_(self, spokegrouphubs):
        for item in spokegrouphubs:
            # 2020.12.21 intfer
            d, rc = self.sla_path_metrics_aggregated_last_1m_detail_intfer_(item)
            # 2020.11.29 Metrics_NoData
            if (400 == rc):
                print("Data Unavailable : devsla_path_metrics_aggregated_last_1m_brief_", self.__deviceName)
            else:
                # 2021.5.11 except
                try:
                    data = json.loads(d)
                    for item_last_stats in data["last-stats"]:
                        tubevisi = int(float(item_last_stats['pdu-loss-ratio'])) # float() ver21
                        print(self.__deviceName, item, item_last_stats["local-wan-link"])
                        process_bar(tubevisi, '+')
                except Exception as e:
                    if "Expecting value: line 1 column 1 (char 0)" == str(e):
                        print(self.__deviceName + " may be unreachable. ")
                        print()
                    else:
                        print("devsla_path_metrics_aggregated_last_1m_brief_ : %s got Error: \"%s\" " % (self.__deviceName, e) )


    def devsla_path_metrics_aggregated_last_1m_detail_(self, spokegrouphubs):
        for item in spokegrouphubs:
            print("site-name: ", item)
            # 2020.12.21 intfer
            d, rc = self.sla_path_metrics_aggregated_last_1m_detail_intfer_(item)
            # 2020.11.29 Metrics_NoData
            if (400 == rc):
                print("Data Unavailable : devsla_path_metrics_aggregated_last_1m_detail_", self.__deviceName)
            else:
                data = json.loads(d)
                for item in data["last-stats"]:
                    print(json.dumps(item, indent = 4))
                print()


    def sla_path_metrics_aggregated_last_1m_detail_(self):
        for item in self.__slaPathMetrics:
            if "controller" not in item:
                print("site-name: ", item)
                # 2020.12.21 intfer
                d, rc = self.sla_path_metrics_aggregated_last_1m_detail_intfer_(item)
                data = json.loads(d)
                for item in data["last-stats"]:
                    '''
                    item.pop("path-handle")
                    item.pop("fwd-class")
                    item.pop("local-wan-link")
                    item.pop("remote-wan-link")
                    item.pop("local-wan-link-id")
                    item.pop("remote-wan-link-id")
                    item.pop("fwd-delay-var")
                    item.pop("rev-delay-var")
                    item.pop("fwd-loss-ratio")
                    item.pop("rev-loss-ratio")
                    item.pop("fwd-loss")
                    item.pop("rev-loss")
                    '''
                    print(json.dumps(item, indent = 4))


    def sla_path_metrics_aggregated_last_1m_detail_intfer_(self, item):
        # 2020.12.21 intfer
        ri_sdwan_slapathmetrics_fetchall_urlpath = '/api/operational/devices/device/{}/live-status/orgs/org/{}/sd-wan/sla-monitor/metrics/last-1m/{}/last-stats'.format(self.__deviceName, self.__orgName, item)
        d, rc = Restinterface(ri_sdwan_slapathmetrics_fetchall_urlpath, 0, 'get').action_restinterface_()
        return d, rc


    def sla_path_metrics_aggregated_last_1m_(self):
        ri_sdwan_slapathmetrics_objects_urlpath = '/api/operational/devices/device/{}/live-status/orgs/org/{}/sd-wan/sla-monitor/metrics/last-1m/'.format(self.__deviceName, self.__orgName)
        d, rc = Restinterface(ri_sdwan_slapathmetrics_objects_urlpath, 0, 'get').action_restinterface_()
        data = json.loads(d)
        # print(data)
        print("sla_path_metrics_: ", rn)
        # print("sla_path_metrics_: ", d)
        self.__slaPathMetrics = [ item["site-name"] for item in data['last-1m'] ]
        return rc, self.__slaPathMetrics


    def forwardingProfile_(self):
        ri_sdwan_forwardingProfile_objects_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/forwarding-profiles'.format(self.__deviceName, self.__orgName)
        d, rc = Restinterface(ri_sdwan_forwardingProfile_objects_urlpath, 0, 'get').action_restinterface_()
        print("forwardingProfile_: ", rc)
        print("forwardingProfile_: ", d)
        return rc, d


    def forwardingProfile_some_(self):
        ...


    def priority_(self, forwardingProfileName):
        self.__forwardingProfileName = forwardingProfileName
        ri_sdwan_forwardingProfile_priority_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/forwarding-profiles/forwarding-profile/{}/circuit-priorities/priority'.format(self.__deviceName, self.__orgName, self.__forwardingProfileName)
        d, rc = Restinterface(ri_sdwan_forwardingProfile_priority_urlpath, 0, 'get').action_restinterface_()
        print("priority_: ", rc)
        print("priority_: ", d)
        return rc, d


    def rule_(self, policyName):
        self.__policyName = policyName
        ri_sdwan_policies_defaultPolicy_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/policies/sdwan-policy-group/{}/rules/rule/'.format(self.__deviceName, self.__orgName, self.__policyName)
        d, rc = Restinterface(ri_sdwan_policies_defaultPolicy_urlpath, 0, 'get').action_restinterface_()
        print("rule_: ", rc)
        print("rule_: ", d)
        return rc, d


    def create_forwardingProfile_(self, forwardingconfig):
        self.__forwardingconfig_fp = forwardingconfig["forwarding-config"]["forwarding-profiles"]
        ri_sdwan_forwardingProfile_objects_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/forwarding-profiles'.format(self.__deviceName, self.__orgName)
        d, rc = Restinterface(ri_sdwan_forwardingProfile_objects_urlpath, json.dumps(self.__forwardingconfig_fp), 'post').action_restinterface_()
        print("create_forwardingProfile: ", rc)
        print("create_forwardingProfile: ", d)
        return rc, d


    def create_rule_(self, policyName, forwardingconfig):
        self.__policyName = policyName
        self.__forwardingconfig_rule = forwardingconfig["forwarding-config"][self.__policyName]
        ri_sdwan_policies_defaultPolicy_rule_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/policies/sdwan-policy-group/{}/rules/'.format(self.__deviceName, self.__orgName, self.__policyName)
        d, rc = Restinterface(ri_sdwan_policies_defaultPolicy_rule_urlpath, json.dumps(self.__forwardingconfig_rule), 'post').action_restinterface_()
        print("create_rule_: ", rc)
        print("create_rule_: ", d)
        return rc, d


    def erase_rule_defaultfp_(self, policyName):
        self.__policyName = policyName
        ri_sdwan_policies_defaultPolicy_rule_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/orgs/org-services/' + self.__orgName + '/sd-wan/policies/sdwan-policy-group/' + self.__policyName + '/rules/rule/Default-FP/'
        d, rc = Restinterface(ri_sdwan_policies_defaultPolicy_rule_urlpath, 0, 'delete').action_restinterface_()
        print("erase_rule_defaultfp_: ", rc)
        print("erase_rule_defaultfp_: ", d)
        return rc, d


    def erase_rule_some_(self, policyName, ruleName):
        self.__policyName = policyName
        self.__ruleName = ruleName
        ri_sdwan_policies_defaultPolicy_rule_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/orgs/org-services/' + self.__orgName + '/sd-wan/policies/sdwan-policy-group/' + self.__policyName + '/rules/rule/' + self.__ruleName + '/'
        d, rc = Restinterface(ri_sdwan_policies_defaultPolicy_rule_urlpath, 0, 'delete').action_restinterface_()
        print("erase_rule_some_: ", rc)
        print("erase_rule_some_: ", d)
        return rc, d


    def factorydefault_forwardingProfile_defaultfp_(self):
        data = json.dumps({"forwarding-profile": {"name": "Default-FP"
            ,"circuit-priorities": {"avoid": {}}
            ,"replication": {}
            ,"fec": {"sender": {}}
        }})
        ri_sdwan_forwardingProfile_defaultFP_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/forwarding-profiles/forwarding-profile/Default-FP/'.format(self.__deviceName, self.__orgName)
        d, rc = Restinterface(ri_sdwan_forwardingProfile_defaultFP_urlpath, data, 'put').action_restinterface_()
        print("factorydefault_defaultfp_: ", rc)
        print("factorydefault_defaultfp_: ", d)
        return rc, d


    def erase_forwardingProfile_some_(self, forwardingProfileName):
        self.__forwardingProfileName = forwardingProfileName
        ri_sdwan_forwardingProfile_some_urlpath = '/api/config/devices/device/' + self.__deviceName + '/config/orgs/org-services/' + self.__orgName + '/sd-wan/forwarding-profiles/forwarding-profile/' + self.__forwardingProfileName + '/'
        d, rc = Restinterface(ri_sdwan_forwardingProfile_some_urlpath, 0, 'delete').action_restinterface_()
        print("factorydefault_some_: ", rc)
        print("factorydefault_some_: ", d)
        return rc, d


    def services_(self):
        ...


    def update_forwardingProfile_defaultFP_(self, forwardingconfig, D_CIRCUIT_P_L_R):
        self.__forwardingConfig = forwardingconfig
        self.__forwardingconfig_fp = forwardingconfig["forwarding-config"]["forwarding-profiles"]
        d_circuit_p_l_r = D_CIRCUIT_P_L_R.split(",")
        d_circuit_plr_alpha = [ "{\"value\":" + str(d_plr.split(':')[0]) + ",\"circuit-names\":{\"local\":[\"" + str(d_plr.split(':')[1]) + "\"],\"remote\": [\"" + str(d_plr.split(':')[2]) + "\"]}}" for d_plr in d_circuit_p_l_r]
        json_d_circuit_plrs = [ json.loads(jdc) for jdc in d_circuit_plr_alpha ]
        self.__json_d_circuit_plrs = json_d_circuit_plrs
        self.__forwardingConfig['forwarding-config']['forwarding-profiles']["forwarding-profile"]["circuit-priorities"]["priority"] = self.__json_d_circuit_plrs
        ri_sdwan_forwardingProfile_defaultFP_urlpath = '/api/config/devices/device/{}/config/orgs/org-services/{}/sd-wan/forwarding-profiles/forwarding-profile/Default-FP/'.format(self.__deviceName, self.__orgName)
        d, rc = Restinterface(ri_sdwan_forwardingProfile_defaultFP_urlpath,  json.dumps(self.__forwardingconfig_fp), 'put').action_restinterface_()
        print("update_forwardingProfile_defaultFP_: ", rc)
        print("update_forwardingProfile_defaultFP_: ", d)
        return rc, d
#!/usr/bin/python
#coding: UTF-8
from .cfue_shct_ import *


class VTG_template:
    __slots__ = ( '__spokeGroup', '__poststagingtemplate' )

    def __init__(self, *args, **kwargs):
        self.__poststagingtemplate = kwargs['pst']
        self.__spokeGroup = ""


    def spoke_(self):
        ri_templatespoke_fetch_urlpath = '/vnms/sdwan/workflow/templates/template/{}'.format(self.__poststagingtemplate)
        d, rc = Restinterface(ri_templatespoke_fetch_urlpath, 0, 'get').action_restinterface_()
        data = json.loads(d)
        # print(json.dumps(data, indent = 4))
        # 2020.11.4 setdefault spokeGroup
        if (data["versanms.sdwan-template-workflow"].get('spokeGroup',None) is None):
            return rc, None
        else:
            return rc, str(data["versanms.sdwan-template-workflow"]["spokeGroup"])


    def commit_(self, dev):
        device = dev
        data = json.dumps({
	    "versanms.devices": {
                "device-list": [ device ]
	}})
        #/vnms/template/applyTemplate/IT-ShenZhen-CPE-01/devices?reboot=false&mode=overwrite
        ri_template_commit_urlpath = '/vnms/template/applyTemplate/{}/devices?reboot=false&mode=overwrite'.format(self.__poststagingtemplate)
        d, rc = Restinterface(ri_template_commit_urlpath, data, 'post').action_restinterface_()
        data = json.loads(d)
        return rc, str(data["versanms.templateResponse"]["taskId"])


    def deploy_(self):
        #/vnms/sdwan/workflow/templates/template/deploy/IT-ShenZhen-CPE-01
        ri_template_deploy_urlpath = '/vnms/sdwan/workflow/templates/template/deploy/{}'.format(self.__poststagingtemplate)
        d, rc = Restinterface(ri_template_deploy_urlpath, 0, 'post').action_restinterface_()
        print(rc)
        return rc, d


    def update_(self, spokegroup):
        rn, tar = self.update_spokegroup_(spokegroup)
        #/vnms/sdwan/workflow/templates/template/IT-ShenZhen-CPE-01
        ri_template_pushconfig_urlpath = '/vnms/sdwan/workflow/templates/template/{}'.format(self.__poststagingtemplate)
        d, rc = Restinterface(ri_template_pushconfig_urlpath, json.dumps(tar), 'put').action_restinterface_()
        print(rc)
        return rc, d


    def update_spokegroup_(self, spokegroup):
        self.__spokeGroup = spokegroup
        rc, src = self.fetch_()
        data = json.loads(src)
        print("- Stationed: ", data["versanms.sdwan-template-workflow"]['spokeGroup'])
        print("- Target At: ", self.__spokeGroup)
        tar = data
        tar["versanms.sdwan-template-workflow"]['spokeGroup'] = self.__spokeGroup
        return rc, tar


    def fetch_(self):
        ri_template_fetch_urlpath = '/vnms/sdwan/workflow/templates/template/{}'.format(self.__poststagingtemplate)
        d, rc = Restinterface(ri_template_fetch_urlpath, 0, 'get').action_restinterface_()
        print(rc)
        return rc, d
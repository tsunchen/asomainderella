#!/usr/bin/python
#coding: UTF-8
from .vtg_device_ import *
import yaml
from .result_module_ import Ok, Err, Result


def connect_rest_interface(decokwargs) -> Result[dict, str]:
    # 2025.5.7 Using Result Module
    try:
        status_, rc = Restinterface(decokwargs['model'], 0, decokwargs['condition']).action_restinterface_()
        data = json.loads(status_)
        return Ok(data)
    except json.JSONDecodeError:
        return Err("JSONDecodeError: Invalid JSON response. Check Username and Password.")
    except Exception as e:
        return Err(f"Unexpected error: {str(e)}")


# class attr : model
# cfue : condition
def INTENT_RESTZ(*decoargs, **decokwargs):
    """
    INTENT_RESTZ - A robust decorator for REST API interactions using Result module.
    """
    def wrapper(model):
        def inner_wrapper(self, *args, **kwargs):
            result = connect_rest_interface(decokwargs)

            print(result)

            if result.is_err():
                print(f"-- Error: {result.unwrap_err()}")
                return

            data = result.unwrap()
            print(f"-- LICENSE_{decokwargs['djson']}: {decokwargs.get('condition')}")

            if decokwargs['djson'] == 'status':
                print(data)
            elif decokwargs['djson'] == 'LicenseCountContainer':
                print(data)
            elif decokwargs['djson'] == 'headEndstatus':
                print(yaml.dump(data))
            else:
                print("-- No specific handler for this djson value.")

        return inner_wrapper

    return wrapper


class VTG_system(object):
    __slots__ = ( '__ri_others_system_configuration_vnf_manager_urlpath_', '__deviceName' )
    """
    2021.8.16 indent_rest classattr: model
    2021.8.15 f_string, property
    2021.4.30
    """
    __ri_others_system_configuration_license_count_urlpath_  = f"/vnms/license/licenseCount?deep=true"
    __ri_others_system_configuration_license_status_urlpath_ = f"/api/config/system/_operations/trial-info?deep=true"
    __ri_vd_monitor_management_urlpath_ = f"/vnms/dashboard/status/headEnds"


    def __init__(self, *args, **kwargs):
        self.__deviceName = kwargs['devicename']
        self.__ri_others_system_configuration_vnf_manager_urlpath_ = f"/api/config/devices/device/{self.__deviceName}/config/system/vnf-manager"


    @property
    @INTENT_RESTZ( model = __ri_vd_monitor_management_urlpath_, condition = 'get', djson = 'headEndstatus' )
    def headEnd_status_(self):
        ...

    @property
    @INTENT_RESTZ( model = f"/sdwan", condition = 'got', djson = 'cookie' )
    def license_cookie_(self):
        ...

    @property
    @INTENT_RESTZ( model = __ri_others_system_configuration_license_status_urlpath_, condition = 'post', djson = 'status' )
    def license_status_(self):
        ...

    @property
    @INTENT_RESTZ( model = __ri_others_system_configuration_license_count_urlpath_, condition = 'get', djson = 'LicenseCountContainer' )
    def license_count_(self):
        ...

    async def lIcense_status_(self):
        """ /api/config/system/_operations/trial-info?deep=true """
        lIcense_status_, rc = await Restinterface(__ri_others_system_configuration_license_status_urlpath_, 0, 'post').action_restinterface_()
        # print("license_status_: ", rc)
        # print("license_status_: ", d)
        print('{}'.format(lIcense_status_['output']['status']))

    async def lIcense_count_(self):
        """ /vnms/license/licenseCount?deep=true """
        lIcense_count_, rc = await Restinterface(__ri_others_system_configuration_license_count_urlpath_, 0, 'get').action_restinterface_()
        # print("license_count_: ", rc)
        print("license_count_: ", lIcense_count_)

    @property
    def vnf_manager_(self):
        """ /api/config/devices/device/<appliance-name>/config/system/vnf-manager """        
        systemvnfmanager_, rc = Restinterface(self.__ri_others_system_configuration_vnf_manager_urlpath_, 0, 'get').action_restinterface_()
        print("systemvnfmanager_: ", rc)
        # print("systemvnfmanager_: ", d)
        return rc, systemvnfmanager_
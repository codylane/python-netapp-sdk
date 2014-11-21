#!/usr/bin/env python

from NaServer import *
from NaElement import *
import xmltodict
import time

def usage():
    print('USAGE: %s <netapp hostname> <username> <password>' %(sys.argv[0]))
    sys.exit(0)

def _invoke_api(conn, *args):
    api = NaElement(*args)
    call = conn.invoke_elem(api)
    if call.results_errno() != 0:
        raise IOError('Failed api call=%s, errno=%s, desc=%s'
            %(args, call.results_errno(), call.sprintf())
        )
    return call

def connect(hostname, user, password, minor_version=1, major_version=21):
    global conn
    conn = NaServer(hostname, minor_version, major_version)
    conn.set_server_type('filer')
    conn.set_transport_type('HTTPS')
    conn.set_port(443)
    conn.set_style('LOGIN')
    conn.set_admin_user(user, password)
    return conn

if __name__ == '__main__':
    if len(sys.argv[1:]) != 3:
        usage()

    netapp_hostname = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    conn = connect(netapp_hostname, username, password)

    system_api_list = _invoke_api(conn, 'system-api-list')

    api_xml = system_api_list.sprintf()

    hash = xmltodict.parse(api_xml)

    api_list = hash.get('results').get('apis').get('system-api-info')

    ws_indent = ' '*4

    header = '''############################################################################
# This module was auto-generated on %s
# by using the 'system-api-list' api call from NetApp SDK for python.  
# If you make changes to this module it will likely be broken the next time
# this file is auto-generated.  If you choose to update this file anyway,
# please ensure that you have also updated the generate-api.py script
# to include your new changes.
#
# Also worth mentioning that some of the api calls may not work properly
# and that is because there is no way to easily auto-determine what api
# calls require additional arguments.  If you find one that is broken,
# you may need to manually update this file but that is not recommended.
#
# The goal of this module is to make it easier to develop code since the
# original API requires you to know the exact API calls for interating
# with your NetApp appliance.  The other goal of this module is to ensure
# you can override it instaed of modifying it directly if you find problems.
############################################################################
''' %(time.ctime())
    print(header)
    print('')
    print('import sys')
    print('from NaElement import *')
    print('from NaServer import *')
    print('import xmltodict')
    print('import unicodedata')
    print('')

    print('conn = None')
    print('timeout = 10')
    print('')
    print('def connect(hostname, user, password, minor_version=1, major_version=21):')
    print('%sglobal conn' %(ws_indent))
    print('%sconn = NaServer(hostname, minor_version, major_version)' %(ws_indent))
    print("%sconn.set_server_type('filer')" %(ws_indent))
    print("%sconn.set_transport_type('HTTPS')" %(ws_indent))
    print("%sconn.set_port(443)" %(ws_indent))
    print("%sconn.set_style('LOGIN')" %(ws_indent))
    print("%sconn.set_admin_user(user, password)" %(ws_indent))
    print("%sconn.set_timeout(timeout)" %(ws_indent))
    print("%sreturn conn" %(ws_indent))
    print('')

    for api in api_list:
        api_call = api.get('name')
        api_function = api_call.replace('-','_')

        print('def %s(*args):' %(api_function))
        print("%sapi_call = _invoke_api('%s', *args)" %(ws_indent, api_call))
        print('%sreturn api_call' %(ws_indent))
        print('')

    print('def xml_to_dict(xml):')
    print('%sreturn xmltodict.parse(xml)' %(ws_indent))
    print('')
    print('def normalize_unicode(result):')
    print("%s'''" %(ws_indent))
    print('%sTakes the dictionary @result from xml_to_dict and normalizes the' %(ws_indent))
    print('%sunicode characters.' %(ws_indent))
    print('')
    print('%sReturns a new dictionary with no more unicode characters' %(ws_indent))
    print("%s'''" %(ws_indent))
    print('%sd = {}' %(ws_indent))
    print('%sfor key,value in result.iteritems():' %(ws_indent))
    print('%s%sif isinstance(key, unicode):' %(ws_indent, ws_indent))
    print("%s%s%skey = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore')" %(ws_indent, ws_indent, ws_indent))
    print('%s%sif isinstance(value, unicode):' %(ws_indent, ws_indent))
    print("%s%s%svalue = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')" %(ws_indent, ws_indent, ws_indent))
    print('%s%sd[key] = value' %(ws_indent, ws_indent))
    print('%sreturn d' %(ws_indent))
    print('')
    print('def _invoke_api(*args):')
    print('%sapi = NaElement(*args)' %(ws_indent))
    print('%scall = conn.invoke_elem(api)' %(ws_indent))
    print('%sif call.results_errno() != 0:' %(ws_indent))
    print("%s%sraise IOError('Failed api call=%%s, errno=%%s, desc=%%s'" %(ws_indent, ws_indent))
    print("%s%s%s%%(args, call.results_errno(), call.sprintf())" %(ws_indent, ws_indent, ws_indent))
    print("%s%s)" %(ws_indent, ws_indent))
    print("%sreturn call" %(ws_indent))

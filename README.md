python NetApp SDK
=================
This site helps you create a small python module for interacting with your NetApp appliance.  

Pre-Conditions
==============
Because the NetAPP SDK is a licensed product, I'm not able to provide the SDK here.  Instead you will need to download the NetApp Manageability SDK from support.netapp.com and uzip it to your location of choice.  Once you have the Netapp Manageability SDK downloaded and uzipped you also need to remember the path to where you unzipped this archive.  You will need to setup `PYTHONPATH` environment to the location of your unzipped archive later. 

* You must also ensure that the username passed to this script is part of the
  `admin` group in your Netapp console. Otherwise you will
 get permission denied errors.

WARNING
=======
This generation code isn't perfect since the NetApp SDK requires knowledge of use of each API call.  I tried to do my best to remedy this but testing all the functionality is difficult and destructive.  Please do let me know if api call you are trying to use (in the generated script) doesn't work and I'll do my best to help out.   The use of the zedi tool can help diagnose the problems from the generated code.  Please sumbit pull requests if you find problems.  I appreciate feedback positive or negative.  

FUTURE
======
I would love to have a full test suite from the generated code to ensure that it works as designed but without having a non-production instance I found it to troublesome.  If you have ideas on how to help make this better or some API calls in the generated code don't work please submit a pull request.  Let's make this better for everyone!

NOTES
=====
This was tested against SDK version `netapp-manageability-sdk-5.3`

Auto-Generating the Base API
============================
* First ensure that you have set you `PYTHONPATH` environment variable to the location where you unpacked the archive.
```
export PYTHONPATH=~/netapp-manageability-sdk-5.3/lib/python/NetApp:$PYTHONPATH
```
* Next cd into the directory to where you have cloned this repository
```
cd ~/prj/python-netapp-sdk
pip install -r requirements.txt
./generate-api.py mynetapp.host.com adminuser adminuser_password >
netapp_utils.py
```

Running the command above will generate all the code to standard out so you name the generated module anything you want.  I chose to name it `netapp_utils.py` in the example above.

USAGE
=====
Once you have the generated module, you can import it as follows for testing in the python interpreter or Ipython.  I prefer Ipython for quick tasks.  It's best left as an example:

This example will show you how to obtain lun stats for everyone LUN on your filer.

```
$ ipython
In [1]: from netapp_utils import *
In [2]: from netapp_utils import _xml_to_dict
In [3]: conn = connect('mynetapp.fqdn', 'adminuser', 'adminpass')
In [4]: lun_stats = lun_stats_list_info()
In [5]: lun_stats
Out[6]: <NaElement.NaElement instance at 0x10f60f878>
In [7]: xml = lun_stats.sprintf()
In [8]: lun_stats_dict = _xml_to_dict(xml)
In [9]: lun_stats_list = lun_stats_dict.get('results').get('lun-stats').get('lun-stats-info')
In [10]: type(lun_stats_list)
Out[10]: list
In [17]: for lun_stat in lun_stats_list:
   ....:     print(lun_stat)
   ....:     
{u'last-zeroed': u'17741072', u'block-size': u'512', u'write-ops': u'4929906238', u'write-blocks': u'102752775069', u'other-ops': u'3858547', u'path': u'/vol/volume01/lun01', u'read-blocks': u'61399577045', u'read-ops': u'701187624'}
{u'last-zeroed': u'17741072', u'block-size': u'512', u'write-ops': u'3589121881', u'write-blocks': u'62376738778', u'other-ops': u'2856613', u'path': u'/vol/volume02/lun02', u'read-blocks': u'8809654074', u'read-ops': u'210613066'}
{u'last-zeroed': u'17741072', u'block-size': u'512', u'write-ops': u'936983634', u'write-blocks': u'23812208448', u'other-ops': u'3130975', u'path': u'/vol/volume03/lun03', u'read-blocks': u'7215877586', u'read-ops': u'172634525'}
```

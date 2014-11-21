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


NOTE: I used variables with _ before them in this example, to not
pollute the API calls since we imported with a *.  I wouldn't do this
in production code, but for this example it will work nicely.
```
cat > test.py << EOF
#!/usr/bin/env python

from netapp_utils2 import *
from netapp_utils2 import normalize_unicode

conn = connect('mynetapp.fqdn', 'adminuser', 'adminpass')

_lun_stats_call = lun_stats_list_info()

_xml = _lun_stats_call.sprintf()

_lun_stats_dict = xml_to_dict(_xml)

_lun_stats_list = _lun_stats_dict.get('results').get('lun-stats').get('lun-stats-info')
for _lun in _lun_stats_list:
    _no_unicode_dict = normalize_unicode(_lun)
    print(_no_unicode_dict)
EOF
```

And the executed result would look something like this:

```
./test.py
{'last-zeroed': '17744171', 'block-size': '512', 'write-ops':
'4931526577', 'write-blocks': '102771697989', 'other-ops': '3858813',
'path': '/vol/vol01/lun01', 'read-blocks': '61399766772',
'read-ops': '701198849'}
{'last-zeroed': '17744171', 'block-size': '512', 'write-ops':
'3590211758', 'write-blocks': '62391954839', 'other-ops': '2856883',
'path': '/vol/vol02/lun02', 'read-blocks': '8810635966',
'read-ops': '210642108'}
{'last-zeroed': '17744171', 'block-size': '512', 'write-ops':
'937098977', 'write-blocks': '23816240186', 'other-ops': '3131364',
'path': '/vol/vol03/lun03', 'read-blocks': '7217757779',
'read-ops': '172708839'}
```

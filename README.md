python NetApp SDK
=================
This site helps you create a small python module for interacting with your NetApp appliance.  

Pre-Conditions
==============
Because the NetAPP SDK is a licensed product, I'm not able to provide the SDK here.  Instead you will need to download the NetApp Manageability SDK from support.netapp.com and uzip it to your location of choice.  Once you have the Netapp Manageability SDK downloaded and uzipped you also need to remember the path to where you unzipped this archive.  You will need to setup `PYTHONPATH` environment to the location of your unzipped archive later. 

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

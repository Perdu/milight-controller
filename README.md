Milight controller
=============

A gateway script to control milight bulbs from multiple applications without conflicts.

## Why this script ##

Milight lamps, also called LimitlessLED, Easybulb, Applight, Applamp, LEDme, dekolight or iLight, are smart bulbs.

When controlling multiple Milight lamps from multiple sources (e.g., an arduino and a smartphone), you will experience conflicts between these sources controllers, causing them to target the wrong lamps, or not work at all (if those lamps are off). This is due to the fact that Milight commands are UDP packets which do not always indicate the targeted lamp. Then, the target may be changed to another lamp by an application when using another one, even if they don't send packets at the same time.

To solve this problem, I wrote this script to insert correct lamp selection packets when needed. To do so, the script keeps tracks of which controller targets which lamp. When the target is unknown (the script was just started or the controller has not indicated a target yet), commands will be sent to all lamps.

The script has to be run on a server between your Milight controller applications and your Milight bridge.

![Where to run the script](install.png?raw=true "Where to run the script")

## How to install ##

Copy `config.py.example` to `config.py` and add the address of your Milight bridge as well as the IP address to which your server is joinable.

Put this script on a server in your local network. Change the target IP from the bridge IP to your server IP in all your Milight controller applications. On smartphone applications, the script should appear as a new bridge with MAC address "00:00:B0:0B:00:00".

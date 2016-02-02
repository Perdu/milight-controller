Why this script:

When controlling Milight multiple lamps from multiple sources (e.g., an arduino and a smartphone), you will experience conflicts between these sources controllers, causing them to target the wrong lamps, or not work at all. This is due to the fact that Milight commands are UDP packets which do not always contain the targeted lamp. Then, the target may be changed to another lamp by one application when using another one.

To solve this problem, I wrote this script to insert correct lamp selection when needed. It has to be run on a server between your Milight controller applications and your Milight bridge.

How to install:

Copy config.py.example to config.py and add the address of your Milight bridge.
Put this script on a server in your local network. Change the target IP from the bridge IP to your server IP in all your Milight controller applications.
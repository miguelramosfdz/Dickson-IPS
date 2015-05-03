IPS-Server
==========

The source code running on the main ground computer in Dickson College's Indoor Positioning System (IPS).

Current dependencies:
	1. Python-2.7

The Dickson IPS project is a cheap alternative to professional IPS.
It uses Raspberry Pi camera board as nodes, with OpenCV running on the RPis.
The vehicles being tracked are tracked with coloured markers (the plan is to move to black & white patterns).
The IPS node converts the pixel location of the vehicles with the relative location of the RPis & the global location of the server to determine the vehicle’s location.

View IPS-Node software in action (without IPS-Server running):
1. http://gfycat.com/ArtisticWanIndianjackal
2. http://gfycat.com/PeriodicArcticBanteng (Note: Top-left GUI is made-up data)


Using the IPS with MissionPlanner:
![Map](/images/map.png?raw=true “Map”)

![Map](/images/map.png?raw=true “Map”)
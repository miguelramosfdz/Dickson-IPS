IPS-Server
==========

The source code running on the main ground computer in Dickson College's Indoor Positioning System (IPS). Its main functions are to comincate with each node (running OpenCV on a Raspberry Pi) and with each vehicle (with a Pixhawk autopilot and an XBee). The IPS server combines the pixel location of the vehicles with the relative location of the RPis & the global location of the server to determine the vehicle’s location. It converts this into NMEA format and, using XBees, sends it off the the Pixhawk autopilots.

Current dependencies:
	1. Python-2.7

View IPS-Node software in action (without IPS-Server running):
1. http://gfycat.com/ArtisticWanIndianjackal
2. http://gfycat.com/PeriodicArcticBanteng (Note: Top-left GUI is made-up data)


The on-ground hardware involved (including an autonomous system):
![Map](/images/hardware.png?raw=true “Map”)

My role in the project was as the lead software developer, working with the code running on the nodes and on the server. The roles of other students included setting up networking between RPis and the server, mounting the hardware and project management.


Idea
===

Dickson College is setting up an optical-based Indoors Positioning System. The goal of the project is to create a system capable of detecting vehicles in areas where GPS is not available, for a setup and maintenance cost affordable to any interested school or university.

Software
===

The software aspect of the IPS has been split up into two sections.

1. The IPS-Node software runs on each Raspberry Pi, recognizing vehicles and returning a pixel offset;
2. The IPS-Server software runs on a single computer, receiving pixel offsets of each vehicle, converting them into a GPS coordinates and sending it to the vehicles.

The Raspberry Pis, each connected to a Raspberry Pi camera module, make use of the open source OpenCV computer vision library to ease the task of detecting vehicles. After receiving a frame from the camera, the Pi first converts the data from the RGB (red,green,blue) to the HSV (hue, saturation, brightness) colourspace. By using a polar coordinate system rather than a three dimensional Cartesian coordinate system, HSV makes it easier to categorize colours by angles. For each vehicle in the field, the image is transformed into a 1-bit image containing only the colour of a marker on the vehicle.

After detecting the pixel offset of the vehicle, the data is send to the ground server. The ground server, upon receiving the pixel offset of a vehicle, combines it with the latitude and longitude of the relevant node to find the global position. Using the NMEA 0183 specification, defined by the National Marine Electronics Foundation, the serv- er converts the position into a format readable by the onboard autopilot. Using an xBee radio module, the server send the NMEA sentence to the autopilot, at a rate of approximately 9Hz.

The software on the autopilot and ground station of an autonomous system do not need to be modified to make use of the IPS. The only hardware modifications required for each vehicle is the replacement of the GPS module with an xBee radio module. This involves simply disconnecting one cable from the autopilot and connecting the other.


System
===

After coming up with concepts and designs for each component of the project, a prototype has been setup in a classroom, using four nodes in series. The setup uses a small autonomous Rover controlled by a Pixhawk autopilot, a groud station running both the IPS-Server software and APM Mission Planner and the four Raspberry Pi’s running the IPS-Node software. The prototype has been used to succesfully control the autopilot, setting different Way-points around the classroom. After setting up the IPS, the only equipment required to use it is an autonomous vehicle and a ground station (image above).

Using the IPS with MissionPlanner:
![Map](/images/map.png?raw=true “Map”)


Next Step
===

After completin and evaluating Dickson College’s Indoor Positioning System, the school plans on making the technology available and cheap to schools worldwide.

By using crowd-funding services online, the project will introduce students to real-world project management, strengethening financial and comunication skills.

The Positioning system is also planned to be extended to cover other uses, including physical movement-based Augmented / Virtual Reality.
The system will be used in 2015 to run various quadcopter and rover based events and competitions. In the 2014 UAV Outback Challenge, the Dickson team repurposed the IPS- Node software to detect symbols in a grass field.

# IPtracing

--About--

Function: Plots the path that an internet protocol packet takes from your point of origin

Method:
(1) Runs the command-line utility TRACERT to trace the route to a chosen web address and returns route IP addresses
(2) Uses ipapi.co to return lat and lon from IP addresses
(3) Display the packet path with plotly


--How to use--

(1) Update main.py with a destination web address (default is wikipedia.com) and run
(2) Wait several minutes

# IPtracing

--About--

Plots path of ICMP packet, from origin to destination.

Method:
(1) Runs TRACERT, maps IP addresses for packet path to specified url. 
(2) Uses ipapi.co, returns lat and lon from IP addresses. 
(3) Via plotly, geographically displays the path. 


--How to use--

(1) Install required packages from requirements.txt
(2) Update main.py with a destination web address (default is wikipedia.com) and run. 
(3) Wait several minutes.

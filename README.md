# IPtracing

## About

Plots path of ICMP packet, from origin to destination.

### Functions:
(1) tracert.py: finds IP addresses on packet path to specified url. 
(2) locate.py: returns lat and lon from IP addresses via ipapi.co. 
(3) plot.py: geographically displays packet path via plotly. 

## Usage

(1) Install required packages from requirements.txt

E.g.,
```bash
pip install -r requirements.txt
```

(2) Update main.py with a destination web address (default is wikipedia.com).
(3) Run main.py and wait a bit. IP addressses printed in terminal, plot displayed via browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)
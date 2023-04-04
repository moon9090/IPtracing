from tracert import tracert
from locate import locate
from plot import plot_trace

IPs = tracert('wikipedia.com') #returns list of IPs
print(IPs)
IP_locs = locate(IPs) #returns dataframe of locations/lat/lon etc.
print(IP_locs)
# IP_locs.to_csv('data/IP_locs.csv', index=False)
plot_trace(IP_locs)
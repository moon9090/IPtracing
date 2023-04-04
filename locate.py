import requests
import pandas as pd

ip_locs = []

def locate(IPs):
    for i in IPs:
        ip_address = i
        ip_data = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        ip_locs.append({
            "ip": ip_address,
            "city": ip_data.get("city"),
            "region": ip_data.get("region"),
            "country": ip_data.get("country_name"),
            "latitude": ip_data.get("latitude"),
            "longitude": ip_data.get("longitude"),
        })
    df = pd.json_normalize(ip_locs, max_level=1)
    df2 = pd.DataFrame(df)
    return df2

#print(locate(IPs))
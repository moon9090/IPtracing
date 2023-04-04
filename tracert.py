import subprocess
# import pandas as pd
# from io import StringIO
import re

#usage e.g., IPs = tracert('live.com')
def tracert(website):
    proc = subprocess.Popen('tracert ' + website, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tmp = proc.stdout.read() #bytes object
    s=str(tmp,'utf-8') #converting/decoding bytes object to string
    print(s)
    #find all IPs in raw text
    IPs = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', s)
    IPs = IPs[2:]

    # #--or--
    # #Pandas
    # data = StringIO(s)
    # df=pd.read_csv(data, on_bad_lines='skip')
    # IPs = df.squeeze().str.extract('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')
    # IPs = pd.DataFrame(IPs).dropna()
    # IPs.columns = ['IPs']
    # # print(IPs)

    return IPs

# print(tracert('google.com'))
import speedtest

from time import sleep
from random import uniform

speedTestHelper = speedtest.Speedtest()

speedTestHelper.get_best_server()
pre_results = speedTestHelper.results.dict()
print(f"You're testing from: {pre_results['client']['ip']} - {pre_results['client']['isp']} ISP")
download = round(speedTestHelper.download() / (1024*1024), 2)
upload = round(speedTestHelper.upload() / (1024*1024), 2)
ping = round(speedTestHelper.results.dict()['ping'])

print(f"Ping: {ping} ms    Jitter: 0 ms")
print(f"Download rate:  {download} Mbps")
print(f"Upload rate:    {upload} Mbps")

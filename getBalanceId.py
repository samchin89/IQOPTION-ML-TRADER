import time
import json
import iqoption as iq

iqStream = iq.IQOption(active_id="EURUSD")


profile = iqStream.api.getprofile()#api.getprofile()
# print profile._content
res = json.loads(profile._content)
balance = res['result']['balances']
print balance
"""
Library and framework

"""

import requests, time
from dhooks import Webhook, Embed

url = "https://api.binance.com/api/v3/ticker/price"

while True:
	r = requests.get(url)
	data = str(r.json()[0])
	# print(data)

	hook = Webhook('https://discord.com/api/webhooks/959429553665757252/XBMJoohVlpmuL5utb1Q5Lu21RWWK6sY-srrdN_SXPldV8216CYcSoE1AVlHuxIUQFzR0')
	embed = Embed(
	    description=data,
	    color=0x5CDBF0,
	    timestamp='now'  # sets the timestamp to current time
	    )
	hook.send(embed=embed)

	time.sleep(5)

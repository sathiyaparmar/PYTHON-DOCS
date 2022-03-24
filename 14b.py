trades = {
	"AAPL":{
		"entryprice":145.36,
		"exitprice":143.24,
		"quantity":369
	},
	"MSFT":{
		"entryprice":355.36,
		"exitprice":393.24,
		"quantity":35
	},
	"JNJ":{
		"entryprice":545.36,
		"exitprice":533.24,
		"quantity":5
	},
	"TWTR":{
		"entryprice":78.26,
		"exitprice":75,
		"quantity":3
	},
}

# Find net profit
	# aapl pl = (ex-en)*q
# Find percent profit
	# pr = (final-initial)/initial*100

netPL = 0

for i, val in trades.items():
	x = (val['exitprice'] - val['entryprice'])*val['quantity']
	netPL += x

print(netPL)
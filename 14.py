settings = {
	"timezone":"US/Eastern",
	"use_tz":True,
	"watchlist":
	[
		{"symbol":"TSLA",'quantity':2},
		{'symbol':"NVDA",'quantity':6},
		{'symbol':"RIOT",'quantity':23},
		{'symbol':"MRNA",'quantity':8},
		{'symbol':"FB",'quantity':4},
	]
}

# How many watchlist are there
print(len(settings['watchlist']))

# What is tsla's quantity
symbol = 'TSLA'

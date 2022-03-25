"""
find all bids, find all asks
ltp = (bid + ask)/2
"""

d = {
	"service": "NASDAQ_BOOK",
	"timestamp": 1631106279900,
	"command": "SUBS",
	"content": [
		{
			"key": "MSFT",
			"BOOK_TIME": 1631106275491,
			"BIDS": [
				{
					"BID_PRICE": 299.61,
					"TOTAL_VOLUME": 52,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "NSDQ",
							"BID_VOLUME": 52,
							"SEQUENCE": 28011809
						}
					]
				},
				{
					"BID_PRICE": 299.56,
					"TOTAL_VOLUME": 100,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "arcx",
							"BID_VOLUME": 100,
							"SEQUENCE": 29065093
						}
					]
				},
				{
					"BID_PRICE": 299.5,
					"TOTAL_VOLUME": 100,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "edgx",
							"BID_VOLUME": 100,
							"SEQUENCE": 29048286
						}
					]
				},
				{
					"BID_PRICE": 299.0,
					"TOTAL_VOLUME": 200,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "batx",
							"BID_VOLUME": 200,
							"SEQUENCE": 29016216
						}
					]
				},
				{
					"BID_PRICE": 297.8,
					"TOTAL_VOLUME": 200,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "amex",
							"BID_VOLUME": 200,
							"SEQUENCE": 21600043
						}
					]
				},
				{
					"BID_PRICE": 284.77,
					"TOTAL_VOLUME": 100,
					"NUM_BIDS": 1,
					"BIDS": [
						{
							"EXCHANGE": "baty",
							"BID_VOLUME": 100,
							"SEQUENCE": 28827241
						}
					]
				},
				{
					"BID_PRICE": 284.01,
					"TOTAL_VOLUME": 700,
					"NUM_BIDS": 7,
					"BIDS": [
						{
							"EXCHANGE": "bosx",
							"BID_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "cinn",
							"BID_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "nyse",
							"BID_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "phlx",
							"BID_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "VIRT",
							"BID_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "edga",
							"BID_VOLUME": 100,
							"SEQUENCE": 28456931
						},
						{
							"EXCHANGE": "MEMX",
							"BID_VOLUME": 100,
							"SEQUENCE": 28456931
						}
					]
				},
				{
					"BID_PRICE": 239.8,
					"TOTAL_VOLUME": 200,
					"NUM_BIDS": 2,
					"BIDS": [
						{
							"EXCHANGE": "KING",
							"BID_VOLUME": 100,
							"SEQUENCE": 28817121
						},
						{
							"EXCHANGE": "OHOS",
							"BID_VOLUME": 100,
							"SEQUENCE": 28830963
						}
					]
				}
			],
			"ASKS": [
				{
					"ASK_PRICE": 299.74,
					"TOTAL_VOLUME": 400,
					"NUM_ASKS": 4,
					"ASKS": [
						{
							"EXCHANGE": "arcx",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048285
						},
						{
							"EXCHANGE": "batx",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048285
						},
						{
							"EXCHANGE": "edgx",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048285
						},
						{
							"EXCHANGE": "NSDQ",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048285
						}
					]
				},
				{
					"ASK_PRICE": 305.93,
					"TOTAL_VOLUME": 100,
					"NUM_ASKS": 1,
					"ASKS": [
						{
							"EXCHANGE": "phlx",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048330
						}
					]
				},
				{
					"ASK_PRICE": 314.86,
					"TOTAL_VOLUME": 100,
					"NUM_ASKS": 1,
					"ASKS": [
						{
							"EXCHANGE": "baty",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048281
						}
					]
				},
				{
					"ASK_PRICE": 315.62,
					"TOTAL_VOLUME": 200,
					"NUM_ASKS": 2,
					"ASKS": [
						{
							"EXCHANGE": "edga",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28456931
						},
						{
							"EXCHANGE": "MEMX",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28456931
						}
					]
				},
				{
					"ASK_PRICE": 315.63,
					"TOTAL_VOLUME": 400,
					"NUM_ASKS": 4,
					"ASKS": [
						{
							"EXCHANGE": "cinn",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "nyse",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "VIRT",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28454938
						},
						{
							"EXCHANGE": "bosx",
							"ASK_VOLUME": 100,
							"SEQUENCE": 29048281
						}
					]
				},
				{
					"ASK_PRICE": 359.8,
					"TOTAL_VOLUME": 200,
					"NUM_ASKS": 1,
					"ASKS": [
						{
							"EXCHANGE": "TSSM",
							"ASK_VOLUME": 200,
							"SEQUENCE": 27000018
						}
					]
				},
				{
					"ASK_PRICE": 359.84,
					"TOTAL_VOLUME": 100,
					"NUM_ASKS": 1,
					"ASKS": [
						{
							"EXCHANGE": "KING",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28817121
						}
					]
				},
				{
					"ASK_PRICE": 359.86,
					"TOTAL_VOLUME": 100,
					"NUM_ASKS": 1,
					"ASKS": [
						{
							"EXCHANGE": "OHOS",
							"ASK_VOLUME": 100,
							"SEQUENCE": 28830963
						}
					]
				}
			]
		}
	]
}
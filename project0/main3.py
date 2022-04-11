import time
from datetime import datetime

# print(x)
# print(type(x))

# # =================
# tsSecond = time.time()
# print(tsSecond)

# ms = tsSecond*1000
# print(ms)

def tick_on_timeframe(interval: int) -> bool:
	"""
	interval will be 1, 2 , 10 , 15

	# 10 minute ke liye
	# 2022-04-11 17:57:00
	# 2022-04-11 17:57:13
	# 2022-04-11 17:58:00
	# 2022-04-11 17:58:01
	# 2022-04-11 18:00:00
	"""
	# code here
	currentTime = datetime.now()
	return

while True:
	

	if tick_on_timeframe(1):
		print('tick')
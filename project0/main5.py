import time
from datetime import datetime


def tick_on_timeframe(interval,index=1):
	if index == 1: # not better while changing machine
		return datetime.now().second == 0 and datetime.now().minute % interval == 0

	elif index == 2: # better (machine independent)
		cT = datetime.now()
		return cT.second == 0 and cT.minute % interval == 0

while True:

	if tick_on_timeframe(1):
		print("tick")
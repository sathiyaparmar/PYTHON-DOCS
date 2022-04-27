from datetime import datetime

import time

class Bot:

	def __init__(self, creds:dict, config:dict):

		self.CREDS = creds
		self.CONFIG = config

	def tick_on_timeframe(self,tf):
		cT = datetime.now()
		return cT.minute % tf == 0 and cT.second == 0

	def run(self):

		while True:
			if self.tick_on_timeframe(1):
				print('tick')

				time.sleep(1)

				# TODO

creds = {}
config = {}
bot1 = Bot(creds,config)
bot1.run()
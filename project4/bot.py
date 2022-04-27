import time

class Bot:
	

	def __init__(self, creds:dict, config:dict):

		self.CREDS = creds
		self.CONFIG = config

	def update_parameters(self, config:dict):
		self.CONFIG = config

	def run(self):
		while True:
			print(self.CONFIG)
			time.sleep(2)


if __name__ == '__main__':

	creds = {}
	config = {}

	bot1 = Bot(creds,config)
	bot1.run()
import threading, time

from bot import Bot

creds = {}
config = {"factor":7}

bot1 = Bot(creds, config)

# This is running in a separate thread
t = threading.Thread(target=bot1.run)
t.start()

time.sleep(5)
config = {"factor":5555}
bot1.update_parameters(config)
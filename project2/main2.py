import pickle, os 

# x = {"my_data":"some data"}

picklePath = os.path.join(os.path.dirname(__file__),'dummy.pk') # pickle, pkl, pk

# with open(picklePath,'wb') as f:
# 	pickle.dump(x,f)
# 	f.close()

with open(picklePath,'rb') as f:
	x = pickle.load(f)
	f.close()

print(x)

# I/O operations
# txt
# json
# csv, xlsx
# pickle
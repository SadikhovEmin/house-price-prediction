import pickle

# Using already created model
pickle_in = open('finalized_model.sav', 'rb')
loaded_model = pickle.load(pickle_in)
pickle_in.close()



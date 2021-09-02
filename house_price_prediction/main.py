import pickle
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['house_price_prediction']
collection = db['prices']

# prediction = {
#     'Avg. Area Income': 79545.45857431678,
#     'Avg. Area House Age': 5.682861321615587,
#     'Avg. Area Number of Rooms': 7.009188142792237,
#     'Avg. Area Number of Bedrooms': 4.09,
#     'Area Population': 23086.800502686456,
#     'Price': 1059033.5578701235
# }


# x = collection.insert_one(prediction)
# print('inserted id : ', x.inserted_id)


# Using already created model
# pickle_in = open('finalized_model.sav', 'rb')
# loaded_model = pickle.load(pickle_in)
# pickle_in.close()
#
# ''' Making predictions '''
# sample_input = [[51156.73942606786, 5.594270942207965, 6.976381319424375, 2.39, 25753.28312030552]]
# # sample_input.reshape(1, -1)
# predict = loaded_model.predict(sample_input)
# print('Prediction : ', predict)


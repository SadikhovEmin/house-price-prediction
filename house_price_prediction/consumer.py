from json import loads
from kafka import KafkaConsumer
import pickle
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['house_price_prediction']
collection = db['prices']

consumer = KafkaConsumer(
    'model',
    bootstrap_servers=['localhost:9092'],
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# Using already created model
pickle_in = open('finalized_model.sav', 'rb')
loaded_model = pickle.load(pickle_in)
pickle_in.close()

''' Getting data and making predictions '''
for i in consumer:
    temp = i
    i = i.value
    sample_input = [[i['Avg. Area Income'], i['Avg. Area House Age'],
                     i['Avg. Area Number of Rooms'], i['Avg. Area Number of Bedrooms'], i['Area Population']]]

    predict = loaded_model.predict(sample_input)
    print('Prediction : ', predict)

    i.update({'Price': predict[0]})  # Appending price to json
    print(i)
    x = collection.insert_one(i)
    print('inserted id : ', x.inserted_id)



from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
prediction = {
    'Avg. Area Income': 79545.45857431678,
    'Avg. Area House Age': 5.682861321615587,
    'Avg. Area Number of Rooms': 7.009188142792237,
    'Avg. Area Number of Bedrooms': 4.09,
    'Area Population': 23086.800502686456,
    # 'Price': 1059033.5578701235
}


for e in range(1):
    data = {'number': e}
    producer.send('model', value=prediction)
    sleep(5)

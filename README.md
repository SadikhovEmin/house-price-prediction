# House Price Prediction

This repository contains CSV file of a house prices based on their age, # of rooms,
area income etc. Using scikit-learn library to create, train model, pickle library to save 
trained model, and kafka producer & consumer to get data to make predictions from 
that saved model. Finally, data along with model's predicted price is stored locally at 
mongodb ```house_price_prediction``` index at ```prices``` collection. 


Run these commands on separate terminal tabs

### Create a Kafka topic 
```
bin/kafka-topics.sh --create --topic model --bootstrap-server localhost:9092
```

### Start Zookeeper
```
sudo bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka Server 

```
sudo bin/kafka-server-start.sh config/server.properties
```


### Start the Kafka-Producer
```
bin/kafka-console-producer.sh --topic model --bootstrap-server localhost:9092
```


### Start Kafka-Consumer

```
bin/kafka-console-consumer.sh --topic model --from-beginning --bootstrap-server localhost:9092
```
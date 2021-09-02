# House Price Prediction

Run these commands on new terminal tabs

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
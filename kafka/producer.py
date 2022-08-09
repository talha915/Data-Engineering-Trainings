from kafka import KafkaProducer

# Create Message
msg = 'Messi is best player in the world!'

# Create a producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Function to send messages into Kafka
def kafka_python_producer_async(producer, msg):
    
    producer.send('mytesttopic', msg).add_callback(success).add_errback(error)
    producer.flush()

def success(metadata):
    print(metadata.topic)

def error(exception):
    print(exception)  

print("start producing")

# Produce the message, but serialize into bytes
kafka_python_producer_async(producer,bytes(msg, 'utf-8'))

print("done")
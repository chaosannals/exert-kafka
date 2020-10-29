from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
for i in range(100):
    print(i)
    # topic 必须先创建。
    producer.send('exert', b'some_message_bytes', partition=0)
    
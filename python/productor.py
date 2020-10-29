from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
for i in range(100):
    # topic 必须先创建。
    print(i)
    producer.send('exert', b'some_message_bytes', partition=3)
    producer.flush()
    # r = f.get(timeout=60)
    # print(f'{i} => {r}')
producer.close()
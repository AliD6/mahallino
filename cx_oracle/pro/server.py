import pika
from main import db_conn
import json

def isnfloat(num1,num2):
    try:
        float(num1)
        float(num2)
        return False
    except ValueError:
        return True

connection  = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='oracle_queue')

def on_request(ch , method  , props , body):

    body = body.decode('ascii')
    lat , lon = body.split(',')

    if isnfloat(lat,lon):
        response = str({"status" : "400" , "message" : "lat or lon not float"})
    else :
        db_con = db_conn(lat , lon)
        response = (db_con.conn())

    # print(response)
    # print(type(response))
    # print('='*90)
    # print(str(response))
    # print(type(str(response)))

    ch.basic_publish(exchange = '' , routing_key = props.reply_to , properties = pika.BasicProperties(correlation_id= props.correlation_id   ) , body = response )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='oracle_queue'  , on_message_callback= on_request)

print('waiting for requests')

channel.start_consuming()

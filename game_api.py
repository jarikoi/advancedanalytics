#!/usr/bin/env python
#Example calls
#docker-compose exec mids curl -X POST "http://localhost:5000/logout?id=6"
#dompose exec mids curl -X POST "http://localhost:5000/purchase_bomb"
#docker-compose exec mids curl -X POST "http://localhost:5000/login?id=6"
#
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword'}
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

@app.route("/purchase_bomb/<type>")
def purchase_bomb(type):
    purchase_bomb_event = {'event_type': 'purchase_bomb','bomb_type':type}
    log_to_kafka('events', purchase_bomb_event)
    return "Bomb Purchased!"+type+"\n"


@app.route("/purchase_grenades", methods=['POST'])
def purchase_grenades():
    n = request.args.get('n',default=1,type=int)
    purchase_grenades_event = {'event_type': 'purchase_grenades','n':n}
    log_to_kafka('events', purchase_grenades_event)
    return "Grenades Purchased = "+str(n)+"\n"


@app.route("/login", methods=['POST'])
def login():
    id = request.args.get('id',default=0,type=int)
    login_event = {'event_type': 'login','id':id}
    log_to_kafka('events', login_event)
    return "User logged in = "+str(id)+"\n"

@app.route("/logout", methods=['POST'])
def logout():
    id = request.args.get('id',default=0,type=int)
    logout_event = {'event_type': 'logout','id':id}
    log_to_kafka('events', logout_event)
    return "User logged out = "+str(id)+"\n

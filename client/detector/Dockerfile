FROM w251/cuda:tx2-4.2_b158

RUN apt-get update && apt-get -y install python3.7 python3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./detector.py" ]

ENV MQTT_BROKER=broker \
    MQTT_QOS=0

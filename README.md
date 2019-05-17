# W251 Homework 3

## Shane Andrade

### Usage

#### Jetson

On the Jetson run the following:
```bash
cd client
./start.sh $REMOTE_BROKER

# run the following to stop the containers:
./stop.sh
```

Where `$REMOTE_BROKER` is the public ip of the MQTT broker running on Softlayer.

#### Softlayer Instance

On your VM run the following:
```bash
cd server
./start.sh $ACCESS_KEY $SECRET_ACCESS_KEY

# run the following to stop the containers:
./stop.sh
```

### MQTT

The topic used for MQTT is `jetson/webcam/faces`. This path was chosen as it describes in a hierarchical fashion 1. which device type the data came from (`jetson`), 2. the sensor type of that device (`webcam`), and 3. the type of data coming in (`faces`).

The QoS chosen was `0` which refers to at most once delivery. This QoS was chosen due to the streaming nature of the data. Since we are dealing with a video stream, if we drop a frame, the subsequent frames will have similar data assuming we are capturing at a reasonable FPS.

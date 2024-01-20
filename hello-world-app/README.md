## Pre-requisites
1. Please Install all necessary [pre-requisite](https://github.com/abhi4578/IUDX-Devops-Workshop#pre-requisites)
2. git clone this repo with following command:

  ``` git clone https://github.com/abhi4578/IUDX-Devops-Workshop.git```
# Hello World Docker hands on

This directory contains a simple hello world web application and associated 
- Dockerfile - To build docker image 
- docker-compose.yaml - To deploy docker container in a declarative fashion

## How to deploy 
1. Build Docker image.
```docker build -t hello-world:1.0 .```


2. Run docker container using docker cli
``` docker run -p 8000:8000 --name hello-world -d <dockerhub-username>/hello-world:1.0 ```

3. Stopping docker container using docker cli
``` docker stop hello-world ```

4. Run docker container using docker compose file
```docker compose up ```

5. Bring down the containers using docker compose 
   ```docker compose down```

6. Tag and push image to registry
```docker build -t <dockerhub-username>/hello-world:1.0```


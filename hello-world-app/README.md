# Hello World Docker hands on

This directory contains a simple hello world web application and associated 
- Dockerfile - To build docker image 
- docker-compose.yaml - To deploy docker container in a declarative fashion

## How to deploy 
1. Build Docker image.
``docker build -t <dockerhub-username>/hello-world:1.0 .``

2. Push Docker image
`` docker push <dockerhub-username>/hello-world:1.0``

3. Run docker container using docker cli
`` docker run -p 8000:8000 --name hello-world -d <dockerhub-username>/hello-world:1.0 ``

4. Stopping docker container using docker cli
`` docker stop hello-world ``

5. Run docker container using docker compose file
``docker compose up ``

6. Bring down the containers using docker compose 
`` docker compose down``

FROM python:3.10-slim-bullseye
WORKDIR /user/share/app
COPY src/requirements.txt  .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src/hello-world.py .
RUN useradd -r -u 1001 -g root hello-world-user
ENTRYPOINT ["python3","hello-world.py"]

FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3.7 python3-pip && \
    apt-get install -y mongodb

RUN pip3 install pymongo==3.10 pycodestyle==2.5.*

WORKDIR /databases

COPY . /databases

EXPOSE 27017

# run mongod upon startup
CMD ["mongod", "--bind_ip_all"]

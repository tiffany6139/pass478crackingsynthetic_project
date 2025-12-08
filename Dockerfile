FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
#add sudo and no-install recommedation
RUN apt update && apt install -y sudo && apt install -y --no-install-recommends \
&& apt install -y iputils-ping \
&& apt install -y net-tools  && apt install -y iproute2\
    libpcap0.8 libpcap0.8-dev tcpdump 

#Make the user + password
RUN useradd -m user1 && \
    echo "user1:password" | chpasswd
RUN usermod -aG sudo user1

#Set user to made one
USER user1

#directory of user
WORKDIR /app

COPY attackerscript.py /app
# CMD ["python", "/app/attackerscript.py" ]

#References: https://www.baeldung.com/ops/root-user-password-docker-container
#https://www.bitdoze.com/add-users-to-docker-container/

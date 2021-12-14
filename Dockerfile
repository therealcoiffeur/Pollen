FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install the requirements.
RUN apt-get update
RUN apt-get install -y default-jre \
	net-tools \
	curl \
	nano \
	openssh-server \
	unzip \
	binutils \
	build-essential \
	sslh \
	python3-pip

RUN python3 -m pip install paramiko

# Copy source code.
RUN mkdir -p /app
WORKDIR /app
COPY ./src ./

# Use to share the log file with the host.
RUN mkdir -p /app/log

# Defined the entrypoint script.
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

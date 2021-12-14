# Pollen

## Description

Pollen is a honeypot deployable with docker (used to log HTTPS/HTTP requests paths and SSH credentials).

- SSH: SSH server listening on port 65422
- HTTS: Custom HTTP server listening on port 65443
- HTTP: Custom HTTP server listening on port 65480

### Build

To build the docker image run the following command:

```bash
$ ./build.sh
```

or this one:

```bash
$ docker build -t pollen .
```

### Run

To run the docker container run the following command:

```bash
$ ./start.sh
```

or this one:

```bash
$ docker run -p 66:66 -p 80:80 2301:2301 ... -v $(pwd)/log:/app/log -d -it -t pollen
```

### Results

The requested paths are stored in files:

- log/http_server.log
- log/https_server.log

The credentials used to authenticate users via SSH are stored in file:

- log/ssh_server.log

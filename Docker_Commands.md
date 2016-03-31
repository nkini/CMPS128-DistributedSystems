#Docker commands

This "cheatsheet" is not really meant to be the starting point for learning docker commands. It's the place you copy and paste from once you know what the command means, or finding a command you didn't know about and looking it up.

#### Starting up docker (although this should happen on startup automatically)
```shell
sudo service docker start
```

#### Build a Dockerfile
```shell
sudo docker build -t nkini/HW1
```

#### Run a docker container
```shell
sudo docker run -p 49165:8080 -d nkini/HW1
```

#### Process snapshot (Status) for Docker images
```shell
sudo docker ps
```
Output is in the format
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAME

#### Check logs for the container
```shell
sudo docker logs d2437d00b0c7
```

#### Stop a running container
```shell
sudo docker stop d2437d00b0c7
```

#### List all Images
```shell
sudo docker images
```
Output is in the format
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE

#### Start (and access) a terminal on the docker image
```shell
sudo docker run -i -t nkini/hw1 /bin/bash
```

#### Remove a container
```shell
sudo docker rm a6c2ea43802d
```

#### Remove an image
```shell
sudo docker rmi f760a1c73519
```

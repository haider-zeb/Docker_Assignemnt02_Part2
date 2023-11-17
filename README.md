Part 2: Multi-Container Application Deployment using Docker Compose

Create a Docker file for the web application container.

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker build -f
docker/web/Dockerfile -t helloworld-app . \[+\] Building 0.1s (9/9)
FINISHED docker:default =\> \[internal\] load build definition from
Dockerfile 0.0s =\> =\> transferring dockerfile: 197B 0.0s =\>
\[internal\] load .dockerignore 0.0s =\> =\> transferring context: 2B
0.0s =\> \[internal\] load metadata for docker.io/library/python:latest
0.0s =\> \[1/4\] FROM docker.io/library/python:latest 0.0s =\>
\[internal\] load build context 0.0s =\> =\> transferring context: 63B
0.0s =\> CACHED \[2/4\] COPY run.py run.py 0.0s =\> CACHED \[3/4\] COPY
Requirements.txt Requirements.txt 0.0s =\> CACHED \[4/4\] RUN pip
install -r Requirements.txt 0.0s =\> exporting to image 0.0s =\> =\>
exporting layers 0.0s =\> =\> writing image
sha256:7da20d9f204c94a5ff5c7f09e5bf7116eecfc0cd5f433a04b8a9f71eeb8f1455
0.0s =\> =\> naming to docker.io/library/helloworld-app 0.0s

What\'s Next? View a summary of image vulnerabilities and
recommendations → docker scout quickview

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker images
REPOSITORY TAG IMAGE ID CREATED SIZE helloworld-app latest 7da20d9f204c
2 weeks ago 1.05GB

Create a Docker file for the database container.

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker build -f
docker/db/Dockerfile -t mysql-db . \[+\] Building 0.4s (7/7) FINISHED
docker:default =\> \[internal\] load build definition from Dockerfile
0.0s =\> =\> transferring dockerfile: 115B 0.0s =\> \[internal\] load
.dockerignore 0.0s =\> =\> transferring context: 2B 0.0s =\>
\[internal\] load metadata for docker.io/library/mysql:latest 0.0s =\>
\[internal\] load build context 0.1s =\> =\> transferring context:
9.47kB 0.0s =\> \[1/2\] FROM docker.io/library/mysql 0.2s =\> \[2/2\]
COPY . . 0.1s =\> exporting to image 0.0s =\> =\> exporting layers 0.0s
=\> =\> writing image
sha256:7c0465e1ea20d19a8f309e108063894a490cb5bc09cf076dd6a2d044a92a9862
0.0s =\> =\> naming to docker.io/library/mysql-db 0.0s

What\'s Next? View a summary of image vulnerabilities and
recommendations → docker scout quickview

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker images
REPOSITORY TAG IMAGE ID CREATED SIZE mysql-db latest 7c0465e1ea20 3
minutes ago 596MB

Create a docker-compose.yml file

version: \"1.1\" services: web: \# will build ./docker/web/Dockerfile
build: ./docker/web ports:  - \"2010\"

db: \# will build ./docker/db/Dockerfile build: ./docker/db image:
\"mysql\" ports:  - \"3306:3306\" environment:  -
MYSQL_ROOT_PASSWORD=mysqlpassword volumes:  - ./db_data:/var/lib/mysql

Use the docker-compose up command to build and run the application

docker compuse up command executed

:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker compose up
2023/11/17 18:17:40 http2: server: error reading preface from client
//./pipe/docker_engine: file has already been closed \[+\] Building
19.6s (9/9) FINISHED docker:default =\> \[web internal\] load build
definition from Dockerfile 0.0s =\> =\> transferring dockerfile: 247B
0.0s =\> \[web internal\] load .dockerignore 0.0s =\> =\> transferring
context: 2B 0.0s =\> \[web internal\] load metadata for
docker.io/library/python:latest 0.0s =\> \[web internal\] load build
context 0.0s =\> =\> transferring context: 414B 0.0s =\> \[web 1/4\]
FROM docker.io/library/python:latest 0.0s =\> CACHED \[web 2/4\] COPY
run.py run.py 0.0s =\> \[web 3/4\] RUN pip install fastapi 15.6s =\>
\[web 4/4\] RUN pip install uvicorn 3.7s =\> \[web\] exporting to image
0.2s =\> =\> exporting layers 0.2s =\> =\> writing image
sha256:440e8d1da0516eb958c9a3e22bdecf1f63a79d879f3b534df559e4768fec3c7f
0.0s =\> =\> naming to docker.io/library/docker_assignment_2\_part_2-web
0.0s \[+\] Running 3/3 ✔ Network docker_assignment_2\_part_2\_default
Created 0.1s ✔ Container docker_assignment_2\_part_2-web-1 Created 0.1s
✔ Container docker_assignment_2\_part_2-db-1 Created 0.1s Attaching to
docker_assignment_2\_part_2-db-1, docker_assignment_2\_part_2-web-1
docker_assignment_2\_part_2-db-1 \| 2023-11-17 13:18:00+00:00 \[Note\]
\[Entrypoint\]: Entrypoint script for MySQL Server 8.2.0-1.el8 started.
docker_assignment_2\_part_2-db-1 \| 2023-11-17 13:18:01+00:00 \[Note\]
\[Entrypoint\]: Switching to dedicated user \'mysql\'
docker_assignment_2\_part_2-db-1 \| 2023-11-17 13:18:01+00:00 \[Note\]
\[Entrypoint\]: Entrypoint script for MySQL Server 8.2.0-1.el8 started.
docker_assignment_2\_part_2-db-1 \| 2023-11-17 13:18:01+00:00 \[Note\]
\[Entrypoint\]: Initializing database files
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:01.315333Z 0
\[System\] \[MY-015017\] \[Server\] MySQL Server Initialization - start.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:01.316944Z 0
\[Warning\] \[MY-011068\] \[Server\] The syntax \'\--skip-host-cache\'
is deprecated and will be removed in a future release. Please use SET
GLOBAL host_cache_size=0 instead. docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:01.317877Z 0 \[System\] \[MY-013169\] \[Server\]
/usr/sbin/mysqld (mysqld 8.2.0) initializing of server in progress as
process 80 docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:01.326991Z 1 \[System\] \[MY-013576\] \[InnoDB\] InnoDB
initialization has started. docker_assignment_2\_part_2-web-1 \| INFO:
Started server process \[1\] docker_assignment_2\_part_2-web-1 \| INFO:
Waiting for application startup. docker_assignment_2\_part_2-web-1 \|
INFO: Application startup complete. docker_assignment_2\_part_2-web-1 \|
INFO: Uvicorn running on http://0.0.0.0:2010 (Press CTRL+C to quit)
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:01.827119Z 1
\[System\] \[MY-013577\] \[InnoDB\] InnoDB initialization has ended.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:03.303960Z 6
\[Warning\] \[MY-010453\] \[Server\] root@localhost is created with an
empty password ! Please consider switching off the
\--initialize-insecure option. docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:06.690334Z 0 \[System\] \[MY-015018\] \[Server\] MySQL
Server Initialization - end. docker_assignment_2\_part_2-db-1 \|
2023-11-17 13:18:06+00:00 \[Note\] \[Entrypoint\]: Database files
initialized docker_assignment_2\_part_2-db-1 \| 2023-11-17
13:18:06+00:00 \[Note\] \[Entrypoint\]: Starting temporary server
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:06.839351Z 0
\[System\] \[MY-015015\] \[Server\] MySQL Server - start.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.072510Z 0
\[Warning\] \[MY-011068\] \[Server\] The syntax \'\--skip-host-cache\'
is deprecated and will be removed in a future release. Please use SET
GLOBAL host_cache_size=0 instead. docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:07.073684Z 0 \[System\] \[MY-010116\] \[Server\]
/usr/sbin/mysqld (mysqld 8.2.0) starting as process 124
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.091572Z 1
\[System\] \[MY-013576\] \[InnoDB\] InnoDB initialization has started.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.249325Z 1
\[System\] \[MY-013577\] \[InnoDB\] InnoDB initialization has ended.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.610012Z 0
\[Warning\] \[MY-010068\] \[Server\] CA certificate ca.pem is self
signed. docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.610052Z
0 \[System\] \[MY-013602\] \[Server\] Channel mysql_main configured to
support TLS. Encrypted connections are now supported for this channel.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.614155Z 0
\[Warning\] \[MY-011810\] \[Server\] Insecure configuration for
\--pid-file: Location \'/var/run/mysqld\' in the path is accessible to
all OS users. Consider choosing a different directory.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.642639Z 0
\[System\] \[MY-011323\] \[Server\] X Plugin ready for connections.
Socket: /var/run/mysqld/mysqlx.sock docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:07.642954Z 0 \[System\] \[MY-010931\] \[Server\]
/usr/sbin/mysqld: ready for connections. Version: \'8.2.0\' socket:
\'/var/run/mysqld/mysqld.sock\' port: 0 MySQL Community Server - GPL.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:07.647072Z 0
\[System\] \[MY-015016\] \[Server\] MySQL Server - end.
docker_assignment_2\_part_2-db-1 \| 2023-11-17 13:18:07+00:00 \[Note\]
\[Entrypoint\]: Temporary server started.
docker_assignment_2\_part_2-db-1 \| \'/var/lib/mysql/mysql.sock\' -\>
\'/var/run/mysqld/mysqld.sock\' docker_assignment_2\_part_2-db-1 \|
Warning: Unable to load \'/usr/share/zoneinfo/iso3166.tab\' as time
zone. Skipping it. docker_assignment_2\_part_2-db-1 \| Warning: Unable
to load \'/usr/share/zoneinfo/leap-seconds.list\' as time zone. Skipping
it. docker_assignment_2\_part_2-db-1 \| Warning: Unable to load
\'/usr/share/zoneinfo/leapseconds\' as time zone. Skipping it.
docker_assignment_2\_part_2-db-1 \| Warning: Unable to load
\'/usr/share/zoneinfo/tzdata.zi\' as time zone. Skipping it.
docker_assignment_2\_part_2-db-1 \| Warning: Unable to load
\'/usr/share/zoneinfo/zone.tab\' as time zone. Skipping it.
docker_assignment_2\_part_2-db-1 \| Warning: Unable to load
\'/usr/share/zoneinfo/zone1970.tab\' as time zone. Skipping it.
docker_assignment_2\_part_2-db-1 \| docker_assignment_2\_part_2-db-1 \|
2023-11-17 13:18:11+00:00 \[Note\] \[Entrypoint\]: Stopping temporary
server docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:11.232457Z
10 \[System\] \[MY-013172\] \[Server\] Received SHUTDOWN from user root.
Shutting down mysqld (Version: 8.2.0). docker_assignment_2\_part_2-db-1
\| 2023-11-17T13:18:12.465365Z 0 \[System\] \[MY-010910\] \[Server\]
/usr/sbin/mysqld: Shutdown complete (mysqld 8.2.0) MySQL Community
Server - GPL. docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:12.468211Z 0 \[System\] \[MY-015016\] \[Server\] MySQL
Server - end. docker_assignment_2\_part_2-db-1 \| 2023-11-17
13:18:13+00:00 \[Note\] \[Entrypoint\]: Temporary server stopped
docker_assignment_2\_part_2-db-1 \| docker_assignment_2\_part_2-db-1 \|
2023-11-17 13:18:13+00:00 \[Note\] \[Entrypoint\]: MySQL init process
done. Ready for start up. docker_assignment_2\_part_2-db-1 \|
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.243850Z 0
\[System\] \[MY-015015\] \[Server\] MySQL Server - start.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.465208Z 0
\[Warning\] \[MY-011068\] \[Server\] The syntax \'\--skip-host-cache\'
is deprecated and will be removed in a future release. Please use SET
GLOBAL host_cache_size=0 instead. docker_assignment_2\_part_2-db-1 \|
2023-11-17T13:18:13.467363Z 0 \[System\] \[MY-010116\] \[Server\]
/usr/sbin/mysqld (mysqld 8.2.0) starting as process 1
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.477314Z 1
\[System\] \[MY-013576\] \[InnoDB\] InnoDB initialization has started.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.685703Z 1
\[System\] \[MY-013577\] \[InnoDB\] InnoDB initialization has ended.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.940871Z 0
\[Warning\] \[MY-010068\] \[Server\] CA certificate ca.pem is self
signed. docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.940931Z
0 \[System\] \[MY-013602\] \[Server\] Channel mysql_main configured to
support TLS. Encrypted connections are now supported for this channel.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.945141Z 0
\[Warning\] \[MY-011810\] \[Server\] Insecure configuration for
\--pid-file: Location \'/var/run/mysqld\' in the path is accessible to
all OS users. Consider choosing a different directory.
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.966482Z 0
\[System\] \[MY-011323\] \[Server\] X Plugin ready for connections.
Bind-address: \'::\' port: 33060, socket: /var/run/mysqld/mysqlx.sock
docker_assignment_2\_part_2-db-1 \| 2023-11-17T13:18:13.966548Z 0
\[System\] \[MY-010931\] \[Server\] /usr/sbin/mysqld: ready for
connections. Version: \'8.2.0\' socket: \'/var/run/mysqld/mysqld.sock\'
port: 3306 MySQL Community Server - GPL.
docker_assignment_2\_part_2-web-1 \| INFO: 172.20.0.1:52512 - \"GET /
HTTP/1.1\" 200 OK

Implement a backup strategy for the database Added below script in
docker-compose.yml but doing this it created db_data folder on host
machine. volumes:  - ./db_data:/var/lib/mysql

Implement a scaling strategy for the web application.All three instances
of web application is working fine on 3 different local host ports.

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker-compose up
-d \--scale web=3 \[+\] Building 0.0s (0/0) docker:default \[+\] Running
4/4 ✔ Container docker_assignment_2\_part_2-web-1 Started 0.8s ✔
Container docker_assignment_2\_part_2-web-3 Started 0.3s ✔ Container
docker_assignment_2\_part_2-web-2 Started 0.3s ✔ Container
docker_assignment_2\_part_2-db-1 Running 0.0s

C:\\Users\\HP\\Desktop\\Docker_Assignment_2\_Part_2\>docker compose ps
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
docker_assignment_2\_part_2-db-1 mysql \"docker-entrypoint.s...\" db 14
minutes ago Up 14 minutes 0.0.0.0:3306-\>3306/tcp, 33060/tcp
docker_assignment_2\_part_2-web-1 docker_assignment_2\_part_2-web
\"python run.py\" web 13 seconds ago Up 10 seconds
0.0.0.0:65315-\>2010/tcp docker_assignment_2\_part_2-web-2
docker_assignment_2\_part_2-web \"python run.py\" web 13 seconds ago Up
11 seconds 0.0.0.0:65313-\>2010/tcp docker_assignment_2\_part_2-web-3
docker_assignment_2\_part_2-web \"python run.py\" web 13 seconds ago Up
10 seconds 0.0.0.0:65314-\>2010/tcp

Implement a monitoring strategy for the application

Used Prometheus to monitor health and perfomance of the app.

Demonstrate an understanding of Docker Compose and container
orchestration

Compose is a tool for defining and running multi-container Docker
applications. With Compose, we use a YAML file to configure our
application\'s services. Then, with a single command, we create and
start all the services from our configuration.

Container orchestration automatically provisions, deploys, scales, and
manages containerized applications without worrying about the underlying
infrastructure. Developers can implement container orchestration
anywhere containers are, allowing them to automate the life cycle
management of containers.

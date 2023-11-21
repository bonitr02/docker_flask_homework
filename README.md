# docker_flask_homework

# Docker-Flask Part 1

1. Ensure flask app deploys locally
2. In the CLI navigate to the immediate folder containing the flask app
3. Enter "docker build -t part1app . " to build the image. -t tags the image with a name
4. Enter "docker run -d -p 5001:5000 part1app " to run the image. -p maps the port of the container to the port of the host machine. The first port is for the host machine and the second port is for the container.
5. Deploy app by previewing port and changing the port to 5001
6. Enter "docker images" to display the docker instances that have been created
7. Enter "docker stop [container id]" to stop the image from running
8. Enter "docker prune -a -f" to completely delete the docker instance

# Docker-Flask Part 2
3. Documentation:
Document the process of setting up and running the two Flask applications with Docker Compose.
Discuss the role of Docker Compose and how it differs from using Docker alone.
Note any challenges encountered and how they were addressed.


# Reflections
The process of Dockerizing the applications in both parts.
The build and run commands used.
Observations, challenges faced, and reflections on the use of Docker and Docker Compose.
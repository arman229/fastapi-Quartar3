- Docker:
Docker is a platform and tool for developing, deploying, and running applications in containers. Docker is a  tool that helps you create, manage, and run containers, making it easy to deploy and test your code.
Docker is a tool which creats the container(virtual machine) and runs.

- container
A container is an isolated environment for your code
Containers are lightweight, standalone, and executable software packages that contain everything needed to run an application.
Running instance of image
- Docker Image: A Docker image is a static, immutable package of software that includes everything an application needs to run. It's a template or a blueprint for creating containers.
Image is a template of project
A Docker image is a lightweight, standalone, and executable package of software that includes everything an application needs to run, such as:

1. Code
2. Libraries
3. Dependencies
4. Tools
5. Settings

It's a snapshot of a container that can be run on any system that supports Docker, without requiring a specific environment or configuration.

- BaseImage
A base image is like the foundation or starting point for creating more complex images in Docker. It's a pre-built image that already contains a basic operating system and some essential software components. Developers use base images as a starting point for building their own custom images by adding additional layers of software, configurations, and application code on top.
Docker image is a class and docker container is object" - This is the best single line explanation for docker image vs container

Installing Docker Desktop 

## Check Docker version
  
      docker --version

## Test Docker installation

    docker run hello-world
## Building the Docker Image
  
    docker build -f Dockerfile.dev -t image_naem .
-f: if my docker image name is specfied then we use -f to find the file naem
-t: This is the docker image name 
* Note: Don't forget to add the . at the end of this command

## check Images

    docker image


## find the additional information to the image

    docker inspect image_name

## Running the docker image

    docker run --name docker_pro -p 8000:8000 -it dockerproimg:latest

#List Running containers
  

    docker ps
    OR
    docker container ls

 # Running the Container and start a Bash shell:

      docker run -it image_name /bin/bash
# Opening the command line in the container:

      docker exec -it image_name bash    

# Difference between RUN and CMD commands in docker file
Run : this command will execute when we build docker image
CMD : this command will execute when we run the docker image




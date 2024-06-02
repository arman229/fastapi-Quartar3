
# Docker:
Docker is a platform and tool for developing, deploying, and running applications in containers.
Docker is a  tool that helps you create, manage, and run containers, making it easy to deploy and test your code.
Docker is a tool which creats the container(virtual machine) and runs.
Here's a revised version:

"Why do we need to use Docker? Let's consider a scenario: suppose we've been working on a frontend application project for two months, successfully completing it. Now, it's time for testing. During our development, we were using Node.js version 18.0 and React version 12.0. However, when a tester clones our project and installs all the dependencies, they might encounter issues. This is because React and Node.js could have been updated since we last worked on the project, potentially introducing errors or deprecating features in previous versions.

Docker offers a solution to this problem. With Docker, we can ensure that the exact dependencies and environment used during the last two months of development are replicated. Docker allows us to package our application along with its dependencies, libraries, and environment settings into a container. This means that when a tester runs the application in a Docker container, they will be using the same versions of Node.js and React that we used during development.

In essence, Docker provides consistency and reproducibility in software development environments. By encapsulating our application and its dependencies in a container, Docker eliminates the "it works on my machine" problem and ensures that our application behaves consistently across different environments and setups."

# container
A container is an isolated environment for your code
Containers are lightweight, standalone, and executable software packages that contain everything needed to run an application.
Running instance of image
#  Docker Image:
A Docker image is a static, immutable package of software that includes everything an application needs to run. It's a template or a blueprint for creating containers.
Image is a template of project
A Docker image is a lightweight, standalone, and executable package of software that includes everything an application needs to run, such as:

1. Code
2. Libraries
3. Dependencies
4. Tools
5. Settings

It's a snapshot of a container that can be run on any system that supports Docker, without requiring a specific environment or configuration.

# BaseImage
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

      docker run --container_name -it   -p 8000:8000 image_name /bin/bash
# Opening the command line in the container:

      docker exec -it image_name bash    

# Difference between RUN and CMD commands in docker file
Run : this command will execute when we build docker image
CMD : this command will execute when we run the docker image




Stop the Container:

     docker stop container_name

Kill the Container:

     docker rm container_name
In summary, docker stop is used to gracefully stop a container, allowing it to clean up resources before stopping, while docker kill forcefully terminates a container immediately.

Test the Container:

      docker run -it --rm my-dev-image /bin/bash -c "poetry run pytest"

container logs

docker logs dev-cont1


how we can build docker image?


          docker build -f Dockerfile -t image_name . 
how we can run docker contanier?
   
         docker run -d --name container_name -p 8000:8000 image_name

docker exec -it dev-cont1 /bin/bash
docker run -it my-dev-image /bin/bash

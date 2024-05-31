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

    docker run --name container_name -it image_name

#List Running containers
  

    docker ps
    OR
    docker container ls


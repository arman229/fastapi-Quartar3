# Dev Container

A Dev Container is an extension in VS Code. Basically, the purpose of a Dev Container is to allow us to open a container within VS Code. It has several features, such as automatically building our image and running it in a container. Additionally, we can add specific extensions to our project within the container.

To use a Dev Container, follow these steps:

First, install the Dev Container extension in VS Code.
Secondly:
Click on "Remote Explorer."
Open the folder in the container.
Add configuration to the workspace:
Select "From Dockerfile."
Click "OK."
This process will add two files to your project:    .devcontainer.
.devcontainer: We can add some extensions to our project by enabling them in a container.

Why do we use a Dev container? 
Sometimes, when we're working on a project and we create an image to run in a container, and we want to add some extensions to our project, we can do so using the Dev container.
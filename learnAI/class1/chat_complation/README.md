# AI Project Setup Using Poetry and FastAPI
Steps to Create an AI Project
Step 1: Initialize the Project
Create a project using Poetry:
   
      poetry new your_project_name --name app
      cd your_project_name

Inside the project directory, create a Dockerfile.
Step 2: Setup Docker Compose
Create a file named compose.yaml with the necessary configuration.
Run the Docker Compose command to set up the environment:
 
 
      docker compose up

Add necessary packages to pyproject.toml in the devcontainer. To add the OpenAI package, use:
 
 
      poetry add openai

Step 3: Write and Run Code
Write all the code in a Jupyter Notebook file (.ipynb).
Run the cells in the Jupyter Notebook to execute the code.
#### Important Notes
* API Keys Security: OpenAI keys must be deleted after the project is complete.
* Environment Variables:
* Store the keys in a .env file.
* Create a file named .backupenv. If working on a client project, the client should rename .backupenv to .env and write their API keys in this file.
* Git Ignore: Ensure the .env file is included in .gitignore to prevent sensitive information from being committed to the repository:
     
     
       .env



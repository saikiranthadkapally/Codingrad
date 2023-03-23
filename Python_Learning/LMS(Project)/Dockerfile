
# Basic structure of Docker for beginners.on-going it will change based up-on backend infrastructure.
# Docker is a platform and tool for building, deploying, and running applications using containers. 
# Containers are a lightweight form of virtualization that allow you to package an application and its dependencies into a single, 
# self-contained unit that can run consistently on any system.
# Docker allows you to automate the process of building, testing, and deploying applications, making it easier to manage dependencies, 
# configure the environment, and scale your applications. With Docker, you can run multiple containers on the same host, and
# isolate your applications from one another, which helps to avoid conflicts and improve security.
# The benefits of using Docker include:
# Portability: Docker containers can run on any system with a Docker engine, 
# making it easier to move applications from one environment to another.
# Isolation: Docker containers run isolated from the host system and from other containers, 
# making it easier to manage dependencies and avoid conflicts.
# Scalability: Docker makes it easy to scale applications horizontally by adding or removing containers as needed.
# Ease of use: Docker provides a simple and intuitive command-line interface and API, 
# making it easy to automate the deployment of applications.
# Docker is used in a variety of environments, including:
# Development: Docker can be used to create a consistent development environment, making it easier to test and debug applications.
# Production: Docker can be used to deploy and manage applications in production environments, 
# making it easier to scale and maintain applications.
# Continuous Integration and Continuous Deployment (CI/CD): Docker can be used in a CI/CD pipeline to automate the build, test, and 
# deployment of applications.
# Cloud computing: Docker can be used to deploy applications on cloud platforms such as Amazon Web Services (AWS), Microsoft Azure, and 
# Google Cloud Platform (GCP).
# Overall, Docker is a versatile and powerful tool that makes it easier to build, deploy, and run applications,
# and is widely used in the software development and deployment industry.

# A container is a lightweight and stand-alone executable package of software that includes everything needed to run a piece of software, 
# including the code, runtime, libraries, environment variables, and config files. 
# Containers provide a consistent and isolated environment for running applications, 
# which makes it easier to manage dependencies, configure the environment, and deploy applications.
# Containers differ from traditional virtualization in that they do not require a full virtual machine with a separate operating system.
# Instead, containers share the host operating system and use Linux namespaces and cgroups to isolate the application and its dependencies. 
# This makes containers more lightweight and efficient than traditional virtual machines,
# and allows multiple containers to run on the same host without interfering with one another.
# Docker is a platform and tool for building, deploying, and running applications using containers.
# With Docker, you can build, package, and distribute applications in containers, making it easier to manage dependencies,
# configure the environment, and deploy applications.



From python:

WORKDIR /src

COPY /src/

COPY requirements.txt /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python main.py
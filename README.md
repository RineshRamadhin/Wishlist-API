# Wishlist API
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f11553d1c0194419b1dcbf104c93992a)](https://www.codacy.com/manual/rinesh.ramadhin/Wishlist-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RineshRamadhin/Wishlist-API&amp;utm_campaign=Badge_Grade)

Django RESTful api for Wishlist.

## Installation

The Wishlist API requires the following software and OS to be installed:

-   Apple Mac OS Yosemite 10.10.3+ or Microsoft Windows 10 Professional/Enterprise 64-bit
-   [Docker Desktop](https://www.docker.com/products/docker-desktop) 

On lower versions of Mac OS, Windows, or on Linux, 
the [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) 
can also be installed, although the Wishlist API is not originally developed using this tools.

## Startup guide

 -  Open a terminal window in the project folder
 -  Copy the .env.dist file to .env and fill in the values
 
   ``` bash
   $ cp .env.dist .env
   ```

 -  Run the following code to prepare and start the required containers

   ``` bash
   $ docker-compose build
   ```

 -  Start all containers in detached mode (see below)
 -  Create a superuser

   ``` bash
   $ docker exec -it api_django_1 sh
   python manage.py createsuperuser
   ```

## Microservices/containers
### Start all project microservices/containers

``` bash
docker-compose up
```

Include ```-d``` after this command to start the containers detached.

### Stop all project microservices/containers
``` bash
docker-compose down
```

### Enter a container
``` bash
docker exec -it {container name or ID} bash
```

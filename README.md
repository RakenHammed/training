
# A Simple User RESTful API 

A simple User RESTful API developed using Flask(python) and PostgresSQL, using a clean architecture.


## Setup development environment
#### Requirements
Python3.10

Poetry1.2.1

PostgresSQL >= 14
#### Setup

Use the script setup_dev_env.sh to setup a virtual environment and activate it on your working terminal, then it will install dependencies using poetry and setup 
the pre-commit pipeline that will check code integrity and format using pylint, isort and black.

To use the script run  

```bash
    source setup_dev_env.sh
```

copy the .env.dist to .env
```bash
    cp .env.dist .env
```
and add the postgressql uri

## Run Locally
#### Using flask server directly from the terminal
Once dependencies installed and PostgresSQL database running you can run the app using in normal mode
```bash
    flask run
```
or  in debug mode
```bash
    flask --debug run
```
#### Using containers

If you do not want to bother with dependencies and database issues you can build and run the app directly using docker
```bash
    docker compose up --build
```

## TODO
Tests !!!!!!!!!!

Even though I have designed this API to be easy to test, I think some modification maybe needed to implement unit tests.

Add roles for user.
Add creation and update date in model to keep history of changes.
Add a JWT token creation and verification to restrict access to the api.


## Notes

You can run the postgres container independently if you don't wont to install it locally

If you run the app using docker you need to use the name of the postgres container as the host

You may encounter sometime problems when running postgres due to some malfunctioning that keeps the port 5432 in use
you can run these commands to tackle this issues.
```bash
    sudo lsof -i:5432 # copy the process id
    sudo kill -9 process_id
```
#### This may be helpful if you installed postgres locally
After installing:

Initialize a database storage area on disk :
```bash
    sudo mkdir /usr/local/pgsql/data
    sudo chown -v postgres /usr/local/pgsql
```

add these lines as sudoer to /var/lib/postgresql/.bash_profile to be able to use postgres command line in any user terminal:

        PATH=/usr/local/pgsql/bin:$PATH
        export PATH
        PATH=/usr/lib/postgresql/{version}/bin:$PATH
        export PATH
then run 
```bash
sudo su - postgres
initdb  -D /usr/local/pgsql/data
```
Running Server:

from your user
```bash
    sudo su - postgres -c 'pg_ctl start -D /usr/local/pgsql/data -l logfile'
```
from postgres user:
```bash
    pg_ctl start -D /usr/local/pgsql/data -l logfile
```

Shutting down the server :

from your user
```bash
    sudo su - postgres -c 'pg_ctl stop -D /usr/local/pgsql/data'
    #or
    sudo kill -INT `sudo head -1 /usr/local/pgsql/data/postmaster.pid`
```
from postgres user:
```bash
    pg_ctl -D stop
    #or
    kill -INT `head -1 /usr/local/pgsql/data/postmaster.pid`
```

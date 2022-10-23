first time:
    initialize a database storage area on disk :
        sudo mkdir /usr/local/pgsql/data
        sudo chown -v postgres /usr/local/pgsql
    add these lines to /etc/profile to be able to use postgres command line in any user terminal:
        PATH=/usr/local/pgsql/bin:$PATH
        export PATH
    sudo su - postgres
    initdb  -D /usr/local/pgsql/data

Running Server:
    from your user :
        sudo su - postgres -c 'pg_ctl start -D /usr/local/pgsql/data -l logfile'
    from postgres user:
        pg_ctl start -D /usr/local/pgsql/data -l logfile

Shutting down the server :
    from your user :
        sudo su - postgres -c 'pg_ctl stop -D /usr/local/pgsql/data'
        or
        sudo kill -INT `sudo head -1 /usr/local/pgsql/data/postmaster.pid`
    from postgres user
        pg_ctl -D stop
        or
        /usr/bin/kill -INT `/usr/bin/head -1 /usr/local/pgsql/data/postmaster.pid`

TODO: configure user in the database
logs from user :

sudo tail -f -n 500 /var/lib/postgresql/logfile
you need this to use postgres
pip install psycopg2-binary

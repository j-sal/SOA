SOA Project
Repo for Service Oriented Architecture group project

Installation Instructions:

Install python3.5 on your machine
Install postgres on your machine
Install python dependencies outlined in setup.py
Start your postgres server installation (for me the command to do so is: postgres -D /usr/local/var/postgres)
Create database to use by running the command createdb insurer_one
Create database table structure by running these commands:
psql insurer_one
\i DB_setup.sql (in the Insurer_One_Python directory)
Start application by running python3.5 main.py while in the Insurer_One_Python directory
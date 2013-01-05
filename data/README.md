
Initial Setup
-------------

    mysql> CREATE USER 'vuvuzela'@'localhost' IDENTIFIED BY 'alezuvuv';
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'vuvuzela'@'localhost' WITH GRANT OPTION;

Database Scripts
----------------

    $ ./create.sh   # creates database and tables
    $ ./insert.sh   # inserts initial data
    $ ./delete.sh   # drops the database



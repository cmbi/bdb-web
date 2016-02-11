## Pre-requisites

The following pre-requisites are required by bdb-web and must be installed
manually:

* libfreetype6
* libfreetype6-dev
* pandoc
* supervisor
* virtualenv
* virtualenvwrapper


## Running in Docker:

BDB web comes with a Docker file. To build the Docker image, run the
following from the project root folder:

    build -t bdb-web .

To run the Docker container, you need a data directory with two subdirectories
called 'bdb' and 'pdb', containing all the data files. An example:

    run -v /home/cbaakman/projects/bdb-web:/app -v /mnt/cmbi4:/data -p 16000:16000 -it bdb-web

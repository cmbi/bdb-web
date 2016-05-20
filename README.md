## Pre-requisites

The following pre-requisites are required by bdb-web and must be installed
manually:

* libfreetype6
* libfreetype6-dev
* pandoc
* supervisor
* virtualenv
* virtualenvwrapper

## Settings

Copy `settings.example` in the `config` directory to e.g.
`config/bdb_web_settings.cfg` and modify it to your needs.

## Running in Docker:

BDB web comes with a Docker file. To build the Docker image, run the
following from the project root folder:

    docker build -t bdb-web .

To run the Docker container, you need a data directory with two subdirectories
called 'bdb' and 'pdb', containing all the data files. (Adjust the
configuration file accordingly). An example:

    docker run -v /path/to/bdb-web:/app -v /host:/data -p 16000:16000 -it bdb-web

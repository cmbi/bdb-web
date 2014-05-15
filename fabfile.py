from fabric.api import cd, env, prefix, run, sudo, task
from fabric.contrib.files import exists

env.user = "bdb-web"
env.hosts = ["cmbi23.cmbi.umcn.nl"]


def update_source():
    """Updates the source code on the host.

    If the git repository already exists on the host, `git pull` is used;
    otherwise, `git clone` is used.
    """
    if exists("~/bdb-web"):
        with cd("~/bdb-web"):
            run("git pull")
    else:
        with cd("~"):
            run("git clone https://github.com/cmbi/bdb-web.git")


def update_virtualenv():
    """Updates the virtualenv on the host."""
    with cd("~/bdb-web"):
        with prefix(". /usr/local/bin/virtualenvwrapper.sh; workon bdb-web"):
            run("pip install -r requirements")


@task
def restart_gunicorn():
    """Restarts gunicorn on the host using supervisorctl."""
    sudo("supervisorctl restart bdb-web")


@task
def deploy():
    update_source()
    update_virtualenv()
    restart_gunicorn()

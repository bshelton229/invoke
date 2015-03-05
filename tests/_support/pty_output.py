import os
from invoke.tasks import task
from invoke.runner import run


cmd = "echo foo && {} bar".format(os.path.join('.', 'err.py'))


def _go(hide):
    run(cmd, hide=hide, pty=True)

@task
def hide_out():
    _go('out')

@task
def hide_err():
    _go('err')

@task
def hide_both():
    _go('both')

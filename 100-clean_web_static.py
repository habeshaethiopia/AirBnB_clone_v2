"""clean up"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.174.204.151', '54.89.179.146']

def do_clean():
    """TO CLEAN  outdated tgz files"""
    local("ls -1t versions | tail -n +2 | xargs -I {} rm versions/{}")
    run("ls -1t /data/web_static/releases | tail -n +2 | xargs -I {} rm -rf /data/web_static/releases/{}")


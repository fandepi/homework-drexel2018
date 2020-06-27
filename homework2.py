__author__ = "fandelin"
__email__ = "fandl18@lzu.edu.cn"
__version__ = "v1.0"

import re, time
from subprocess import Popen, PIPE,DEVNULL
import unicodedata
import matplotlib.pyplot as plt

def get_version(version: list, place):
    for ver in version:
        cmd_tag = 'git tag -l ' + '"' + ver + '.*"'
        p = Popen(cmd_tag, cwd = place, stdout=PIPE, shell=True)
        date, res = p.communicate()
        ver_date = date.decode('latin').encode('utf8').decode('utf8').split("\n")
        v_time=[]
        for v in ver_date:
            cmd_time = 'git log -1 --pretty=format:\"%ct\" ' + str(v)
            p = Popen(cmd_time, cwd = place, stdout = PIPE, shell = True)
            ver_time, res = p.communicate()
            ver_time = int(ver_time.decode('latin').encode('utf8').decode('utf8'))
            v_time.append(ver_time)
    plt.scatter(v_time, ver_date)   			
		
repo = '/tmp/linux-stable'
versions=['v4.1', 'v4.2', 'v4.3', 'v4.4', 'v4.5', 'v4.6', 'v4.7', 'v4.8', 'v4.9', 'v4.10']
get_version(versions, repo)
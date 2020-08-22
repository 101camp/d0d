# -*- coding: utf-8 -*-
'''inv matter for auto pub. 101.camp
'''

__version__ = 'pub101CAMP v.200822.1742'
__author__ = 'Zoom.Quiet'
__license__ = 'MIT@2019-04'

#import io
import os
#import re
import sys
import time
#import datetime
#import json
#import marshal as msh
#import subprocess
#import logging

#import sys
import logging
#logging.basicConfig()
logging.basicConfig(level=logging.CRITICAL)
_handler = logging.StreamHandler()
_formatter = logging.Formatter("[%(levelname)s]%(asctime)s:%(name)s(%(lineno)s): %(message)s"
                #, datefmt='%Y.%m.%d %H:%M:%S'
                , datefmt='%H:%M:%S'
                )
_handler.setFormatter(_formatter)
LOG = logging.getLogger(__name__)
#LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)  
LOG.propagate = False

LOG.addHandler(_handler)
#LOG.debug('load LOG level')




from pprint import pprint as pp
#pp = pprint.PrettyPrinter(indent=4)
from pprint import pformat

#import platform
#os_name = platform.system()
#del platform

#import subprocess





from invoke import task
#from fabric.context_managers import cd
from textwrap import dedent as dedentxt

CAMPROOT = os.environ.get("ABOOKS_ROOT")
CSITES = {'d0d':{'src':'d0d_mkdocs'
                , 'ghp':'d0d'
                , 'log':''
                , 'CNAME':'d0d.101.camp'
                }
        }

AIM = 'site'
_TRIP = '_trigger'
_TOBJ = 'deploy.md'
TRIGGER = 0


@task 
def ver(c):
    '''echo crt. verions
    '''
    print('\n\t powded by {}'.format(__version__))


#   support stuff func.
def cd(c, path2):
    os.chdir(path2)
    print('\n\t crt. PATH ===')
    c.run('pwd')

#@task 
def ccname(c, site):
    '''base cfg. write CNAME into aim path
    '''
    #print(CSITES[site]['CNAME'])
    _aim = '%s/%s/CNAME'%(CAMPROOT, CSITES[site]['ghp'])
    _cmd = "echo {} > {}".format(CSITES[site]['CNAME'], _aim)
    print(_cmd)
    c.run(_cmd, hide=False, warn=True)
    c.run('cat %s'% _aim, hide=False, warn=True)

    return None

    c.run('cp CNAME %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')

#@task 
def sync4media(c):
    c.run('cp -rvf img %s/'% AIM, hide=False, warn=True)
    c.run('ls %s/'% AIM, hide=False, warn=True)
    c.run('pwd')


@task 
def pl(c, site):
    '''$ inv pl [101|py] <- pull all relation repo.
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    if site:
        #pp(CSITES[site])
        
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
        _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
        cd(c, _aim)
        #os.chdir(_aim)
        #c.run('pwd')
        c.run('git pull', hide=False, warn=True)
    else:
        ver(c)


@task 
def bu(c):
    '''usgae MkDocs build AIM site
    '''
    c.run('pwd')
    c.run('mkdocs -q build', hide=False, warn=True)

#@task 
def pu(c):
    '''push gl manuscript...
    '''
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"inv(loc) MkDocs upgraded by DAMA (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#   'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '


#@task 
def gh(c, site):
    '''$ inv gh [101|py] <- push gh-pages for site publish
    '''
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    
    ccname(c, site)
    sync4media(c)
    
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )
    
    _aim = '%s/%s'%(CAMPROOT, CSITES[site]['ghp'])
    cd(c, _aim)
    #os.chdir(AIM)
    #with cd('site/'):
    #c.run('pwd')
    c.run('ls')
    c.run('git st', hide=False, warn=True)
    #c.run('git add .', hide=False, warn=True)
    #c.run('git ci -am '
    c.run('git imp '
          '"pub(site) gen. by MkDocs as invoke (at %s)"'% _ts
                    , hide=False, warn=True)
    #c.run('git pu', hide=False, warn=True)

#@task
def chktri(c):
    '''check trigger obj. set TRIGGER switch
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _path =  './%s'% _TRIP
    print(_path)
    #print(os.listdir(_path))
    #print(type(os.listdir(_path)))
    if _TOBJ in os.listdir(_path):
        print('TRIGGERed by %s exist'% _TOBJ)
        TRIGGER = 1
    else:
        print('TRIGGER obj. -> %s ~> NOT exist\n\t CANCEL build...'% _TOBJ)
        TRIGGER = 0

#@task
def recover(c):
    '''recover trigger state, by del TRIGGER obj.
    '''
    global TRIGGER
    global _TRIP, _TOBJ
    #cd(c, '%s/%s/%s'%(_DU19, PUB, _TRI))
    _path =  './%s'% _TRIP
    _obj =  '%s/%s'%(_path, _TOBJ)
    print(_obj)
    c.run('rm -vf %s'% _obj)
    c.run('ls -Aogh %s'% _path)

    c.run('git st')
    c.run('git fix "(pubDUW) recover trigger obj. wait NEXT deploy"')

    TRIGGER = 0
    print('TRIGGER obj. recover -> waiting human deploy again')


@task 
def pub(c, site):
    '''$ inv pub [101|py] <- auto deploy new site version base multi-repo.
    '''
    global TRIGGER
    global CAMPROOT
    global CSITES
    print(CAMPROOT)
    pl(c, site)
    _crt = '%s/%s'%(CAMPROOT, CSITES[site]['src'])
    cd(c, _crt)
    print('auto deplo NOW:')

    #return None
    bu(c)
    #recover(c)

    pu(c)
    ccname(c, site)
    sync4media(c)
    gh(c, site)
    ver(c)

    return None
    
    chktri(c)
    if TRIGGER:
        print('auto deplo NOW:')
        #return None
        bu(c)
        recover(c)

        pu(c)
        #ccname(c)
        #sync4media(c)
        gh(c, site)
        ver(c)

    else:
        print('nothing need deploy')
    
    return None






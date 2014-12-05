from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp
from factory import *
import os

@step(u'Given I have my localhost as my domain')
def given_i_have_my_localhost_as_my_domain(step):
    assert True
    
@step(u'When I run the factory')
def when_i_run_the_factory(step):
    print os.system('python factory.py')

@step(u'Given I have my locahost as my domain')
def given_i_have_my_locahost_as_my_domain(step):
	assert True

@step(u'Then I can access HTTP files')
def then_i_can_access_http_files(step):
    if os.path.isfile('/home/darin/Documents/CSC184/Factory/'):
        a=open('ftpfiles.txt', 'r')
        read=a.readlines()
        for i in read:
        	print i
    else:
    	print "Selected path is not file"

@step(u'Then I can access the FTP files')
def then_i_can_access_the_ftp_files(step):
    if os.path.isfile('/home/darin/Documents/CSC184/Factory/'):
        a=open('ftpfiles.txt', 'r')
        read=a.readlines()
        for i in read:
        	print i
    else:
    	print "Selected path is not file"
       
    

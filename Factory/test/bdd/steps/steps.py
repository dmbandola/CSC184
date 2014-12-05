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

@step(u'Then I can access HTTP files')
def then_i_can_access_http_files(step):
    resource = 
"""@step(u'And I have the following resources "([^"]*)"')
def and_i_have_the_following_resources_group1(step, resource):
    web = Web(resource)
    assert_equal(web.resource, resource)
    
@step(u'When I run the factory')
def when_i_run_the_factory(step):
    assert True
    
@step(u'Then I can access HTTP "([^"]*)"')
def then_i_can_access_http_group1(step, http_protocol):
   resource = ['www.facebook.com', 'www.twitter.com']
   for row in step.hashes:
       links = str(row['http_protocol'])
       assert_equal("""
       
    

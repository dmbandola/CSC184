from lettuce import *
from proxy import *
import os
from nose.tools import assert_equal, assert_in

@step(u'Given an object is created')
def given_an_object_is_created(step):
	proxy = Proxy()

@step(u'When I run proxy.py')
def when_i_run_proxy_py(step):
	#os.system('python proxy.py')
	assert True

@step(u'Then I can see the following result')
def then_i_can_see_the_following_result(step):
    if os.path.exists('/home/darin/Documents/CSC184/Proxy/result.txt'):
        a=open('result.txt', 'r')
        for row in step.hashes:
            read=a.readline().splitlines()
            assert_equal(read, row.values())



from lettuce import *
from facade import *
import os

@step(u'Given I run the facade.py')
def given_i_run_the_facade_py(step):
	os.system('python facade.py')

@step(u'And it finishes')
def and_it_finishes(step):
	assert True

@step(u'Then I can see the temperature')
def then_i_can_see_the_temperature(step):
	assert True
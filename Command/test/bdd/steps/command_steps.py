from lettuce import step
import os

@step(u'Given I have "([^"]*)" in my directory')
def given_i_have_group1_in_my_directory(step, content):
	if os.path.exists('/home/darin/Documents/CSC184/Command/'):
		path = '/home/darin/Documents/CSC184/Command/' + content
        assert os.path.isfile(path)

@step(u'And I run command.py')
def and_i_run_command_py(step):
    os.system('python command.py')

@step(u'When it finishes successfully')
def when_it_finishes_successfully(step):
	assert True

@step(u'Then I can see the result')
def then_i_can_see_the_result(step):
	list = []
	a = open('command.txt','r')
	read = a.readlines() 
	for i in range(len(read)): 
		list.append(read[i].rstrip('\n'))
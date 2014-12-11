from lettuce import step
from observer import *
from nose.tools import assert_equal, assert_in

@step(u'Given I run the file')
def given_i_run_the_file(step):
  #os.system('python observer.py')
  assert True

@step(u'When it finishes')
def when_it_finishes(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.register_observer(user)
  assert_equal(len(subject.observers), 1)

@step(u'Then I will see the following')
def then_i_will_see_the_following(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.register_observer(user)
  subject.notify_observers()
  assert (subject.cur_time != None)
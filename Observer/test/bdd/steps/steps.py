from lettuce import step
from observer import *
from nose.tools import assert_equal, assert_in

@step(u'Given I have a subject')
def given_i_have_a_subject(step):
  subject = Subject()

@step(u'When I subscribe to a subject')
def when_i_subscribe_to_a_subject(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.register_observer(user)
  assert_equal(len(subject.observers), 1)

@step(u'Then I will receive notifications')
def then_i_will_receive_notifications(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.register_observer(user)
  subject.notify_observers()
  assert (subject.cur_time != None)

@step(u'Given I subscribed to a subject')
def given_i_subscribed_to_a_subject(step):
  subject = Subject()

@step(u'When I unsubscribe a subject')
def when_i_unsubscribe_a_subject(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.unregister_observer(user)
  assert_equal (len(subject.observers), 0)

@step(u'Then I will not receive any notifications')
def then_i_will_not_receive_any_notifications(step):
  subject = Subject()
  user = USATimeObserver('user')
  subject.unregister_observer(user)
  assert (subject.cur_time == None)
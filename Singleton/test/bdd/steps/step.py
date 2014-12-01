from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp
from crawler import *
from crawler_app import *



@step(u'Given I enter the link url "([^"]*)"')
def given_i_enter_the_link_url_group1(step, url):
    dl = ImageDownloaderThread(threading.Thread)

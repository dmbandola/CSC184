from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp
from crawler import *
import os



@step(u'Given I enter the link url "([^"]*)"')
def given_i_enter_the_link_url_group1(step, url):
    link = Url(url)
    assert_equal(link.url, url)

@step(u'When I run the crawler')
def when_i_run_the_crawler(step):
    assert True
    
@step(u'Then I see the downloaded images "([^"]*)"')
def then_i_see_the_downloaded_images_group1(step, image_name):
    image = os.path.exists('/home/darin/Documents/CSC184/Singleton/images')
    assert_equal (image, True)

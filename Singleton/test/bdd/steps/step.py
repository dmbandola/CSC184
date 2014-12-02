from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp
from crawler import *
import os



@step(u'Given I enter the link url "([^"]*)"')
def given_i_enter_the_link_url_group1(step, url):
    link = Url(url)
    assert_equal(link.url, url)

@step(u'When I run the crawler and it sees the image "([^"]*)"')
def when_i_run_the_crawler_and_it_sees_the_image_group1(step, image_name):
    image = os.path.lexists("/home/darin/Documents/CSC184/Singleton/images/" + image_name)
    assert_equal(image, True)
    
@step(u'Then I see the downloaded image:')
def then_i_see_the_downloaded_image(step):
    assert True

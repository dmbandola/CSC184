Feature: An application that adds, removes and notifies the observers

	 As a user I wish to be able to subscribe and unsubscribe a subject so that i will be notified
	 
	
	Scenario: Get time formats for USA and EU
	Given I run the file
	When it finishes 
	Then I will see the following
	|Adding usa_time_observer								|
	|Observer usa_time_observer says: 2014-12-11 11:44AM    |
	|Adding eu_time_observer								|
	|Observer usa_time_observer says: 2014-12-11 11:44AM 	|
	|Observer eu_time_observer says: 2014-12-11 11:44    	|
	|Removing usa_time_observer							 	|
	|Observer eu_time_observer says: 2014-12-11 11:44	 	|
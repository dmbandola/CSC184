Feature: An application that adds, removes and notifies the observers

	 As a user I wish to be able to subscribe and unsubscribe a subject so that i will be notified
	 
	
	Scenario: Subscribe a subject
	Given I have a subject
	When I subscribe to a subject 
	Then I will receive notifications
	|Adding usa_time_observer								|
	|Observer usa_time_observer says: 2014-12-11 11:23:22AM |
	|Adding eu_time_observer								|
	|Observer usa_time_observer says: 2014-12-11 11:23:24AM |
	|Observer eu_time_observer says: 2014-12-11 11:23:24    |
	|Removing usa_time_observer								|
	|Observer eu_time_observer says: 2014-12-11 11:23:26	|



	Scenario: Unsubscribe a subject
	Given I subscribed to a subject
	When I unsubscribe a subject
	Then I will not receive any notifications
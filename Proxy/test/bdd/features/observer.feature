Feature: An application that adds, removes and notififies the observers

	 As a user I wish to be able to subscribe and unsubscribe a subject so that i will be notified
	 
	
	Scenario: Subscribe a subject
	Given I have a subject
	When I subscribe to a subject 
	Then I will receive notifications

	Scenario: Unsubscribe a subject
	Given I subscribed to a subject
	When I unsubscribe a subject
	Then I will not receive any notifications
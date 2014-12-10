Feature: An application that adds, removes and notififies the observers

	 As a user I wish to be able to subscribe and unsubscribe a subject so that i will be notified
	 
	
	Scenario: Subscribe a subject
	Given I have a subject
	When I subcribe in the subject 
	Then I will be notified

	Scenario: Unsubscribe a subject
	Given I have a subject where I subcribed
	When I unsubscribe in the subject
	Then I will not receive any notifications
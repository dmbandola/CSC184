Feature: An application that provides weather temperature in Celsius

		As a user I wish to get the weather temperature of a city so that I will be updated from time to time

		Scenario: Get the weather of a city
		Given I run the facade.py
		When it finishes
		Then I can see the temperature "<temperature>"
			Examples:
		    		|temperature|
		    		|3.59625	|

Feature: A tool that accesses web resources

				As a user I wish to be able to access web resources
				
				Scenario: Access web resources
				Given I have my localhost as my domain
				And I have the following resources "<resources>"
					|		resources	 		 |
					|www.facebook.com |
					|www.twitter.com		 |
				When I run the factory
				Then I can access resources

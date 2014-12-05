Feature: A tool that accesses web resources

				As a user I wish to be able to access web resources so that I can see the files
				
				Scenario: Access HTTP web sites
				Given I have my localhost as my domain
				When I run the factory
				Then I can access HTTP files

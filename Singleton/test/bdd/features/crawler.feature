Feature: An application that downloads images

        As a user I wish to be able to download images
        
        Scenario: Download images
        Given I enter the link url "http://localhost/ATRrepo/about.html" 
        When I run the crawler
        Then I see the downloaded images "<image_name>"
        	Examples:
        		|image_name|
        		|b.jpg			  |
        		|c.jpg			  |
        		|e.jpg			  |
        		

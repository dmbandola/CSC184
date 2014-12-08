Feature: A tool that accesses web resources

		As a user I wish to be able to access web resources so that I can see the files
				
		Scenario: Access HTTP web resources
		Given I have my localhost as my domain
		When I run the factory
		Then I can see the HTTP files "<files>"
			Examples:
				|files			 |
				|www.facebook.com|

		Scenario: Access FTP resources
		Given I have my locahost as my domain
		When I run the factory
		Then I can access the FTP files "<files>"
			Examples:
				|files                                                        |
				|CERT                                                         |
				|CTM -> development/CTM                                       |
				|CVSup -> development/CVSup                                   |
				|ERRATA                                                       |
				|ISO-IMAGES-amd64 -> releases/amd64/amd64/ISO-IMAGES          |
				|ISO-IMAGES-i386 -> releases/i386/i386/ISO-IMAGES             |
				|ISO-IMAGES-ia64 -> releases/ia64/ia64/ISO-IMAGES             |
				|ISO-IMAGES-pc98 -> releases/pc98/ISO-IMAGES                  |
				|ISO-IMAGES-powerpc -> releases/powerpc/powerpc/ISO-IMAGES    |
				|ISO-IMAGES-powerpc64 -> releases/powerpc/powerpc64/ISO-IMAGES|
				|ISO-IMAGES-sparc64 -> releases/sparc64/sparc64/ISO-IMAGES    |
				|README.TXT                                                   |
				|TIMESTAMP                                                    |
				|branches                                                     |
				|development                                                  |
				|dir.sizes                                                    |
				|distfiles -> ports/distfiles                                 |
				|doc                                                          |
				|ports                                                        |
				|releases                                                     |
				|snapshots                                                    |
				|tools                                                        |
				|updates                                                      |
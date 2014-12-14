Feature: An application that creates a file, deletes it, and undoes all deleted files

		As a user I wish to create a file so that I can delete it and Undo it after

		Scenario: Create a file, delete it, undo executed commands
		Given I have "command.py" in my directory
		And I run command.py
		When it finishes successfully
		Then I can see the result
			|result|
			|Creating file...|
			|Content of dir:  ['command.pyc', 'command.py']|
			|Content of dir:  ['command.pyc', 'command.py', 'test_file']|
			|File created.|
			|Deleting file...
			|Content of dir:  ['command.pyc', 'command.py', 'test_file']|
			|Content of dir:  ['.test_file', 'command.pyc', 'command.py']|
			|File deleted.|


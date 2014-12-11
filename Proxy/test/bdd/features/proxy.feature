Feature: An application that counts how many times an object is referenced to

		As a user I wish to know how many times an object is referenced to

		Scenario: Count object references
		Given an object is created
		When I run proxy.py
		Then I can see the following result
			|result|
			|Created new object|
			|Count of references =  1|
			|Using cached object|
			|Count of references =  2|
			|Using cached object|
			|Count of references =  3|
			|Called sort method with args:|
			|Deleting proxy2|
			|Deleted object. Count of objects =  2|
			|The other objects are deleted upon program termination|
			|Deleted object. Count of objects =  1|
			|Number of reference_count is 0. Deleting cached object... Deleted object. Count of objects =  0|
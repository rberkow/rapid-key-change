""" Task B

Algorithm:
	1. Retrieve counter value
	2. Check if (counter value)%(number of messages per key (i.e. 64 for FlexRay)) == 0
		If true:
		3. Retreive master key s0
		4. Set i = (counter value)/(number of messages per key)
		5. Compute new key (using Keccak hash of s0 concatenated with counter)
		6. Set new key based on result of 5.
"""
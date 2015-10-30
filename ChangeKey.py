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

import sys
import hashlib
if sys.version_info < (3,4):
    import sha3
import hmac


class ChangeKey:

    MESSAGES_PER_KEY = 32 # I just randomly chose this because I don't think Bittl specifies number for CAN messages
    MASTER_KEY = "98fkj998w8uhwluww0"
    
    counter = 0
    current_key = ""
    
    def __init__(self):
        self.current_key = self.MASTER_KEY

    def perform_change(self, keccak):
        self.counter = keccak.counter
        if self.counter % self.MESSAGES_PER_KEY is 0:
            i = self.counter / self.MESSAGES_PER_KEY
            self.current_key = self.compute_new_key(i)

    def compute_new_key(self, i):
        string_to_hash = self.MASTER_KEY + str(i)
        return hmac.new(self.current_key, string_to_hash, hashlib.sha3_256).digest()

""" Task A: validate 

Algorithm:
    1. Retreive key
    2. Compute MAC (hash of key and message - Keccak)
    3. Increment counter
"""

""" Task A: generate

Algorithm:
	1. Increment counter
	2. Retrieve key
	3. Compute MAC (hash of key with message content)
	4. Compare received MAC with computed MAC
"""


"""
    This module will provide an interface for the hmac function
    using keccak
"""

import sys
import hashlib
if sys.version_info < (3,4):
    import sha3
import hmac

class HmacKeccak:
    """A class to abstract MAC generation and validation"""
    
    counter =0 #the nonce
    key = 0 #symmetric key

    def __init__(self,key,ctr=None):
        """Create an instance of HMAC Keccak
            key: symmetric key
            ctr: initialVector (optional default =0)
        """
        if ctr is None:
            counter = 0
        else:
            counter =ctr

        self.key = key;

    
    def generateTag(self,message):
        """Generate a tag, increment a counter"""
        message = str(self.counter) + message;
        self.counter = self.counter + 1;
        return self.generateTagStateless(message)
    
    def generateTagStateless(self,message):
        """Generate a tag without incrementing the internal counter
            useful for verification of a MAC"""
        tag = hmac.new(key,message,hashlib.sha3_256).digest();
        return tag

    def verifyTag(self,message,tag):
        """Validate a MAC and update counter to synchronize"""
        message = str(self.counter) + message;
        if(self.verifyTagStateless(message,tag,self.counter)):
                self.counter = self.counter +1;
                return True
        else:
            return False

    def verifyTagStateless(self,message,tag):
        """Verify if a tag is authentic
            useful for checking
        """
        return self.generateTagStateless(message) == tag

def new(key,ctr=None):
    return HmacKeccak(key,ctr)

if(__name__ == '__main__'):
        """check if consistency requirement of MAC still holds"""
        key = "98fkj998w8uhwluww0"
        message = "ID=0,Data=fireOnEngine3"
        hk = new(key);

        tag=hk.generateTagStateless(message)
        consistent = hk.verifyTagStateless(message,tag)
        print "Consistent Stateless generate and verify: " + str(consistent) 
        
        tag =hk.generateTag(message)
        statefulMessage = str(0)+message;
        consistent = hk.verifyTagStateless(statefulMessage,tag)
        print "Consistent Stateful generate and verify: " + str(consistent) 


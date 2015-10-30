"""
    This module will provide an interface for the hmac function
    using keccak
"""

import sys
import hashlib
if sys.version_info < (3,4):
    import sha3
import hmac

def generateTag(key,message):
    tag = hmac.new(key,message,hashlib.sha3_256).digest();
    return tag

def verifyTag(key,message,tag):
    return generateTag(key,message) == tag

if(__name__ == '__main__'):
        """check if consistency requirement of MAC still holds"""
        key = tobyte("98fkj998w8uhwluww0")
        message = tobyte("ID=0,Data=fireOnEngine3")
        tag=generateTag(key,message)
        consistent = verifyTag(key,message,tag)
        print consistent

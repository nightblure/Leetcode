"""
Time Complexity: O(1). The lookup and update of the hashtable takes a constant time.

Space Complexity: O(M) where M is the size of all incoming messages. 
"""
class Logger(object):

    def __init__(self):
        self._msg_dict = {}
    
    def shouldPrintMessage(self, timestamp, message):
        if message not in self._msg_dict:
            # case 1). add the message to print
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
            return True
        else:
            return False

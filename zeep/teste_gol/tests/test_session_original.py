
import unittest

from base_test import BaseTest

class GolSessionTest(BaseTest):
            
    def test_create_session(self):
        ''' Test to create and destroy session
        '''        
        self.connect()
        self.api.create_session()
        self.assertTrue(getattr(self.api, "security_session"))
        self.assertTrue(self.api.security_session['Signature'])
        
        self.api.close_session()
        self.assertFalse(getattr(self.api, "security_session"))
            

if __name__ == '__main__':
    unittest.main()
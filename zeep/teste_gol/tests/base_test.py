from unittest import TestCase

from zeep.teste_gol.configs import configs
from zeep.teste_gol.configs import agency_info

#NOTE: Hack to import files from pure python_dir Lib
import os, sys
os.chdir('../teste_gol')
current_dir = os.getcwd()
sys.path.append(current_dir)

import teste_gol.utils as api_utils
from gol.utils import exceptions
from gol.api import GolAPI


class BaseTest(TestCase):
    
    def setUp(self):
        """ Initial Conf """
        self.configs = configs
        self.agency_info = agency_info
        self.api_class = GolAPI
        self.api_utils = api_utils
        self.exceptions = exceptions
        
        if hasattr(self, 'setUp_custom'):
            self.setUp_custom()
                
    def connect(self):
        self.api = self.api_class(
            self.configs.get('agent_name'),
            self.configs.get('password'),
            domain_code=configs.get('domain_code'),
            agency_code=configs.get('agency_code'),
            production=True
        )
        

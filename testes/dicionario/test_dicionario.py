from unittest import TestCase
import pandas as pd

class DictTest(TestCase):
    def test_read_json(self):
        x = pd.read_json("dicionario.json")
        print(x)
        assert isinstance(x, pd.DataFrame)

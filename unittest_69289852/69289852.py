import unittest

class MyCLS:
    def __init__(self):
        pass

    def set(self, key):
        if len(key) != 3:
            raise ValueError('invalid length for key: {key}'.format(key=key))
        if not key.isalnum():
            raise ValueError('key: {key} must be alphanumeric'.format(key=key))

class MyClsTest(unittest.TestCase):

    def test_key_length(self):
        m = MyCLS()
        self.assertRaises(ValueError, m.set, key='AAAA')

    def test_key_isalnum(self):
        m = MyCLS()
        self.assertRaises(ValueError, m.set, key='nds(')

    # def test_key_length(self):
    #     m = MyCLS()
    #     with self.assertRaises(ValueError):
    #         m.set('AAAA')

    # def test_key_isalnum(self):
    #     m = MyCLS()
    #     with self.assertRaises(ValueError):
    #         m.set('nds(')

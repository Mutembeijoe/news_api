import unittest
from .models import source

Source = source.Source

class SourceArticleTest(unittest.TestCase):
    '''
      Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','Abc News','A wordl class news channel')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
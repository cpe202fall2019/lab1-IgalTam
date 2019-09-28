import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        list_val = [1, 2, 3, 4, 5]
        self.assertEqual(max_list_iter(list_val), 5) # standard test
        list_val = [5, 199, 0]
        self.assertEqual(max_list_iter(list_val), 199) # value is in middle
        list_val = [57] 
        self.assertEqual(max_list_iter(list_val), 57) # one value
        list_val = [57, 2] 
        self.assertEqual(max_list_iter(list_val), 57) # value is at beginning
        list_val = [-100, -57, -5, -192] 
        self.assertEqual(max_list_iter(list_val), -5) # all values are negative

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # standard 
        self.assertEqual(reverse_rec([3]),[3]) # one value
        self.assertEqual(reverse_rec(["a", "b", "c", "d", "e"]),["e", "d", "c", "b", "a"]) # string list
        self.assertEqual(reverse_rec(["aasadfs", 4, "true", 1789]), [1789, "true", 4, "aasadfs"]) # multiple type list
        self.assertEqual(reverse_rec([]), []) # empty list

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # standard list finds value
        ist_val =[]
        low = None
        high = None
        self.assertRaises(ValueError) # empty list raises value error
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        list_val =[1,2,3,4,7,8,9,10]
        target = 5
        low = 0
        high = len(list_val)-1
        self.assertRaises(ValueError) # target is not found, raises value error
      
        '''list_val =[0,1,2,3,4,7,8,9,10]
        target = 10
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 10 )
        list_val =[0,1,2,3,4,7,8,9,10]
        target = 2
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2 )
        list_val =[0,1,2,3,4,7,8,9,10]
        target = 8
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 8 )
        list_val =[1,2,3,4,7,8,9,10]'''
        
        

if __name__ == "__main__":
        unittest.main()

    

from comparefilecontent import comparefilecontent
import unittest


class TestFolder(unittest.TestCase):

    def test_for_missing_filecontent(self):
        missingkeys = comparefilecontent(".env", "standard.env")
        self.assertEqual(len(missingkeys) , 0)
    
    def test_invalid_folder_path(self):
        compare_folder_contents("env", "standard.env")

    def test_invalid_standard_path(self):
        compare_folder_contents(".env", "standard.env")
        
 
     
if __name__ == "__main__":
    unittest.main()

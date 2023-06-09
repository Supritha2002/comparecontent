from compare_filecontent import comparefilecontent
import unittest


class TestFolder(unittest.TestCase):

    def test_for_no_missing_filecontent(self):
        missingkeys = comparefilecontent(".env", "standard.env")
        self.assertEqual(len(missingkeys), 0)
 
    def test_for_missing_filecontent(self):
        missingkeys = comparefilecontent(".env.common", "standard.env")
        self.assertTrue(len(missingkeys) > 0)
    
    def test_invalid_folder_path(self):
        self.assertRaises(SystemExit,comparefilecontent,"env", "standard.env")

    def test_invalid_standard_path(self):
        self.assertRaises(SystemExit,comparefilecontent,".env", "standards.env")

from comparefilecontent import comparefilecontent
import unittest


class TestFolder(unittest.TestCase):

    def test_for_missing_filecontent(self):
        missingkeys = comparefilecontent(".env", "standard.env")
        self.assertEqual(len(missingkeys) ,  0)


if __name__ == "__main__":
    unittest.main()

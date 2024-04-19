from list_item import ListItem
import unittest

class TestListItem(unittest.TestCase):

    def test_init(self):
        foobar = ListItem()
        self.assertEqual(foobar.title, "")
        self.assertFalse(foobar.complete)
    
    def test_toggle_complete(self):
        foobar = ListItem("Foo my bar")
        foobar.toggle_complete()
        self.assertTrue(foobar.complete)
    
    def test_title(self):
        foobar = ListItem("\nHello, World!\n")
        self.assertEqual(foobar.title, "Hello, World!")


if __name__ == '__main__':
    unittest.main()

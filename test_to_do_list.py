import unittest
from pathlib import Path
from to_do_list import ToDoList

class TestToDoList(unittest.TestCase):


    def test_init(self):
        list = ToDoList()
        self.assertEqual(list.items, [])


    def test_add_list_item(self):
        list = ToDoList()
        item = "Buy cereal."
        list.add_item(item)
        self.assertGreater(len(list.items), 0)

    def test_load_from_file(self):
        filepath = './saved_lists/test'
        list = ToDoList(filepath=filepath).load_from_file()

        self.assertEqual(list.items[0].title, 'Testing 1,2,3')
        self.assertEqual(list.items[1].title, 'Testing 4,5,6')
        self.assertEqual(list.items[2].title, 'Testing 7,8,9')
    

    def test_save(self):
        filepath = Path('./saved_lists/write_test')
        todo_list = ToDoList(filepath=filepath)
        items = ('Foo', 'Bar', 'Baz')

        for each_item in items: 
            todo_list.add_item(each_item)
        self.assertTrue(todo_list.save())

        with filepath.open('r') as file:
            for i, j in zip(items, file):
                self.assertEqual(i, j.strip())


if __name__ == "__main__":
    unittest.main()
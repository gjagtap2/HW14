from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object.add_book("Twilight",1)
        self.assertTrue(test_object.has_read("Twilight"), True)


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object.add_book("Twilight",2)
        test_object.add_book("Twilight",2)
        self.assertTrue(test_object.has_read("Twilight"), True)

                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        self.assertTrue(test_object.has_read("War of the Worlds"), True)
        

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.assertFalse((test_object.has_read("Harry Potter")), True)


    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object.add_book("Outliers",3)
        test_object.add_book("Jane Eyre",4)
        expected = 4 # War of the Worlds, Twilight, Outliers, Jane Eyre
        self.assertEqual(test_object.num_books_read(), expected)


    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object.add_book("Hunger Games",5)
        test_object.add_book("Catching Fire",4)
        test_object.add_book("Mockingbird",3)
        self.assertTrue(min(test_object.fav_books()['book_rating']>3))
                



if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com",
    "scifi")
    test_object.add_book("War of the Worlds", 4)
    unittest.main(verbosity=3)
    
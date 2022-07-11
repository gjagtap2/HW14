import pandas as pd

class BookLover():

    def __init__(self, name, email, fav_genre,
    num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list


    # METHOD 1
    def add_book(self, book_name, rating):

        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book],
            ignore_index=True)

            self.num_books += 1 # increment number of books

        else:
            print("This book already exists in the list!")


    # METHOD 2
    def has_read(self, book_name):      
        
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False


    # METHOD 3
    def num_books_read(self):
        
        return self.num_books


    # METHOD 4
    def fav_books(self):
        
        return self.book_list[self.book_list['book_rating']>3]
        
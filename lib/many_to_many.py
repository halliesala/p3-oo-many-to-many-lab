class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return list of contracts
        return [c for c in Contract.all if c.author == self]

    def books(self):
        # Return list of books
        return [c.book for c in Contract.all if c.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([c.royalties for c in Contract.all if c.author == self])

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda x: x.date)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, val):
        if isinstance(val, Author):
            self._author = val
        else:
            raise Exception("Author must be of class Author")
        
    @property
    def book(self):
        return self._book 
    
    @book.setter
    def book(self, val):
        if isinstance(val, Book):
            self._book = val
        else:
            raise Exception("Book must be of class Book")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, val):
        if isinstance(val, str):
            self._date = val
        else:
            raise Exception("Date must be a string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, val):
        if isinstance(val, int):
            self._royalties = val
        else:
            raise Exception("Royalties must be int")

# import ipdb; ipdb.set_trace()
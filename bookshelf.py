class Books:
    def __init__(self,name,author,PY,price):
        self.bookName = name
        self.booksAuthorsName = author
        self.booksPY = PY
        self.booksPrice = price
        
    def AddBook(self):
        print("Book's name: " + self.bookName)
        print("Book's author's name: " + self.booksAuthorsName)
        print("Book's publishing year: " + str(self.booksPY))
        print("Book's price: " + str(self.booksPrice))
        print("This book was published " + str(2022 - self.booksPY) + " years ago")
        print("The book has been added")
        
BookOne = Books("Harry Pottor and the Philosopher's Stone", "J. K. Rowling",1997,19.28)
BookOne.AddBook()

BookTwo = Books("Diary of a Wimpy Kid", "Jeff Kinney", 2017, 7.00)
BookTwo.AddBook()

BookThree = Books("All The Wrong Questions: Who Could That Be at This Hour?", "Lemmony Snicket", 2012, 12.99)
BookThree.AddBook()

BookFour = Books("Kiki's Delivery Service", "Eiko Kadono", 1985, 17.71)
BookFour.AddBook()

BookFive = Books("Howl's Moving Castle", "Diana Wynne Jones", 1986, 17.71)
BookFive.AddBook()

BookSix = Books("The Land of Stories: The Wishing Spell", "Chriss Colfer", 2017, 13.99)
BookSix.AddBook()

BookSeven = Books("Alice's Adventures in Wonderland", "Lewis Carroll", 1965, 5.95)
BookSeven.AddBook()

BookEight = Books("The Wonderful Wizard of Oz", "L. Frank Baum", 1900, 18.00)
BookEight.AddBook()

BookNine = Books("Around the World in Eighty Days", "Jules Verne", 1872, 7.99)
BookNine.AddBook()

BookTen = Books("The Chronicles of Narnia: The Magican's Nephew", "C. S. Lewis", 1970, 7.00)
BookTen.AddBook()
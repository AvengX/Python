class Book:
    count=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.review_list=[]

    def new_review(self):
        review=input("Enter your review :")
        self.review_list.append(review)
        Book.count+=1

    @classmethod
    def get_count(cls):
        print(f"Total number of reviews is {cls.count}")

    def display_reviews(self):
        print(f"Reviews for {self.title} :")
        for r in self.review_list:
            print(f"{r}")
        
book=Book("love","Ayush")
book.new_review()
book.new_review()
book.get_count()
book.display_reviews()




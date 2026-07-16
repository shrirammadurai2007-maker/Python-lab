class BookStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, book):
        if len(self.stack) == self.size:
            print("Stack is full")
        else:
            self.stack.append(book)
            print(book, "added to stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            book = self.stack.pop()
            print(book, "retrieved from stack")

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Books in stack:")
            for book in self.stack[::-1]:
                print(book)


size = int(input("Enter stack size: "))

books = BookStack(size)

n = int(input("Enter number of books: "))

for i in range(n):
    title = input("Enter book title: ")
    books.push(title)

print("\nStack after push operation:")
books.display()

print("\nPop operation:")
books.pop()

print("\nStack after pop operation:")
books.display()

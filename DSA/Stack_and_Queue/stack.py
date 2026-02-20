class stackemptyerror(Exception):
    print("Stack is empty")

class stackfullerror(Exception):
    print("Stack is full")

class stack:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.count = 0

    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == len(self.items)
    
    def push(self, x):
        if self.is_full():
            raise stackfullerror("Sorry, stack is full so you cant push any item.")
        self.items[self.count] = x
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise stackemptyerror("Sorry, stack is empty so you can't pop any item.")
        x = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return x
    
    def peek(self):
        if self.is_empty():
            raise stackemptyerror("Sorry, stack is empty so you cant peek.")
        return self.items[self.count - 1]

    def display(self):
        print(self.items)

if __name__ == "__main__":
    st = stack(15)

    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Quit")

        option = int(input("Enter your choice: "))

        if option == 1:
            x = int(input("Enter the element you want to push: "))
            st.push(x)

        elif option == 2:
            x = st.pop()
            print("Poped element is: ", x)

        elif option == 3:
            print("Element at the top is: ", st.peek())

        elif option == 4:
            print("Size of your stack is: ", st.size())
        
        elif option == 5:
            st.display()

        elif option == 6:
            break

        else:
            print("Please select the correct option.")
        print()
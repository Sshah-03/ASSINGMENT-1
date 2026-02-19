class Node:

    def __init__(self,value):
        self.info = value 
        self.link = None 
        
class SingleLinkedList:

    def __init__(self):
        self.start = None
     
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is :   ")
            p = self.start 
            while p is not None:
                print(p.info , " ", end='')
                p = p.link 
            print()

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        try:
            n = int(input("Enter the number of nodes: "))

            if n < 0:
                print("Number of nodes cannot be negative.")
                return

            if n == 0:
                print("List remains empty.")
                return

        except ValueError:
            print("Invalid input! Please enter an integer.")
            return

        for i in range(n):
            while True:
                try:
                    data = int(input("Enter the element to be inserted: "))
                    self.insert_at_end(data)
                    break
                except ValueError:
                    print("Invalid input! Please enter an integer.")

    def concatenate(self, list2):
        if self.start is None:
            self.start = list2.start
            return
            
        if list2.start is None:
            return

        p = self.start
        while p.link is not None:
            p = p.link

        p.link = list2.start
            
list1 = SingleLinkedList()
list2 = SingleLinkedList()
		
print("Enter first list :- ")
list1.create_list()
print("Enter second list :- ")
list2.create_list()

print("First "); list1.display_list()
print("Second "); list2.display_list()

list1.concatenate(list2)
print("Concatenated List is:2 "); list1.display_list()
class Node(object):

    def __init__(self,value):
        self.info = value 
        self.link = None
        
class CircularLinkedList(object):

    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print("List is empty\n")
            return
        p = self.last.link
        while True:
            print(p.info , " ",end='')
            p = p.link
            if  p == self.last.link:
                break
        print() 

    def insert_in_empty_list(self,data):
        temp = Node(data) 
        self.last = temp 
        self.last.link = self.last 
      
    def insert_at_end(self,data):
        temp = Node(data) 
        temp.link = self.last.link 
        self.last.link = temp 
        self.last = temp 
      
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
                    if self.last is None:
                        self.insert_in_empty_list(data)
                    else:
                        self.insert_at_end(data)
                    break
                except ValueError:
                    print("Invalid input! Please enter an integer.")
            
    def concatenate(self,list2):
        if self.last is None:
            self.last = list.last
            return
        if list2.last is None:
            return
        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last
        
list1 = CircularLinkedList()
list2 = CircularLinkedList()

print("Enter first list : ")
list1.create_list()

print("Enter second list : ")
list2.create_list()

print("First ")
list1.display_list()
print("Second ")
list2.display_list()

list1.concatenate(list2)
print("Concatenated list is: ")
list1.display_list()


                
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def deletef(self):
        if self.head==None:
            print('Empty')
        else:
            temp=self.head
            self.head=self.head.next
    def insert(self,value):
        Newnode=node(value)
        if self.head==None:
            self.head=Newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Newnode

    def view(self):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
    def deleteany(self,key):
        if self.head.data==key:
            self.head=self.head.next
        else:
            pre=None
            curr=self.head
            while True:
                if curr.data==key:
                    pre.next=curr.next
                    return
                pre=curr
                curr=curr.next
li=ll()
li.insert(10)
li.insert(20)
li.insert(30)
li.insert(40)
li.view()
print('\n')
li.deleteany(10)
li.view()
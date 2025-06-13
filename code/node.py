class Node:
    def __init__(self,val):
       self.data=val
       self.next=None
def createLinkedList(arr):
    head=None
    for val in arr:
        if (head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    return temp.next
arr=list(map(int,input().split()))
print(createLinkedList(arr))   
deleteHead(head)
def deleteHead(head):
    #code here
    n_head=head.next
    head.next=None
    return n_head
        


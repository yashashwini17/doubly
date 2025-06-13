class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createCLL(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            newNode.prev=temp
            temp.next=newNode
            temp=temp.next
    temp.next=head
    head.prev=temp
arr=list(map(int,input().split()))
createCLL(arr)

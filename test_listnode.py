class ListNode:
    def __init__(self, arr: list=None, val=0, next=None):
        if arr:
            a = self.__toListNode(arr)
            self.val = a.val
            self.next = a.next
            return
        self.val = val
        self.next = next

    def toList(self) -> list:
        out = []
        head = self
        while head:
            out.append(head.val)
            head = head.next
        return out

    def __str__(self):
        return str(self.toList())

    __repr__ = __str__

    def __toListNode(self, list: list):
        p = None
        while list:
            p = ListNode(val=list.pop(), next=p)
        return p



b = ListNode()
print(b.val)
print(b.next)


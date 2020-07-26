class LinkNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middle_linked_lst(self, head):
        list = [head]
        while list[-1].next:
            list.append(list[-1].next)

        return list[int(len(list)/2)].val

    def middle_linked_lst_2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(fast.val)
            print(slow.val)
        return slow.val

if __name__ == "__main__":
    list = [1,2,3,4,5]

    test = Solution()
    node_5 = LinkNode(5)
    node_4 = LinkNode(4, node_5)
    node_3 = LinkNode(3, node_4)
    node_2 = LinkNode(2, node_3)
    node_1 = LinkNode(1,node_2)

    print(test.middle_linked_lst_2(node_1))

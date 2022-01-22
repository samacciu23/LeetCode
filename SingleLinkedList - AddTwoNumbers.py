# source: https://leetcode.com/problems/add-two-numbers/

'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self, node):
        if self.val is None:
            print('list is empty')
        else:
            temp = node
            while temp is not None:
                print(self.val)
                temp = self.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry, result = 0, 0
        l3 = ListNode(0)
        temp = l3
        while l1 or l2 or carry:
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            result += carry
            temp.next = ListNode(result%10)
            carry = result // 10
            result = 0
            temp = temp.next
        return l3.next

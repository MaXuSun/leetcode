# 0001题, Hash
# 注意：python中，dict.get(key)(返回None)和dict[key](报错)区别
# 细节：num2index[num] = index要放在if后面，是处理[3,3]这种
def twoSum(nums,target):
    num2index={}
    for index,num in enumerate(nums):
        if num2index.get(num):
            return [num2index[num],index]
        num2index[num] = index

# 0002题，LinkList
# 注意：python中没有 do~while 结构，要想实现，需要用 while + break 实现
# 细节：在遍历链表时，有两种判断方法：p.next == None 和 p == None，配合while和do~while就有4种组合
#       当同时遍历两个链表时，我这里使用3个while太繁琐了，可以使用一个while(l1!=None||l2!=None)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p_l1 = l1
        p_l2 = l2
        len_arr = None
        output = ListNode(0)
        p_out = output
        flag = 0
        while True:
            sum_ = p_l1.val + p_l2.val + flag
            p_out.val = sum_ % 10
            flag = sum_ // 10
            p_l1 = p_l1.next
            p_l2 = p_l2.next
            if p_l1 == None or p_l2 == None:
                break
            p_out.next = ListNode(0)
            p_out = p_out.next
        print(output)
        while p_l1 != None:
            sum_ = p_l1.val + flag
            flag = sum_ // 10
            p_l1 = p_l1.next
            p_out.next = ListNode(sum_ % 10)
            p_out = p_out.next
        while p_l2 != None:
            sum_ = p_l2.val + flag
            flag = sum_ // 10
            p_l2 = p_l2.next
            p_out.next = ListNode(sum_ % 10)
            p_out = p_out.next
        if flag > 0:
            p_out.next = ListNode(flag)
        return output
            
            
            
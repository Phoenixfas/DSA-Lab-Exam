######### 1 ##########
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def revList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev




########## 2 ##########
def two_sum_ind(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None





######### 3 ###########
class CircularQueue:
    def __init__(self, k):
        self.queue = [0]*k
        self.head = self.tail = self.size = 0
        self.k = k

    def enqueue(self, value):
        if self.size == self.k:
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return False
        ret = self.queue[self.head]
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return ret

    def front(self):
        return -1 if self.size == 0 else self.queue[self.head]

    def rear(self):
        return -1 if self.size == 0 else self.queue[self.tail - 1]

    def isEmpty(self):
        return self.size == 0

######### 4 #########
def find_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


######## 5 ########
def rev_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s

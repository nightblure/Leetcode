# https://leetcode.com/problems/min-stack/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def display_func_value(f):
    def inner(*args, **kwargs):
        value = f(*args, **kwargs)
        print(value)
        return value
    return inner

def list_to_linked_list(values: list):
    head = ListNode(values[0])
    cur = head

    for value in values[1:]:
        cur.next = ListNode(value)
        cur = cur.next

    return head

def list_to_str(values, delimiter=None):
    if not delimiter:
        return f''.join([str(x) for x in values])
    return f'{delimiter}'.join([str(x) for x in values])
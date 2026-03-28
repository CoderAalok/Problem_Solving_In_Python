

# rem = 0
    # slow = head
    # while slow:
    #     rem = (rem*10) + slow.val % 10
    #     slow = slow.next
    # # x contains copy of rem
    # x = rem
    # new_rem = 0
    # while rem != 0:
    #     new_rem = (new_rem*10) + rem % 10
    #     rem //= 104

    # if new_rem == x:
    #     return True
    # return False

    # brute force
    # n = ""
    # slow = head
    # while slow:
    #     n += str(slow.val)
    #     slow = slow.next

    # n = int(n)
    # x = n
    # rem = 0
    # while n != 0:
    #     rem = (rem*10) + (n % 10)
    #     n //= 10
    
    # if rem == x:
    #     return True
    # return False
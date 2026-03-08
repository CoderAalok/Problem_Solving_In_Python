# stack: It is a container that contains or stored an elements.  In other hand, It is a way to stored values.
# stack -> LIFO: Last In First Out

# It's key property such that; always check top/peek element
# Push on top, pop on top element

# Generally, in python list behaves like stack.

# In stack, the brackets where at any position but when comes closing brackets
# it must matching it with most recent bracket.
# for example: stack = ["{", "("] and bracket comes in next iteration which is "}" 
# it must matching with "(" not "{". so at this condition false.

def balanced_order(brackets):
    matching = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    
    open = '([{'   
    close = '})]'
    stack = []
    
    for bracket in brackets:
        # Initillizing, check first in open
        if bracket in open:
            stack.append(bracket)
        
        # after check in open, check in close
        elif bracket in close:
            if not stack: #Ensure stack is empty
                return False
            
            elif stack[-1] == matching.get(bracket):
                stack.pop(-1)
    
            else:
                return False

    return not stack

brackets = "][]{})"
print(balanced_order(brackets))
    
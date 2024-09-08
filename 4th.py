def minimize_ticket_price(ticket_price, K):
    
    stack = []
    
 
    for digit in ticket_price:
       
        while K > 0 and stack and stack[-1] > digit:
            stack.pop()
            K -= 1
        
        stack.append(digit)
    
    while K > 0:
        stack.pop()
        K -= 1
    
    result = ''.join(stack).lstrip('0')   
    return result if result else "0"


ticket_price = input().strip()
K = int(input().strip())

print(minimize_ticket_price(ticket_price, K))

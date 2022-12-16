def tree(quantity):
    try:
         quantity=int(quantity)
    except:
         return "TYPE_ERROR"
    result = ''
    if quantity >= 3:
        quantity-=2
        for i in range(quantity+1):
            result=result+' '*(quantity-i)+'*'*(1+i*2)+' '*(quantity-i)+'\n'
        result+=' '*quantity+'|'+' '*quantity
        return result
    else:
        return "null"

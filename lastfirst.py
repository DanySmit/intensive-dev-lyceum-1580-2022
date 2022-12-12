def last(a):
    if type(a) == list and len(a) >0:
        return(a[len(a)-1])
    return "undefined"

def first(a):
    if type(a) == list and len(a) >0:
        return(a[0])
    return "undefined"

print(last([]))
print(last(['a','b','c']))
print(last([1,2,3,4]))
print(last('abc'))
print()
print(first([]))
print(first(['a','b','c']))
print(first([1,2,3,4]))
print(first('abc'))
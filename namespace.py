def namespace(s):
    dict = {}
    m=reversed(s.split('.'))
    for i in m:
        dict = {i : dict}
    return dict

print(namespace('a.b.c.d.e'))


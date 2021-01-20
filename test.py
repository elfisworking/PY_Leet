import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

# Use dict and setdefault    
print(d)
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)
print(g)


# Use dict
e = {}
for k, v in s:
    e[k] = v
print(e)

##list(d.items())
##list(g.items())
##list(e.items())
## Union Find Template
parent = [-1] * 100001
        
def find_parent(x):
    if parent[x] == -1:
        return x
    parent[x] = find_parent(parent[x])
    return parent [x]

def union(x,y):
    xs = find_parent(x)
    ys = find_parent(y)
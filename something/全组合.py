import itertools
l = ["a","b","c"]
ans = []
for i in range(1,len(l)+1):
    ans+=list(itertools.combinations(l,i))
print(ans)
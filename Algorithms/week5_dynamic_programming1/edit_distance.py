# Uses python3
def edit_distance(s, t):
    res = [[i for i in range(len(s)+1)]for j in range(len(t)+1)]
    for j in range(len(t)+1):
        res[j][0]=j
    for x in range(1,len(s)+1):
        for y in range(1,len(t)+1):
            insert = res[y][x-1]+1
            delete = res[y-1][x]+1
            mismatch = res[y-1][x-1]+1
            match = res[y-1][x-1]
            if s[x-1]==t[y-1]:
                res[y][x]=min(insert,delete,match)
            else:
                res[y][x]=min(insert,delete,mismatch)
    return res[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

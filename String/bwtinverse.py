# python3
import sys

def InverseBWT(bwt):
    last = [(val,idx) for idx,val in enumerate(bwt)]
    first = sorted(last)
    first_to_last = {f: l for f,l in zip(first,last)}
    
    next1 = first[0]
    result = ''
    for i in range(len(bwt)):
        result += next1[0]
        next1 = first_to_last[next1]
        
    return result[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
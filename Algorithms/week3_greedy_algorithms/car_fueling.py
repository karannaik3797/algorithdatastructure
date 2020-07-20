# python3
import sys


def compute_min_refills(distance, tank, stops):
    currefill = 0
    lastrefill = 0
    refill = 0
    stops.insert(0,0)
    stops.append(distance)
    if distance <tank:
        return 0
    while currefill < len(stops)-1 :
        lastrefill = currefill
        while currefill<=len(stops)-1 and stops[currefill+1] - stops[lastrefill]<=tank:
            currefill += 1
            if currefill == len(stops)-1:
                break
        if currefill == lastrefill:
            return -1
        if currefill < len(stops)-1:
            refill += 1
    return refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

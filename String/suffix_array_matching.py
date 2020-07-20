# python3
import sys
import operator

def find_occurrences(text, patterns):
    suffix_array = build_suffix_array(text)
    text = text +'$'
    ans = []
    for pattern in patterns:
       ans1 = (find_all_matches(suffix_array, text, pattern))    
       for ans2 in ans1:
           ans.append(ans2)
    ans = set(ans)   
    return ans

def find_all_matches(suffix_arr, text, query):
    def binary_search(lo, hi, op):
        m = len(query)
        while lo < hi:
            mid = (lo + hi) // 2
            suffix = suffix_arr[mid]
            if op(text[suffix:suffix+m], query):
                lo = mid + 1
            else:
                hi = mid

        return lo

    n = len(suffix_arr)
    start = binary_search(0, n, operator.lt)
    end = binary_search(start, n, operator.eq)

    return suffix_arr[start:end]
    
 
def sort_characters(text):
    order = [0] * len(text)
    char_set = sorted(set(text))
    count = [text.count(c) for c in char_set]

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i, c in reversed(list(enumerate(text))):
        count[char_set.index(c)] -= 1
        order[count[char_set.index(c)]] = i

    return order


def compute_char_classes(text, order):
    clss = [0] * len(text)

    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            clss[order[i]] = clss[order[i - 1]] + 1
        else:
            clss[order[i]] = clss[order[i - 1]]

    return clss


def sort_doubled(text, l, order, clss):
    len_text = len(text)
    count = [0] * len_text
    new_order = [0] * len_text

    for i in range(len_text):
        count[clss[i]] += 1
    for j in range(1, len_text):
        count[j] += count[j - 1]

    for i in range(len_text - 1, -1, -1):
        start = (order[i] - l + len_text) % len_text
        cl = clss[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order


def update_classes(new_order, clss, l):
    n = len(new_order)
    new_clss = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = cur + l, (prev + l) % n
        if clss[cur] != clss[prev] or clss[mid] != clss[mid_prev]:
            new_clss[cur] = new_clss[prev] + 1
        else:
            new_clss[cur] = new_clss[prev]

    return new_clss


def build_suffix_array(text):
    text1 = text + '$' 
    order = sort_characters(text1)
    clss = compute_char_classes(text1, order)
    length = 1
    len_text = len(text1)

    while length < len_text:
        order = sort_doubled(text1, length, order, clss)
        clss = update_classes(order, clss, length)
        length = length * 2

    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
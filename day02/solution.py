
def split_into_parts(s, num_parts):
    """Split string s into num_parts parts of as-equal-as-possible lengths."""
    parts = []
    length = len(s)
    part_len = length // num_parts
    extra = length % num_parts
    start = 0
    for j in range(num_parts):
        cur_len = part_len + (1 if j < extra else 0)
        parts.append(s[start:start+cur_len])
        start += cur_len
    return parts


def sol():
    f = open("./day02/dummy.txt")
    ranges = []
    for line in f.readlines():
        l = list(filter(lambda x: x != "", line.strip().split(',')))
        for rang in l:
            start = rang.split('-')[0]
            end = rang.split('-')[-1]
            ranges.append([start, end])

    print(ranges)

    res = 0

    for pair in ranges:
        start = int(pair[0])
        end = int(pair[1]) + 1


        for current_num in range(start, end):
            print(f"testing {current_num}")
            current_num_done = False
            s = str(current_num)
            length = len(s)
            num_parts = 2
            while num_parts <= length:
                if current_num_done:
                    break
                parts = split_into_parts(s, num_parts)
                if all(p == parts[0] for p in parts):
                    print(f"All parts for {s} are equal: {parts}")
                    res += int(s)
                    print(f"res {res}")
                    current_num_done = True
                num_parts += 1

    return res
    

print(sol())
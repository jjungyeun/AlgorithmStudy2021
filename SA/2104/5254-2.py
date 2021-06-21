def getNthPrefix(N, word):
    suffix_set = set()
    for i in range(len(word)):
        suffix_set.add(word[i:])
    suffix_set = sorted(suffix_set)

    prefixes = []
    cnt = 1
    for suf in suffix_set:
        for i in range(len(suf)):
            prefix = suf[:i+1]
            if prefix not in prefixes:
                if cnt == N:
                    return prefix
                prefixes.append(prefix)
                cnt += 1


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        tmp = input().split()
        N, word = int(tmp[0]), tmp[1]
        res = getNthPrefix(N, word)
        print("#%d %s %d" % (T, res[0], len(res)))
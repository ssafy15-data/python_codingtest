s = "aabb"
t = "ab"

idxs = []
prev_next_idx = 0
for t_char in t:
    for idx, s_char in enumerate(s[prev_next_idx:]):
        if t_char == s_char:
            prev_next_idx = (idx + prev_next_idx) + 1
            idxs.append(prev_next_idx - 1)
            break

def subseq(cur_idxs, pos):
    if pos == -1:
        return
    
    cur_idx = cur_idxs[pos]
    next_idx = cur_idxs[pos+1] if pos < len(t) - 1 else len(s)
    t_char = t[pos]

    subseq(cur_idxs, pos-1)
    for idx, s_char in enumerate(s[cur_idx+1:next_idx]):
        if s_char == t_char:
            answer[0] += 1
            cur_idxs[pos] = idx + cur_idx + 1
            subseq(cur_idxs, pos-1)
            cur_idxs[pos] = cur_idx

if len(idxs) == len(t):
    answer = [1]
    subseq(idxs, len(t)-1)
else:
    answer = [0]

print(answer[0])
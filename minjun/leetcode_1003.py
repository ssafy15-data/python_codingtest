class Solution:
    def isValid(self, s: str) -> bool:

        idxs = [i for i in range(len(s))]
        len_idxs = len(idxs)

        while True:
            removed = []
            for e_idx, idx in enumerate(idxs):
                if s[idx] == "a":
                    if e_idx+2 <= len_idxs -1:
                        if s[idxs[e_idx+1]] == "b" and s[idxs[e_idx+2]] == "c":
                            removed.append(idx)
                            removed.append(idxs[e_idx+1])
                            removed.append(idxs[e_idx+2])
            
            if len(removed) == 0:
                return False
            
            idxs = [idx for idx in idxs if not idx in removed]
            len_idxs = len(idxs)
            if len_idxs == 0:
                return True
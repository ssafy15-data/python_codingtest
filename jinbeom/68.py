class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret=[]
        start, length, tot_length=0,0,0
        for idx,word in enumerate(words):
            if len(word)+tot_length<=maxWidth:
                tot_length+=len(word)+1
                length+=len(word)
            else:
                tmp=''
                for i in range(start,idx-1):
                    if i<start+(maxWidth-length)%(idx-start-1):
                        tmp+=words[i]+' '*((maxWidth-length)//(idx-start-1)+1)
                    else:
                        tmp+=words[i]+' '*((maxWidth-length)//(idx-start-1))
                tmp+=words[idx-1]
                tmp+=' '*(maxWidth-len(tmp))
                ret.append(tmp)
                start=idx
                length,tot_length=len(word), len(word)+1
        ret.append(' '.join(words[start:])+' '*(maxWidth-tot_length+1))
        return ret
'''
Longest common subsequence problem (recursive solution)
'''
def lcs(text1, text2):
    lcs_length = 0
    if(len(text1)==0 or len(text2)==0):
        return 0
    if text1[0] == text2[0]:
        lcs_length = 1 + lcs(text1[1:], text2[1:])
        return lcs_length
    else:
        lcs_length = max(lcs(text1[1:], text2[:]), lcs(text1[:], text2[1:]))
        return lcs_length
    
print(lcs('acge', 'abcdefg'))

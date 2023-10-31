'''
Longest common subsequence problem (recursive solution)
'''
def lcs(text1, text2):
    table = [[0*i for i in range(len(text1)+1)] for j in range(len(text2)+1)]
    return lcs_helper(text1, text2, table)

def lcs_helper(text1, text2, table ):
    largest_length = 0
    if(len(text1)==0 or len(text2)==0):
        return 0
    if text1[0] == text2[0]:
        largest_length = 1 + lcs_helper(text1[1:], text2[1:])
        return largest_length
    else:
        largest_length = max(lcs_helper(text1[1:], text2[:]), lcs_helper(text1[:], text2[1:]))
        return largest_length
    
print(lcs_helper('acge', 'abcdefg'))

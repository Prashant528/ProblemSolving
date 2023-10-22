def longestCommonSubsequence(text1, text2, length=0):
    if len(text1)==0 or len(text2)==0:
        return 0

    if text1[0]==text2[0]:
        length = 1+ longestCommonSubsequence(text1[1:], text2[1:], length)

    else:
        #move one character ahead in text2
        length = longestCommonSubsequence(text1[:], text2[1:], length)
        #move one character ahead in text1
        length =longestCommonSubsequence(text1[1:], text2[:], length)
    return length

print(longestCommonSubsequence("abc", "def"))
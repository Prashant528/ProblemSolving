def editDistance(str1, str2, no_of_ops=0):
    #indices of the last element in both strings
    i = len(str1)-1
    j = len(str2)-1
    #base case:
    #if one of the strings is empty, no of inserts or deletes = no of remaining elements in another string
    if len(str1)==0 or len(str2)==0:
        return len(str1)+len(str2)
    #if both characters are same, we need no operation, do the same leaving the last element of both strings
    elif str1[i]==str2[j]:
        no_of_ops = editDistance(str1[0:i], str2[0:j])
    #if not same, we can take minimum of the operations required.
    # editDistance(str1[0:i-1], str2[0:j]) for delete
    # editDistance(str1[0:i], str2[0:j-1]) for insert
    # editDistance(str1[0:i-1], str2[0:i-1]) for replace
    else:
        no_of_ops = 1 + min(editDistance(str1[0:i], str2[:]), editDistance(str1[:], str2[0:j]), editDistance(str1[:i], str2[:j]))

    return no_of_ops
    
print(editDistance("ATCAT", "ATTATC"))
print(editDistance("APPLE", "BABBLE"))
print(editDistance("taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat", "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"))

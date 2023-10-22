def dna_match_topdown_helper(DNA1, DNA2,i,j):
    m=len(DNA1)
    n=len(DNA2)
    cache = [[0 for x in range(n+1)] for x in range(m+1)]
    if cache[i][j]!=0:
        return cache[i][j]
    if i==0 or j==0:
        return 0
    if DNA1[i]==DNA2[j]:
        cache[i][j]= 1+dna_match_topdown_helper(DNA1,DNA2,i-1,j-1)
    if DNA1[i] != DNA2[j]:
        return max(dna_match_topdown_helper(DNA1, DNA2, i , j - 1),dna_match_topdown_helper(DNA1,DNA2,i-1,j))

def dna_match_topdown(DNA1, DNA2):
    return dna_match_topdown_helper(DNA1,DNA2,len(DNA1)-1,len(DNA2)-1)


DNA1="ATAGTTCCGTCAAA"
DNA2="GTGTTCCCGTCAAA"
print(dna_match_topdown(DNA1,DNA2))
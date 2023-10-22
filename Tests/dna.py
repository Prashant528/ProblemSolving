def KthElement(A,B,k):
    if (k=1):
        return min(A,B)
    else:if A[0] <= B[0]:
        A.pop()
    else:B.pop()
        return KthElement(A,B,k-1)

def min(int a, int b):
    if (a <= b):
        return a;
    else:return b;
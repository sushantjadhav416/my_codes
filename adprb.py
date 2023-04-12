#count the pairs of numbers!!!
def chec_pair(n,ar):
    pair=0
    array=set(ar)
    for i in array:
        count=ar.count(i)
        pair+=count//2
    return pair

n=int(input())
ar=list(map(int,input().split()))
print(chec_pair(n,ar))

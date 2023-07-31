def sum(n):
    if n==1:
        sum=1
        return
    else:
        sum=n+sum(n-1)
        return 
sum(10)
def sum(n):
    return n * (n+1)//2

array = [2,4,6,8,9]

def sum_array(n):
    sum=0
    for i in range(len(n)):
        sum += int(n[i])
    print(f"The sum of this array {n} is: {sum}")

def sumn(n):
    if n <=0:
        return 0
    return n + sumn(n-1)
print("Sum of first n numbers (n=5):",sum(5))
sum_array(array)
print("recursive function n=5:",sumn(5))
def T(n):
    if n<=0:
        return
    else:
        T(n//2)
        T(n//2)
        print("Codingal")
        print(n//2)
        print(n//2)

T(7)
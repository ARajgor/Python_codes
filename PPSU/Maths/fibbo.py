# x=int(input("enter a value: "))
#
# def fibo(n):
#     ft = 0
#     lt = 1
#     if n == 1:
#         print(ft)
#     else:
#         print(ft)
#         print(lt)
#         for i in range(2,n):
#             s=ft+lt
#             ft=lt
#             lt=s
#             print(s)
#
# fibo(x)

#-----------recursion--------------#
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


print(Fibonacci(9))
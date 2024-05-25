def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
while True:
    num = int(input("أدخل عددًا لحساب المضروب: "))
    print(f"مضروب {num} هو {factorial(num)}")
    s = input("Do you want to continue? (y/n) ").lower()
    if s == "n":
        break
print("Hello from Mars")


def fact(i):
    if i == 1:
        return 1
    else:
        return i * fact(i - 1)


ans = fact(4)
print("Ans: ", ans)

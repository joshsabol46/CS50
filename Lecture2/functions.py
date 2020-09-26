def square(x):
    return x * x

# for i in range(10):
#     print(f"{i} squared is {square(i)}")
def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()
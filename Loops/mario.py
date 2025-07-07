def main():
    print_square(3)

def print_square(size):
    for i in range(3):
        for j in range(3):
            print("*", end=" ")
        print()
main()

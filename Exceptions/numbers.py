def main():
    while True:
        try : 
            x = int(input("What's x? "))
        except ValueError:
            print(f"x is not integer")
        else:
            print(f"x is {x}")
            break

if __name__ == "__main__":
    main()
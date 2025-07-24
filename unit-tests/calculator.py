def main():
    num = int(input("What's the value of num?"))
    print("num sqaured is ", square(num))

def square(num):
    return num * num

if __name__=='__main__':
    main()
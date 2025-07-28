def write_file():
    name = input("What's your name? ") 
    
    with open("names.txt", "a") as file:
        file.write(f"{name}")

def read_file():
    names = []

    with open("names.txt", "r") as file:
        for line in file:
            # print(line.rstrip())
            names.append(line.rstrip())
    
    for name in sorted(names):
        print(f"{name}")

def reading_csv_file():
    pass

def main():
    read_file() 

if __name__=="__main__":
    main()
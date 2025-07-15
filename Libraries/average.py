import statistics
import sys 

def witharguments():
    try: 
        print(f"Hello, My name is {sys.argv[1]}") 
    except IndexError:
        print("Too many arguments")
        sys.exit()

def main():
    print(f"{statistics.mean([90, 100, 40, 50])}")

    for arg in sys.argv[1:]:
        print(f"{arg}", end = " ")
    
    print()
    witharguments()

if __name__ == "__main__":
    main()
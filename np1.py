import numpy as np

def main():
    try:
        n = int(input("Enter n: "))
        arr = np.arange(n)
        arr[arr % 2 != 0] = -1
        print(arr)
    except ValueError:
        print("Enter int n")

if __name__ == "__main__":
    main()

def main():
    N = int(input().strip())
    if N == 1:
        print(0)
    else:
        print(2 * 3**(N-2))

if __name__ == "__main__":
    main()
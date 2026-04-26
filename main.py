def main():
    data = [10, 20, 30, 40, 50]
    it = iter(data)
    next(it)
    print(next(it))  # 20
    next(it)
    print(next(it))  # 40


if __name__ == "__main__":
    main()

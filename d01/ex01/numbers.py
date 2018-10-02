def display_num():
    with open("numbers.txt") as f:
        for line in f:
            for number in line.split(","):
                print(number.strip())  

if __name__ == '__main__':
    display_num()

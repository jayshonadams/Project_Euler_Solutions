
if __name__ == "__main__":
    total = 0

    for x in range(1,1000):
        if x % 5 == 0 or x % 3 == 0:
            total += x
    
    print(total)

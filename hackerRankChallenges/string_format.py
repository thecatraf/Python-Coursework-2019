def print_formatted(n):
    # your code goes here
    width = len(bin(n+1)[2:]) 
    for i in range(n):
        i += 1
        octal = oct(i)[2:]
        hx = hex(i)[2:].upper()
        binary = bin(i)[2:]
        i = str(i)
        print(i.rjust(width), end=' ')
        print(octal.rjust(width), end=' ')
        print(hx.rjust(width), end=' ')
        print(binary.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)





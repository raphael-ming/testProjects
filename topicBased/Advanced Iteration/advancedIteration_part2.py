

def print_pattern1():
    n = 5
    for i in range(1, n+1, 1):
        for j in range(1, i+1):
            print (j, end=" ")
        print("")
    print ("")

print_pattern1() #function for pattern 1

def print_pattern2():
    n = 10
    for i in range(0, n+1, 1):
        for j in range(n-i, 0, -1):
            print(j, end = ' ')
        print("")
    print("")

print_pattern2() #function for pattern 2

def search_prime_numbers():
    start = 10
    end = 50

    print(f'The prime numbers between {start} and {end} is:')
    for x in range(start, end+1):
        for y in range(2, x): #2 because everything modulus 1 == 0
            if x%y == 0:
                break #break loop if definite not prime

        else:
            print(x)

    print("")

search_prime_numbers() #function for search prime numbers between two points
#1. bikin variabel start = angka bawah
#2. bikin variabel end = angka atas
#misal start = 10, end = 50 -> berarti programnya cari angka prima dari 10-50

#bikin for buat cek satu-satu setiap angka dari angka 10-50
#cek angkanya, angka prima atau bukan? -> cuman bisa dibagi angkanya sendiri

def star_pattern():
    max = 5
    for x in range(1, max+1):
        for y in range(1, x+1):
            print("*", end = ' ') 
        print("")
    
    for x in range(1, max):
        for y in range(max-x, 0, -1):
            print("*", end = ' ')
        print("")
    print("")

star_pattern() #function for star_pattern

#Program to count, for example: user_input = 10
#count the result of: 1+2+3+4+5+..+10
def arithmetics():
    while True:
        user_input = input("")

        try:
            user_input = int(user_input)
            break

        except:
            pass

    sum = 0
    for x in range(1,user_input+1,1):
        sum += x
    print (sum)

#arithmetics() #function for arithmetics

def fibbonaci():
    n = 10
    i = 0
    fibbonaci_sequence = [0,1]
    while len(fibbonaci_sequence) <= n:
        nextNumber = fibbonaci_sequence[i] + fibbonaci_sequence[i+1]
        fibbonaci_sequence.append(nextNumber)
        i += 1
    print(fibbonaci_sequence)
    print("")

fibbonaci() #function for fibbonaci

def find_factorial():
    x = number = 5
    for y in range(number-1, 0, -1):
        x *= y
    print (x)

find_factorial() #function for find_factorial

def find_cube():
    numbers = 10
    for x in range(1, numbers+1, 1):
        print(f'The number is {x}, and the cube is: {x*x*x}')

find_cube()
n = int (input("Введите год: "))

def is_year_leap(n):
    if(n % 4 == 0):
        print(True)
    else: 
        print(False)

is_year_leap(n)
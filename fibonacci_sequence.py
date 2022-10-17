"""
Fibonacci Sequence
Enter a number and have the program generate
the Fibonacci sequence to that number or to the Nth number.
"""


def fib_seq(nth_num: int) -> list:  # function annotations covered in PEP 3107
    """
    Function to find all fibonacci numbers to nth number and return list of numbers.
    Formula: Fn = Fn-1 + Fn-2, where n > 1
    """
    first_num = 0
    next_num = 1
    list_fib_seq = [first_num, next_num]
    for nums in range(1, nth_num):
        next_num += first_num
        first_num = next_num - first_num
        list_fib_seq.append(next_num)
        nums += 1
    return list_fib_seq


def fib_seq_nth_num() -> int:
    """
    Function to ask user for non-negative integer greater then 1
    """
    while True:
        try:
            nth_num = int(input("""
            \rEnter a number and have the program generate 
            \rthe Fibonacci sequence to that number or to the Nth number.
            \rPlease enter a integer number greater then 1. Limit is 100.
            \rYour number: """))
            if 1 < nth_num <= 100:
                return nth_num
            print(
                "\nError. The number does not meet the conditions. ")
            continue
        except ValueError:
            print("\nError. Please use integer numbers")
            continue


while True:
    try:
        print("""\nPlease choose:
        \r1. Get Fibonacci number of nth number.
        \r2. Get Fibonacci sequence to nth number.
        \r3. Quit.
        """)
        num_choice = int(input("Your choice: "))
        if num_choice == 1:
            print(fib_seq(fib_seq_nth_num())[-1])
        elif num_choice == 2:
            print(fib_seq(fib_seq_nth_num()))
        elif num_choice == 3:
            break
        else:
            print("\nYour choice isn't in the list")
    except ValueError:
        print("\nError. Please use numbers from that list of choice")
        continue

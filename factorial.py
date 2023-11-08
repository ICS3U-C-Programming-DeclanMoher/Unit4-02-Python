#!/usr/bin/env python3
# Created by: Declan.Moher
# Created on: Nov. 8, 2023
# This program checks factorials of user_number


def main():
    user_number_str = input("Enter a positive number")
    try:
        user_number = int(user_number_str)
    except ValueError:
        print("Invalid Input")
    else:
        if user_number >= 0:
            count = 0
            factorial = 1
            while True:
                count = count + 1
                factorial = factorial * count
                if count >= user_number:
                    break
            print(f"{factorial}")
        else:
            print(f"{user_number}is not a positive number")


if __name__ == "__main__":
    main()

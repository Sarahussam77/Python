#Q1
# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()

# def reduce_adjacent_elements(user_list):
#     reduced_list = [user_list[0]]  
#     for i in range(1, len(user_list)):
#         if user_list[i] != user_list[i-1]:  
#             reduced_list.append(user_list[i])  
#     print(reduced_list)

# reduce_adjacent_elements(user_list)


#Q2
# string1=input("Enter the first string")
# string2=input("Enter the second string")
# def front_back_combine(a, b):
#     if len(a)%2==0:
#         a_front = a[:(len(a)//2)]
#         a_back = a[(len(a)-len(a_front)):]
#     else:
#         a_front = a[:((len(a)+1)//2)]
#         a_back = a[((len(a)+1)-len(a_front)):]
#     if len(b)%2==0:
#         b_front = b[:(len(b)//2)]
#         b_back = b[(len(b)-len(b_front)):]
#     else:
#         b_front = b[:((len(b)+1)//2)]
#         b_back = b[((len(b)+1)-len(b_front)):]
#     print((a_front+b_front)+(a_back+b_back))
   

# front_back_combine(string1,string2)

#Q3
# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# def all_different(seq):
#     return len(seq) == len(set(seq))

# print(all_different(user_list))

#Q4
# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# def bubble_sort(list):
#     n = len(list)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(1, n):
#             if list[i-1] > list[i]:
#                 list[i-1], list[i] = list[i], list[i-1]
#                 swapped = True
#         n -= 1
#     print(list)

# bubble_sort(user_list)

#Q5
# import random


# def play_game(tries=10):
#     random_num = random.randint(1, 100)
#     guessed_nums = set()

#     while tries > 0:
#         user_num = input(
#             f"Guess the number (1-100). You have {tries} tries left: ")

#         # Check if user input is out of range
#         if not user_num.isdigit() or int(user_num) < 1 or int(user_num) > 100:
#             print("Invalid input. Please enter a number between 1 and 100.")
#             continue

#         user_num = int(user_num)

#         # Check if user has already guessed the number
#         if user_num in guessed_nums:
#             print("You already guessed that number. Try again.")
#             continue

#         guessed_nums.add(user_num)

#         if user_num == random_num:
#             print("Congratulations! You guessed the number!")
#             print("You have {} tries left. Guess a new number!".format(
#                 tries))
#             return
#         if user_num < random_num:
#             print("Your guess is Low..")
#         else:
#             print("Your guess is high..")

#         tries -= 1

#     print(f"Sorry, you lost. The number was {random_num}.")
   


# play_game()



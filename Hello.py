# msg = 'Hello world'
# print(msg)

# import random

# r1 = ["Gary",
#         "Jim",
#         "Mike",
#         "Dave"]

# r2 = ["Code.",
#           "Hike.",
#           "play video games.",
#           "listen to music."]

# random_r1 = random.choice(r1)
# random_r2 = random.choice(r2)
# #random_person2 = random.choice(people)

# print(f"Hello my name is {random_r1} and I like to {random_r2}")

# print("Winter is coming")
# print("You know nothing.")

# a_list = []
# a_tuple = (1, "one")
# a_list = a_list + [a_tuple]

# print(a_list)

# a_number = 1
# b_number = 2
# # swap 
# b_number, a_number = a_number, b_number
# print(a_number, b_number)

# fizz_buzz activity

#part 1
# def fizz_buzz():
#       print(0)
#       for i in range(1, 16):
#           if i % 3 == 0 and i % 5 == 0:
#             print('fizzBuzz')
#           elif i % 3 == 0:
#             print('fizz')
#           elif i % 5 == 0:
#             print('buzz')
#           else:
#             print(i)
# fizz_buzz()

# part 2
# def fizz_buzz(i = 15):
#       x = 1
#       print(0)
#       while x <= i:
#         if x % 3 == 0 and x % 5 == 0:
#             print('fizzBuzz')
#         elif x % 3 == 0:
#             print('fizz')
#         elif x % 5 == 0:
#             print('buzz')
#         else:
#             print(x)
#         x += 1    
# fizz_buzz()

#part 3 
# def fizz_buzz(i = 15):
#         x = 0
#         list = []
#         list.append(tuple((x, str(x))))
#         while x < i + 1:
#                 # print(x) 
#             if x % 3 == 0 and x % 5 == 0:
#                 list.append(tuple((x,'fizzBuzz')))
#                 # print('fizzBuzz')
#             elif x % 3 == 0:
#                 list.append(tuple((x,'fizz')))
#                 # print('fizz')
#             elif x % 5 == 0:
#                 list.append(tuple((x,'buzz')))
#                 # print('buzz')
#             else:
#                 list.append(tuple((x, str(x)))) 
#                 # print(x)
#             x += 1
#         print(list)
# fizz_buzz()

# def fizz_buzz(fizz=3, buzz= 5, up_to_number= 15):
#         x = 0
#         result = []
#         while x < up_to_number + 1:
#             if x % 3 == 0 and x % 5 == 0:
            
#             elif x % 3 == 0:
                
#             elif x % 5 == 0:
        
#             else:
def fizz_buzz(fizz=3,buzz=5,up_to=15):
        x = 1;
        result =[]
        while x < up_to:
                
                string = ''
                if x%fizz==0:
                        string += 'Fizz'
                if x%buzz==0:
                        string += 'Buzz'
                result.append((x,(str(x) if string == "" else string)))
                x+=1
        return  result
print(fizz_buzz(3,5,100))       

# x = count i = up_to_number
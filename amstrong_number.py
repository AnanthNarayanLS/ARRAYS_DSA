

user_input = int(input("enter a number : "))
temp_store = 0
for i in str(user_input):
    temp_store += int(i)**3
if temp_store == user_input:
    print("its an amstrong number ")
else:
    print("it's not an amstrong nunmber")
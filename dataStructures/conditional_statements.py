# #basic syntax for if statement
grade = 90
if grade >= 90:
    print("your grade is A")
elif grade >= 80:
    print("your grade is B")
elif grade >= 70:
    print("your grade is C")
elif grade >= 60:
    print("your grade is D")
else:
    print("you failed in your exams")

# for loop

for number in range(1, 6):
    print(f"number {number}")

# while loop - it performs a list of instructions as long as the condition is true
#example 
count = 1
while count <= 5:
    print(f"count {count}")
    count +=1

#example of loop controls: Break and continue

for number in range(1, 10):
    if number == 5:
        print("breaking loop at 5")
        break
    elif number % 2 == 0:
        print(f"skipping number: {number} since its even")
        continue
    print(f"processing number {number}")

# nested loops 
#example 
for i in range(1, 4):
    for j in range(1, 4):
        print(f"outer loop{i} inner loop j{j}")

list1 = [1, 2, 3,4,5,6,7,8,9]

list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in list1:
    for j in list2:
        print(f"outer list list1 {i} iner list list2 {j}")
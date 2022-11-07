text = """Hello minions welcome to your worst nightmare!
At Starbucks! Filled with people. 
Then suddenly everyone turns into monsters
THe staff room is on your left but you to..."""

text2 = """Good job.
Imagine you forgot your password, that would have been an ugly ending.
All of this is happening because then Tentacle monster has been released from the drift!"""

print(text)

#password

password = "0174"
usrAttempts = 3


while usrAttempts > 0:
    guess = input("type password")
    if guess == password:
        print("door opened")
        break
    usrAttempts -= 1
else:
    print("not attempts left")

print(text2)




#numbers

numbers =[2, 3, 5, 7, 66, 89, 134]
output = []
player = input()

if not player.isdigit():
    print("that is not a number")
    exit()

player = int(player)

for i in numbers:
    if i < player:
        output.append(i)
print(output)



#activity 3

word = "python"
no = ""

for letter in word:
    if letter != "t":
       no += letter

print(no)




#activity 2

theString = "hello world"
numLs = int(0)

for letter in theString:
    if letter.lower() == "l":
        numLs += 1

print("the number of L's in the string is {}". format(numLs))



#activity 1

inventory =["knife","dagger","tentacle sweeper" ]

print("you have defeat the tentacle monster")
print(inventory)

choice = input("choose your weapon! ").lower()

if choice not in inventory:
    print("dead")
    exit()

else:print("you reach down and pull a % from your bag" % choice)

if "tentacle sweeper" in choice:
    print("you have picked the right weapon")

elif "knife" or "dagger" in choice:
    print("the weapon is weak, the monster killed you!")

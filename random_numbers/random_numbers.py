import random 

# Function to generate 
# and append them 
# start = starting range, 
# end = ending range 
# num = number of 
# elements needs to be appended 
def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
        return res 

num = int(input("Enter a Number: "))
start = int(input("Enter a Start Number: "))
end = int(input("Enter a End Number: "))
print(Rand(start, end, num)) 

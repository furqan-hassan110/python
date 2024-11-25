##1. Declare a variable city and assign it the name of your city. Create another variable population and assign it a number. Print a sentence using these variables, such as "The population of Paris is 2,140,526."

city = "karachi"
population = 2140526
print(f"The population of {city} is {population}.")



##2. Take two numbers as input from the user and calculate their sum. Print the result.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
sum_result = number1 + number2
print(sum_result)


##3. Create a list of four colors and print the list.

colors = ["Red", "Black", "Purple", "Yellow"]
print(colors)


##4. From the list of colors, print the second and fourth color using their index positions.


print(f"The second color is: {colors[1]}")
print(f"The fourth color is: {colors[3]}")

##5. Add a new color to the list and print the updated list.

colors.append("Blue")
print(colors)

##6. Write a program to iterate through the list of colors using a for loop and print each color.

for colors in colors:
    print(colors)


##7. Use a for loop with range() to print numbers from 1 to 20

for i in range(1,21):
    print(i)


##8. Write a program to print the multiplication table of 5 up to 10 using a for loop

for i in range(1,11):
    print(f"5 X {i} = {i*5}")
 

##9. Create a list of all four numbers. Use a for loop to calculate and print the sum of all numbers in the list.

numbers=[1,1,1,1]
list_sum=0
for i in numbers:
    list_sum+=i
print(list_sum)

#10. Write a basic code that can calculate area of triangle. The code must take input values from user. Also decide the correct type of your input variables.


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")

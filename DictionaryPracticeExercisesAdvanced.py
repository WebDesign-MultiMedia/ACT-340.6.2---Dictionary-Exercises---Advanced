#Problem 1
print("Problem 1")
# Add the following key/value pair to the dictionary below. 
# "oceans": ["Pacific", "Atlantic", "Indian", "Arctic"]
geography = {
    "continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"]}
geography["oceans"] = ["Pacific", "Atlantic", "Indian", "Arctic"]
print(geography)
print('')

#Problem 2
print("Problem 2")
# Use the Dic below
# Change the value for the height ket to 72 inches
patient = {
    "name" : "John Doe",
    "age" : 25,
    "height" : 64,
    "symptoms" : "cough"
    }
print(patient, " - Before [height]")
patient["height"] = 72
print(patient, " - After [height]")
print('')

#Problem 3
print("Problem 3")
# Use a class method to generate a list of tuples that
# contain the key/value pairs.
print(patient.items(), " - Items")
print('')

#Problem 4
print("Problem 4")
# Use a class method to print the value of "name"
print(patient.keys(), " - Keys", " - keys")
print('')

#Problem 5
print("Problem 5")
# Use a Class method to look for the key "weight", and
# supply a default arguement of 150 if the value is not found
print(patient.get("weight", 150), " - Get")
print('')

#Problem 6
print("Problem 6")
# Use a Class method to 
# remove everything from the dictionary
print(patient.clear(), " - Clear")
print('')

#Problem 7
print("Problem 7")
# Use a for loop to move through the dictionary.
# If the value is above 2000, add the value to a new list minus 500
# Example: If the value is 2500, 2000 would be added to the new list
stock_qty = {"cookies": 3200, "bread": 500, "crackers": 52000, "chips": 2000}
print(stock_qty, " - Before")
for key, value in stock_qty.items():
    if value > 200 :
        value = value - 500
        print(key, value)
print('')

#Problem 8
print("Problem 8")
# Loop through the list 
# Create a dictionary to keep track of how many times a number appears in a list
# Print the final dictionary

# Things to consider:
### How to check if an integer already exists in the new dictionary
### What is the first value when the key gets added to the dictionary?
### How to increase the value of each key on each iteration of the loop?

list= [10, 9, 88, 20, 9, 20, 22, 101, 68, 10, 108, 33, 9, 53]
for key, value in enumerate(list):
    x = list.count(value)
    print(value, "Appears", x, "times" )
    print('')
list.sort()
print(list , " - final and sorted")

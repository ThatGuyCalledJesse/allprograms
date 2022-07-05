print("Enter \"20 kilometers\" or \"20 km\" to convert to mile, and \"20 mile\" to convert to miles.")
string = input("Enter a distance: ").lower()
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
stringSplitted = list(string)

distance = ""

for i in stringSplitted:
    for number in numbers:
        if i == number:
            distance += i

distance = int(distance)

def kilometersToMiles(kilometers: float):
    return kilometers * 0.621371192
def milesToKilometers(miles: float):
    return miles * 1.609344

# Driver code
if "kilometers" in string or "kilometer" in string or "km" in string:
    print(f"{kilometersToMiles(distance)} mile")
elif "miles" in string or "mile" in string:
    print(f"{milesToKilometers(distance)} kilometer")
else:
    raise Exception("You didn't enter a valid distance! Please try again.")
print("Enter the hour in 24 hour clock (0 to 23)")
hour = int(input())

if hour < 8:
    print("Too early!")
elif hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
elif hour == 18:
    print("Dinner time!")
elif hour < 24:
    print("Good night!")
else:
    print("Sorry, I don’t recognise that!")
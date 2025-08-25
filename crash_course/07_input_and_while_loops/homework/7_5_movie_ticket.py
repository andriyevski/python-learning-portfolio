# # Homework from file tasks/7_5_movie_ticket.md
# ## Task ## : 7.5
# # 7_5_movie_ticket
while True:
    try:
        age = int(input("\nWrite your age to take ticket to movie (or type 0 to exit): "))

        if age == 0:
            print("Goodbye! 🎬")
            break
        elif age < 3:
            print("You can enter cinema free!")
        elif age <= 12:
            print("Your ticket price is $10")
        else:
            print("Your ticket price is $15")
    except ValueError:
        print("Please enter a valid number.")

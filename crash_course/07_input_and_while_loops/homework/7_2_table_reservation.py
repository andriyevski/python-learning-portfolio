seats = input("How many seats you want to book ? ")
seats = int(seats)

if seats > 8:
    print(f"\nYou must wait for book, because {seats} is too much right now!")
else:
    print(f"\nYour table on {seats} person is ready!")

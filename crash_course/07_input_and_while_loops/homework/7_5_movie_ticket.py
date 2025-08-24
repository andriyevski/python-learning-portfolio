# # Homework from file tasks/7_5_movie_ticket.md
# ## Task ## : 7.5
# # 7_5_movie_ticket
while True:
    age_input = input("\nВведите ваш возраст для входа в кино (или 'выход' для завершения): ")

    if age_input.lower() == 'выход':
        print("Спасибо за использование системы! До встречи в кинотеатре 🎬")
        break

    try:
        age = int(age_input)
        if age < 3:
            print("Билет бесплатный!")
        elif age <= 12:
            print("Цена билета: $10")
        else:
            print("Цена билета: $15")
    except ValueError:
        print("Пожалуйста, введите корректный возраст или 'выход'.")

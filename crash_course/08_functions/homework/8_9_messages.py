# Homework from file tasks/8_9_messages.md
## Task ## : 8.9
# 8_9_messages
def show_messages(messages):
    for message in messages:
        print(f"Message: {message}")

def main():
    messages = ('hello call me later!','Whats up dude, call me!','Where are you , i wait in bar!')
    show_messages(messages)


if __name__ == '__main__':
    main()

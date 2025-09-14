# Homework from file tasks/8_10_Sending_messages.md
## Task ## : 8.10
# 8_10_Sending_messages
def send_messages(messages, sent_messages):
    print("\nSend Message:")
    for message in messages:
        print(f"Message: {message}")
        sent_messages.append(message)

def show_sent_messages(sent_messages):
    print("\nSent messages:")
    for message in sent_messages:
        print(f"- {message}")

def main():
    messages = ('hello call me later!','Whats up dude, call me!','Where are you , i wait in bar!')
    sent_messages = []
    send_messages(messages, sent_messages)
    show_sent_messages(sent_messages)


if __name__ == '__main__':
    main()

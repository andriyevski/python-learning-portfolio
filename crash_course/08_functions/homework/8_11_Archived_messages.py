# Homework from file tasks/8_11_Archived_messages.md
## Task ## : 8.11
# 8_11_Archived_messages
def send_messages(messages, sent_messages):
    print("\nSend Message:")
    for message in messages:
        print(f"Message: {message}")
        sent_messages.append(message)

def show_sent_messages(sent_messages):
    print("\nSent messages:")
    for message in sent_messages:
        print(f"- {message}")

def check_diff_messages(messages, sent_messages):
    print("\nCheck if all list is the same:")
    for message in sent_messages:
        if message in messages:
            print(f"\n==>Yes ({message}) in 'messages'!")
        else:
            print(f"\n==>No ({message})s not in 'sent messages'")


def main():
    messages = ('hello call me later!','Whats up dude, call me!','Where are you , i wait in bar!')
    sent_messages = []
    send_messages(messages[:], sent_messages)
    show_sent_messages(sent_messages)
    check_diff_messages(messages[:],sent_messages)

if __name__ == '__main__':
    main()

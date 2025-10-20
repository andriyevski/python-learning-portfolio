# filename = 'alice.txt'
#
# with open(filename, encoding = 'utf-8') as f:
#     contents = f.read()



try:
    filename = 'alice.txt'

    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file { filename } does not exist.")
else:
    # Count words in file
    words = contents.split()

    #if we wand see that words in some UX
    num_count = 0
    for word in words:
        num_count += 1
        print(f"# {num_count} -> {word}")

    # count all words
    num_words = len(words)
    print(f"The file { filename } has about { num_words } words.")

# file read and write (txt)

# user_input = input("Enter some text: ")

# write to file
# with open("notes.txt", "w") as file:
#     file.write(user_input)
# print("Text written to notes.txt")

# read from file
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print("Content read from notes.txt: ")
#     print(content)


chatgpt_input = input("type here chatgpt: ")

with open("chatgpt_notes.txt", "w") as file:
    file.write(chatgpt_input)


with open("chatgpt_notes.txt", "r") as file:
    content = file.read()
    print("Text from chatgpt_notes.txt: ")
    print(content)
print("Insert your links below. Press Enter on an empty line when you are done:")

links = []
while True:
    link = input("> ")
    if link == "":
        break
    links.append(link)

with open("links.txt", "w") as f:
    for link in links:
        print(link, file=f)



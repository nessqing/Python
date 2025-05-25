### Copy file for several times
### /to do gui with "tkinter"
with open("11404.csv", "rb") as file:
    data = file.read()
    for i in range(1,11):
        with open(f"haru{i}.csv", "wb") as file1:
            file1.write(data)
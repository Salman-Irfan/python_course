import os

# print current working directory
print(os.getcwd())

# making a new folder
if os.path.exists("notes"):
    print("folder already exists")
else:
    os.mkdir("notes")

# making a new file
# Specify the path to the new file inside the "notes" folder
file_path = os.path.join("notes", "note1.txt")

# Open the file in append mode and write some content
with open(file_path, "a") as file:
    file.write("This is a new file created inside the notes folder.")

print(f"File '{file_path}' created successfully.")

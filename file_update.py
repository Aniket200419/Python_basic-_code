
import os

FILE_NAME = "myfile.txt"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Welcome to Python File Management!\n")
        print("File created successfully.")
    else:
        print("File already exists.")


def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content if content else "File is empty.")
    except FileNotFoundError:
        print("File not found. Please create the file first.")


def add_content():
    content = input("Enter content to add: ")

    with open(FILE_NAME, "a") as file:
        file.write(content + "\n")

    print("Content added successfully.")


def update_content():
    try:
        with open(FILE_NAME, "r") as file:
            old_content = file.read()

        print("\nCurrent content:")
        print(old_content)

        old_text = input("Enter text to replace: ")
        new_text = input("Enter new text: ")

        if old_text not in old_content:
            print("Text not found in the file.")
            return

        updated_content = old_content.replace(old_text, new_text)

        with open(FILE_NAME, "w") as file:
            file.write(updated_content)

        print("File updated successfully.")

    except FileNotFoundError:
        print("File not found. Please create the file first.")


def delete_content():
    confirm = input("Are you sure you want to clear the file? (yes/no): ")

    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            file.write("")
        print("File content cleared successfully.")
    else:
        print("Operation cancelled.")


def main():
    while True:
        print("\n===== FILE UPDATE SYSTEM =====")
        print("1. Create File")
        print("2. Read File")
        print("3. Add Content")
        print("4. Update Existing Content")
        print("5. Clear File Content")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            add_content()
        elif choice == "4":
            update_content()
        elif choice == "5":
            delete_content()
        elif choice == "6":
            print("Thank you for using File Update System!")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()

import os

def create_file(filename):
    with open(filename, 'w') as file:
        print(f"Created file: {filename}")

def write_text(filename, text):
    with open(filename, 'a') as file:
        file.write(text)
        print(f"Added text to {filename}")

def delete_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        os.remove(file)
        print(f"Deleted file: {file}")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a new file")
        print("2. Write text to a file")
        print("3. Delete all files")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            filename = input("Enter the filename: ")
            create_file(filename)
        elif choice == '2':
            filename = input("Enter the filename: ")
            if os.path.isfile(filename):
                text = input("Enter the text to add: ")
                write_text(filename, text)
            else:
                print(f"File '{filename}' does not exist.")
        elif choice == '3':
            delete_files()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

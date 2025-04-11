# File Read & Write + Error Handling 🖋️🧪

def modify_file(input_file, output_file):
    """
    Reads from 'input_file', converts content to uppercase, and writes to 'output_file'.
    """
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
            modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified content written to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def read_user_file():
    """
    Asks user for a filename and tries to read it, with proper error handling.
    """
    filename = input("📄 Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            print("\n📘 File content:\n")
            print(file.read())
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# === Main Program ===
if __name__ == "__main__":
    print("=== Error Handling Lab 🧪 ===")
    read_user_file()

    print("\n=== File Read & Write Challenge 🖋️ ===")
    # You can also prompt the user for filenames if you want
    modify_file("original.txt", "modified.txt")
    print("\n=== File Read & Write Challenge Completed! 🎉 ===")
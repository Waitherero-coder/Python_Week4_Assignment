def file_read_write():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File processed successfully! Modified version saved as {new_filename}")

    except FileNotFoundError:
        print("⚠️ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("⚠️ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

file_read_write()

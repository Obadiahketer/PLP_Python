try:
    file = open("sample.doc", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
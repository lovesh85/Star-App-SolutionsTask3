import os  

class MyFileReader:
    def __init__(self, file_path):
        self.file_path = file_path  

    def read_from_file(self):
        if not os.path.isfile(self.file_path):
            print("⚠️ File not found! Check the path.")
            return None  
        try:
            with open(self.file_path, "r") as file:  
                return file.read()  
        except Exception as error:
            print(f"❌ Error reading file: {error}")
            return None  

file_path = r"D:\Task-3\File Handling\Text.txt"  
reader = MyFileReader(file_path)

print("\n--- File Content ---\n")
if (content := reader.read_from_file()):
    print(content)

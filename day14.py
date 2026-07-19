import os

folder_path = r"D:\Linkdin file"

for filename in os.listdir(folder_path):
    old_file_path = os.path.join(folder_path, filename)
    if filename.endswith(".png"):

        new_filename = "processed" + filename
        new_file_path = os.path.join(folder_path, new_filename)
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
        except FileExistsError:
                print(f"Error: {new_filename} already exists. Skipping.")
    





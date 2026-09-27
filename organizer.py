import os
import shutil

# Folder containing the files
source_folder = "test_files"

# Folder where JPG files will be moved
destination_folder = "JPG Files"

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get all files from the source folder
files = os.listdir(source_folder)

moved_files = 0

# Check each file
for file in files:

    # Check if the file is a JPG file
    if file.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")
        moved_files += 1

# Display the result
print()
print("================================")
print("       FILE ORGANIZER")
print("================================")

if moved_files == 0:
    print("No JPG files were found.")

else:
    print(f"{moved_files} JPG file(s) moved successfully.")

print(f"Destination folder: {destination_folder}")
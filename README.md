# JPG File Organizer 🗂️

A simple Python automation script that automatically finds `.jpg` files in a folder and moves them into a separate folder.

## About the Project

This project demonstrates how Python can be used to automate a repetitive file-management task.

The script scans a specified folder, identifies files with the `.jpg` extension, and moves them into a separate `JPG Files` folder.

## Features

* Automatically scans a folder for JPG files
* Creates the destination folder if it does not exist
* Moves JPG files automatically
* Leaves other file types untouched
* Displays the files that were moved
* Reports the total number of JPG files moved

## Technologies Used

* Python 3
* `os` module
* `shutil` module
* File handling
* Loops
* Conditional statements
* String methods

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Create a folder named `test_files`.
4. Place `.jpg` files inside `test_files`.
5. Open the terminal.
6. Run:

```bash
python organizer.py
```

The script will automatically create a `JPG Files` folder and move the JPG files into it.

## Example

### Before

```text
test_files/
├── image1.jpg
├── image2.jpg
├── document.txt
└── image.png
```

### After

```text
test_files/
├── document.txt
└── image.png

JPG Files/
├── image1.jpg
└── image2.jpg
```

## Project Structure

```text
JPG-File-Organizer/
├── organizer.py
└── README.md
```

## Learning Outcome

This project helped me understand Python file-system automation using the `os` and `shutil` modules. I also practiced loops, conditional statements, string methods, and working with files and folders programmatically.

# File Organizer Readme

This Python script helps you organize files in a source directory by categorizing them into folders based on their file types. The organized files are then moved to a target directory with an added timestamp to their filenames.

## How to Use

1. **Run the Script:**
   - Save the script to a Python file (e.g., `file_organizer.py`).
   - Open a terminal and navigate to the directory containing the script.
   - Run the script using the command: `python file_organizer.py`

2. **Input Source and Target Directories:**
   - Enter the source directory path when prompted.
   - Enter the target directory path when prompted.

3. **File Organization:**
   - The script will create subfolders (images, documents, videos, other) in the target directory.
   - Files from the source directory will be categorized based on their extensions and moved to the appropriate subfolders.
   - Timestamps will be added to the filenames to avoid overwriting.

4. **Error Handling:**
   - If any errors occur during the file organization process, they will be displayed in the terminal.

## Example Usage

```bash
Enter source directory: /path/to/source
Enter target directory: /path/to/target
File organization completed!
```

## Note

- This script categorizes files with the following extensions:
  - Images: .jpg, .png
  - Documents: .pdf, .docx
  - Videos: .mp4, .avi
  - Other: Files with extensions not listed above

- Ensure you have the necessary permissions to read from the source directory and write to the target directory.

- For any issues or errors, review the displayed error messages in the terminal.

Happy file organizing!
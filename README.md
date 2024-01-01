# File Organizer

<img src="https://i.imgur.com/6VclBAI.png" alt="Image of program screen" width="500"/>
This file organizer is a simple Python application that helps users organize their files into categorized folders based on file extensions. It uses a Tkinter GUI to allow users to select a directory and automatically moves files such as text documents, PDFs, images, and more into respective folders.

### Features
- **GUI for easy interaction**
  <img src="https://i.imgur.com/P7kDBib.png" alt="Image of program screen" width="1200"/> <br><br>
- **Organizes files into folders based on file type (e.g., Text Files, PDF Files, Images)**
  <img src="https://i.imgur.com/iJdRbAx.png" alt="Image of program screen" width="1200"/> <br><br>
- **Undo functionality to revert any organization action**
  <img src="https://i.imgur.com/W7Yt9rA.png" alt="Image of program screen" width="1200"/> <br><br>
- **Option to open the organized directory in Windows Explorer**


### Requirements
- Python 3.x
- PIL library for image processing (install using `pip install Pillow`)

### Installation
Download the project files .zip or clone the repository to your local machine with the following command (requires Git to be installed):\
`git clone https://github.com/tsooli97/File-organizer`

### Usage
1. Run `main.py` to start the application.
2. Use the "Select Directory" button to choose the directory you want to organize.
3. Click "Organize Files" to automatically organize the files into folders.
4. If needed, use the "Undo Organization" button to revert any organization action.
5. The "Open directory after organizing" option can be checked to automatically open the directory in Explorer after organizing is complete.

### Project Structure
- `main.py` The main script to run the application. It sets up the GUI and integrates all functionalities.
- `logic.py` Contains the core logic for organizing files, handling file movements and other utility functions.

### Contributing
Contributions to the project are always welcome, if you're interested!

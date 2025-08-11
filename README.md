Image Resizer Tool

Objective
A Python tool to **resize and convert images in batch** using the **Pillow** library.  
This tool reads all images from an input folder, resizes them to user-specified dimensions, and saves them in JPEG format in an output folder.

Features
- Resize multiple images at once
- Convert all images to **JPEG**
- Supports `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif` formats
- User can specify:
  - Input folder path
  - Output folder path
  - New image width & height
- Works on **Windows, macOS, and Linux**

Tools & Libraries
- **Python 3.x**
- **Pillow** (Python Imaging Library fork)

Project Structure
ImageResizer/
│
├── image_resizer.py # Main Python script
├── README.md # Project documentation
├── input_images/ # Folder with original images (user-provided)
└── output_images/ # Folder for resized images (auto-created)

Installation & Usage

1.Clone or Download the Project

git clone https://github.com/your-username/image-resizer-tool.git
cd image-resizer-tool

2️.Install Dependencies
pip install pillow

3️.Run the Script
python image_resizer.py

4.Follow the Prompts:
Enter input folder path
Enter output folder path
Enter width & height (in pixels)

Example Run
=== Image Resizer Tool ===
Enter the path of the input folder containing images: input_images
Enter the path to save resized images: output_images
Enter the new width (px): 800
Enter the new height (px): 600
Resized and saved: output_images/photo1.jpg
Resized and saved: output_images/photo2.jpg
All images have been resized successfully!

Notes
Input folder must contain at least one supported image format.
Output folder will be auto-created if it does not exist.
All output images will be saved as JPEG format.


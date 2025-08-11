import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    """
    Resize and convert all images in the input folder to the specified size.
    Saves them as JPEG in the output folder.
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                # Resize image
                resized_img = img.resize((width, height))
                # Create output file path with .jpg extension
                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
                resized_img.save(output_path, "JPEG")
                print(f"Resized and saved: {output_path}")

    print("\n All images have been resized successfully!")

if __name__ == "__main__":
    print("=== Image Resizer Tool ===")
    
    # Ask for user input
    input_folder = input("Enter the path of the input folder containing images: ").strip()
    output_folder = input("Enter the path to save resized images: ").strip()
    
    try:
        width = int(input("Enter the new width (px): "))
        height = int(input("Enter the new height (px): "))
    except ValueError:
        print("Invalid size entered. Please enter numbers only.")
        exit()

    resize_images(input_folder, output_folder, width, height)

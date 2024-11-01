import os  
from PIL import Image  
  
def print_image_info(folder='output_images'):  
    """  
    Iterates through each image in the specified folder and prints  
    the image name, file size in KB, and dimensions in pixels.  
  
    :param folder: The directory containing the images.  
    """  
    # Ensure the folder exists  
    if not os.path.isdir(folder):  
        print(f"The folder '{folder}' does not exist.")  
        return  
  
    # Iterate over all files in the folder  
    for filename in os.listdir(folder):  
        file_path = os.path.join(folder, filename)  
  
        # Check if it is a file and has an image extension  
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):  
            try:  
                # Get the file size in bytes  
                file_size_bytes = os.path.getsize(file_path)  
                # Convert file size to kilobytes (1 KB = 1024 bytes)  
                file_size_kb = file_size_bytes / 1024  
  
                # Open the image to get dimensions  
                with Image.open(file_path) as img:  
                    width, height = img.size  
  
                # Print the image details  
                print(f"Image Name: {filename}")  
                print(f"File Size: {file_size_kb:.2f} KB")  
                print(f"Dimensions: {width} x {height} px")  
                print('-' * 40)  
  
            except Exception as e:  
                print(f"Error processing '{filename}': {e}")  
        else:  
            # Skip non-image files  
            continue  
  
if __name__ == "__main__":  
    print_image_info()  
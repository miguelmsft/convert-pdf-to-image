# convert-pdf-to-image
Code to convert pdf files to images
   
This repository contains two Python scripts:  
   
1. **`convert_pdf_to_image.py`**: Converts PDF files to PNG images using PyMuPDF.  
2. **`print_image_info.py`**: Iterates through images in a folder and prints their names, sizes in KB, and dimensions in pixels.  

It uses as an example the 2024 2024 Work Trend Index Annual Report from Microsoft and LinkedIn. 

https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
   
---  
   
## Table of Contents  
   
- [Description](#description)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [1. Converting PDFs to PNG Images](#1-converting-pdfs-to-png-images)  
  - [2. Printing Image Information](#2-printing-image-information)  
- [Directory Structure](#directory-structure)  
- [Sample Output](#sample-output)  
- [Notes](#notes)  
- [License](#license)  
   
---  
   
## Description  
   
This repository provides a simple solution for:  
   
- **Batch Converting PDFs to Images**: Automatically processes all PDF files in a specified directory and converts each page to a PNG image.  
- **Extracting Image Information**: Iterates through all images in a specified folder and prints out their filenames, sizes (in KB), and dimensions (in pixels).  
   
---  
   
## Prerequisites  
   
- **Python 3.6 or higher**  
   
### Required Python Libraries:  
   
- **PyMuPDF** (`fitz`): For converting PDF pages to images.  
- **Pillow** (`PIL`): For handling image files and extracting their dimensions.  
   
### Installation of Dependencies:  
   
1. **Install PyMuPDF:**  
  
   ```bash  
   pip install PyMuPDF  
   ```  
   
2. **Install Pillow:**  
  
   ```bash  
   pip install Pillow  
   ```  
   
---  
   
## Installation  
   
1. **Clone the Repository:**  
  
   ```bash  
   git clone https://github.com/yourusername/pdf-to-png-and-image-info.git  
   ```  
   
2. **Navigate to the Project Directory:**  
  
   ```bash  
   cd pdf-to-png-and-image-info  
   ```  
   
3. **Install Dependencies:**  
  
   Ensure you have installed the required libraries as mentioned in the [Prerequisites](#prerequisites) section.  
   
---  
   
## Usage  
   
### 1. Converting PDFs to PNG Images  
   
The script `pdf_to_png_batch.py` processes all PDF files in the `input_pdfs` directory and outputs the images to the `output_images` directory.  
   
#### Steps:  
   
1. **Prepare Input PDFs:**  
  
   - Place all your PDF files into the `input_pdfs` folder.  
   
2. **Run the Conversion Script:**  
  
   ```bash  
   python pdf_to_png_batch.py  
   ```  
  
   - The script will process each PDF file and convert its pages to PNG images.  
   - The output images will be saved in the `output_images` folder.  
   
#### Script Details:  
   
- **Input Directory:**  
  
  - Default: `input_pdfs`  
  - Contains the PDF files to be converted.  
   
- **Output Directory:**  
  
  - Default: `output_images`  
  - The converted PNG images will be saved here.  
   
- **Image Naming Convention:**  
  
  - Single-page PDF: `<pdf_filename>.png`  
  - Multi-page PDF: `<pdf_filename>_page_<page_number>.png`  
   
#### Customization:  
   
- **Changing Directories:**  
  
  - You can modify the input and output directories by editing the variables in the script:  
  
    ```python  
    input_dir = "your_input_directory"  
    output_dir = "your_output_directory"  
    ```  
   
- **Adjusting Image Quality:**  
  
  - The `zoom` parameter controls the resolution of the output images. Increase it for higher quality (at the cost of larger file sizes).  
  
    ```python  
    process_all_pdfs(input_dir, output_dir, zoom=1)  
    ```  
   
### 2. Printing Image Information  
   
The script `print_image_info.py` scans the `output_images` folder and prints the name, size in KB, and dimensions of each image.  
   
#### Steps:  
   
1. **Ensure Images are in the Output Folder:**  
  
   - The `output_images` folder should contain the images you want to inspect.  
   
2. **Run the Image Info Script:**  
  
   ```bash  
   python print_image_info.py  
   ```  
  
   - The script will output the details of each image to the console.  
   
#### Script Details:  
   
- **Target Directory:**  
  
  - Default: `output_images`  
  - The script reads images from this folder.  
   
- **Supported Image Formats:**  
  
  - `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.tiff`  
   
#### Customization:  
   
- **Changing the Target Folder:**  
  
  - You can specify a different folder by passing it as an argument when calling the function in the script:  
  
    ```python  
    if __name__ == "__main__":  
        print_image_info('your_image_folder')  
    ```  
   
---  
   
## Sample Output  
   
### Running `pdf_to_png_batch.py`:  
   
```  
Processing input_pdfs/document.pdf  
Saved output_images/document_page_1.png  
Saved output_images/document_page_2.png  
Processing input_pdfs/report.pdf  
Saved output_images/report.png  
```  
   
### Running `print_image_info.py`:  
   
```  
Image Name: document_page_1.png  
File Size: 250.75 KB  
Dimensions: 1275 x 1650 px  
----------------------------------------  
Image Name: document_page_2.png  
File Size: 245.30 KB  
Dimensions: 1275 x 1650 px  
----------------------------------------  
Image Name: report.png  
File Size: 120.50 KB  
Dimensions: 800 x 600 px  
----------------------------------------  
```  
   
---  
   
## License  
   
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  
   
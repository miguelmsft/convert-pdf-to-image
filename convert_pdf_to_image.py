import fitz  # PyMuPDF  
import os  
  
def pdf_to_png_with_fitz(pdf_path, output_folder, zoom=1):  
    """  
    Converts a PDF to PNG images using PyMuPDF, saving images with the same base filename as the PDF.  
      
    :param pdf_path: Path to the PDF file.  
    :param output_folder: Folder to save PNG images.  
    :param zoom: Zoom factor for image quality.  
    """  
    # Ensure the output folder exists  
    os.makedirs(output_folder, exist_ok=True)  
  
    # Extract the base filename without extension  
    pdf_base_name = os.path.splitext(os.path.basename(pdf_path))[0]  
      
    # Open the PDF file  
    doc = fitz.open(pdf_path)  
    page_count = doc.page_count  
  
    for page_number in range(page_count):  
        page = doc.load_page(page_number)  
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))  
          
        if page_count == 1:  
            # For single-page PDFs  
            image_filename = f'{pdf_base_name}.png'  
        else:  
            # For multi-page PDFs, append the page number  
            image_filename = f'{pdf_base_name}_page_{page_number + 1}.png'  
          
        image_path = os.path.join(output_folder, image_filename)  
        pix.save(image_path)  
        print(f'Saved {image_path}')  
      
    # Close the document  
    doc.close()  
  
def process_all_pdfs(input_folder, output_folder, zoom=2):  
    """  
    Processes all PDF files in the input_folder and converts them to PNG images.  
      
    :param input_folder: Folder containing PDF files.  
    :param output_folder: Folder to save PNG images.  
    :param zoom: Zoom factor for image quality.  
    """  
    # Ensure the output folder exists  
    os.makedirs(output_folder, exist_ok=True)  
  
    # Iterate over all files in the input folder  
    for filename in os.listdir(input_folder):  
        if filename.lower().endswith('.pdf'):  
            pdf_path = os.path.join(input_folder, filename)  
            print(f'Processing {pdf_path}')  
            pdf_to_png_with_fitz(pdf_path, output_folder, zoom)  
  
if __name__ == "__main__":  
    input_dir = "input_pdfs"          # Directory containing input PDF files  
    output_dir = "output_images"      # Directory where images will be saved  
  
    # Process all PDFs in the input directory  
    process_all_pdfs(input_dir, output_dir)  

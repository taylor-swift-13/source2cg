
from cgGen_doxygen import gen_doxygen
from cgGen_doxygen import delete_doxygen

import fitz  # PyMuPDF
import os
import json
from PIL import Image
import io


def get_color_from_pdf(pdf_path, x, y):
    # 打开 PDF 文件
    doc = fitz.open(pdf_path)
    
    # 获取指定页码的页面
    page = doc.load_page(0)  # page_num 是页面的索引，从 0 开始
    
    # 将 PDF 页面转换为图像
    pix = page.get_pixmap()
    
    # 将图像数据转换为 Pillow 图像对象
    img = Image.open(io.BytesIO(pix.tobytes()))
    
    # 获取指定坐标点 (img_x, img_y) 的颜色
    color = img.getpixel((x, y))
    
    return color


def extract_text_with_background(file_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(file_path)

        # Lists to store the extracted text based on background color
        grey_labels = []  # Labels with a gray background
        white_labels = []  # Labels with a white background

        # Iterate through each page of the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]

            # Extract text blocks from the page
            blocks = page.get_text("dict")["blocks"]
            
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()  # Extract text and remove extra spaces
                            bbox = fitz.Rect(*span["bbox"])  # Get the bbox of the text

                            center_x = bbox.x0 + 1
                            center_y = bbox.y0 + 1
                            color = get_color_from_pdf(file_path,center_x,center_y)

                            # Check the RGB color of the pixel
                            if is_gray(color):
                                if text not in grey_labels:
                                    grey_labels.append(text)
                            else:
                                if text not in white_labels:
                                    white_labels.append(text)

        # Construct the final result
        result = {
            "main": "".join(grey_labels),  # Text on gray background
            "dep": ", ".join(white_labels)   # Text on white background
        }

        return result

    except Exception as e:
        return f"Error occurred: {e}"

# Helper function to determine if the color is gray
def is_gray(color):
    # A color is considered gray if all its RGB components are close to each other
    r, g, b = color
    return r == 191 and g == 191 and b == 191

def process_filename(input_string):
    # 去掉后面的部分，只保留 '8h' 或 '8c' 之前的内容
    if '_8h' in input_string:
        filename = input_string.split('_8h')[0] + '_8h'
    elif '_8c' in input_string:
        filename = input_string.split('_8c')[0] + '_8c'
    else:
        filename = input_string

    # 将所有双下划线转为加号
    filename = filename.replace('__', '+')
    
    # 去掉所有单下划线
    filename = filename.replace('_', '')

        # 将所有加号转换为单下划线
    filename = filename.replace('+', '_')
    
    # 将 8 替换为点 '.'
    filename = filename.replace('8', '.')
    
    return filename


def process_all_pdfs_in_directory(directory):
    try:
        # Initialize an empty dictionary to hold file name results
        files_data = {}

        # Iterate through all files in the directory
        for file_name in os.listdir(directory):
            if file_name.endswith(".pdf") and "coll" not in file_name:   # Process only PDF files
                file_path = os.path.join(directory, file_name)
                
                # Process the filename (excluding extension) using process_filename
                processed_name = process_filename(file_name[:-4])  # Remove .pdf before processing
                
                # Call the actual text extraction function (this is just a placeholder)
                result = extract_text_with_background(file_path)
                
                # Add the result to the dictionary, grouped by the processed file name
                if processed_name not in files_data:
                    files_data[processed_name] = []
                files_data[processed_name].append(result)

        # Determine output folder path
        output_folder =  "json"
        
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate a unique filename based on the number of processed PDFs
        output_filename = f"output_{len(os.listdir(output_folder)) + 1}.json"
        output_filepath = os.path.join(output_folder, output_filename)

        with open(output_filepath, "w") as json_file:
            json.dump(files_data, json_file, indent=4)

        
        # Print the results as JSON
        print(json.dumps(files_data, indent=4))

        # Optionally, write the results to a JSON file
        with open(output_filepath, "w") as json_file:
            json.dump(files_data, json_file, indent=4)
        
        print(f"Results have been saved to {output_filepath}")


    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    directory = "input/latex"  # Specify the directory path
    gen_doxygen()
    process_all_pdfs_in_directory(directory)
    delete_doxygen()

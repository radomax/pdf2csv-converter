import sys
from pdf2image import convert_from_path
import pandas as pd
import pytesseract
import argparse

def pdf_to_images(pdf_path, first_page=None, last_page=None, password=None):
    """
    Convert PDF file to images.
    """
    try:
        options = {
            'dpi': 200,
            'poppler_path': '/usr/bin'
        }
        if first_page:
            options['first_page'] = first_page
        if last_page:
            options['last_page'] = last_page
        if password:
            options['password'] = password

        return convert_from_path(pdf_path, **options)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        sys.exit(1)

def images_to_text(images):
    """
    Extract text from a list of image objects using Tesseract.
    """
    text_output = []
    for image in images:
        text = pytesseract.image_to_string(image)
        text_output.append(text)
    return text_output

def text_to_csv(text_list, output_file):
    """
    Convert list of text to a CSV file.
    """
    df = pd.DataFrame(text_list, columns=['ExtractedText'])
    df.to_csv(output_file, index=False)
    print(f"Data extracted to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert PDF to CSV")
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--firstpage', type=int, help='First page to convert', default=None)
    parser.add_argument('--lastpage', type=int, help='Last page to convert', default=None)
    parser.add_argument('--password', type=str, help='Password for the PDF file (optional)', default=None)
    args = parser.parse_args()

    images = pdf_to_images(args.pdf_path, args.firstpage, args.lastpage, args.password)
    text_list = images_to_text(images)
    text_to_csv(text_list, '/home/rado/Nordstjernen/rest_fp_241130.pdf')

if __name__ == "__main__":
    main()


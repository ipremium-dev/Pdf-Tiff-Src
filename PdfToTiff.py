import os
from pdf2image import convert_from_path
# Library path
POPPLER_LIB_PATH = r'poppler-24.08.0-win\Library\bin'

# Configure Accordingly
WORK_DIR = r'C:\Users\DEV1\Downloads\test_data\\'
PDF_FILE_NAME = 'CV.pdf'
BARCODE = 'CV'

# No need to change these directory unless necessary
INPUT_PATH = WORK_DIR + PDF_FILE_NAME # Full path of PDF Input files
TIFF_OUTPUT_DIR = WORK_DIR + 'Output' # Process TIFF IMAGES

# Ensure the output directory exists
if not os.path.exists(TIFF_OUTPUT_DIR):
    print("Unable to find output path " + TIFF_OUTPUT_DIR)
    print("Creating Output path: " + TIFF_OUTPUT_DIR)
    os.makedirs(TIFF_OUTPUT_DIR)

print("Process start: " + INPUT_PATH)
pages = convert_from_path(INPUT_PATH, poppler_path=POPPLER_LIB_PATH) # Convert pdf to tiff pages

# Enumerate per tiff file
for i, image in enumerate(pages):
    tiff_filenme = f'' + BARCODE + '_' + str(i + 1) + '.TIFF'
    image_path = os.path.join(TIFF_OUTPUT_DIR, tiff_filenme)
    image.save(image_path, 'TIFF')
    print(f'Saved: {image_path}')

print("Pdf converted to Tiff Successfully")
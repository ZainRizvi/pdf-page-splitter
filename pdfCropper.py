from pypdf import PdfWriter, PdfReader, Transformation
import sys

file_name = sys.argv[1]
output_file = sys.argv[2]
pages_to_skip = list(map(lambda i: int(i), sys.argv[3:])) # this is for if you want to skip any pages on the output pdf

reader = PdfReader(file_name)
writer = PdfWriter()

new_page_num = 0
horiz_offset = 10 # useful for if the pdf you have is off center

# How much to crop each half of the page by
left_crop = 35
right_crop = 10
top_crop = 20
bottom_crop = 20

for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    
    lower_left = page.cropbox.lower_left
    lower_right = page.cropbox.lower_right
    upper_left = page.cropbox.upper_left
    upper_right = page.cropbox.upper_right
    
    if (new_page_num not in pages_to_skip):
        page.mediabox.lower_left = (lower_left[0] + left_crop + horiz_offset, lower_left[1] + bottom_crop)
        page.mediabox.upper_right = (upper_right[0]/2 - right_crop + horiz_offset, upper_right[1] - top_crop)
        writer.add_page(page)
    new_page_num += 1
    
    if (new_page_num not in pages_to_skip):
        page.mediabox.lower_left = (upper_right[0]/2 + left_crop, bottom_crop)
        page.mediabox.upper_right = (upper_right[0] - right_crop, upper_right[1] - top_crop)
        writer.add_page(page)
    new_page_num += 1

with open(output_file, "wb") as file_pointer:
    writer.write(file_pointer)
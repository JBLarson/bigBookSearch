
import json
import PyPDF2

def extract_pdf_data(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        data = {}
        chapter = None
        page_count = 0
        numPages = len(reader.pages)
        
        for page_num in range(numPages):
            text = reader.pages[page_num].extract_text()  # <-- Changed here
            
            # Assuming chapters are defined with "Chapter X" where X is a number
            # Adjust this based on your PDF's formatting
            if "Chapter" in text:
                chapter = text.split("\n")[0]  # Getting the chapter title (the first line of the page, in this example)
                data[chapter] = {}
                page_count = 0
            
            page_count += 1
            
            if chapter:  # Only if a chapter has been identified
                key = f'page_{page_count}'
                data[chapter][key] = text
                
        return data

pdf_data = extract_pdf_data('bigBook.pdf')
#print(pdf_data)
#print(type(pdf_data))

with open('data.json', 'w') as file:
    json.dump(pdf_data, file, indent=4)

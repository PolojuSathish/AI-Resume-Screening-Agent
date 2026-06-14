import fitz
#we are importing a library called fitz
#fitz comes from PyMuPdf ,if we instal it so it opens the file and reads the text.
def extract_text_from_pdf(pdf_file):
    text = " "
#now pdf should open and read all the pages    
    pdf_document = fitz.open(stream =pdf_file.read(),filetype="pdf")
    for page in pdf_document:   #Loop to read all the pages
        text += page.get_text()   #text+= is like coverting total pages text into one text
    return text     
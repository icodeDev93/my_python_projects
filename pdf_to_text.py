import PyPDF2

# Open the PDF file
with open("Projects GenAI Pinnacle Program.pdf", "rb") as pdf:
    reader = PyPDF2.PdfReader(pdf)

    # Get the first page
    page = reader.pages[0]

    # Extract text from the page
    text = page.extract_text()
    print(text)
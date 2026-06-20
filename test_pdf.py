from pypdf import PdfReader

reader = PdfReader("Jai_Indra_Teja_Resume-Final-2.pdf")

full_text = ""

for page in reader.pages:
    full_text += page.extract_text()

print("Total Characters:", len(full_text))
print("\nFirst 500 characters:\n" )
print(full_text[:500])
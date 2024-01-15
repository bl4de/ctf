from pypdf import PdfReader

with open("secret.pdf", "rb") as pdf:
	reader = PdfReader(pdf)
	text = reader.pages[0].extract_text()
	print(text)


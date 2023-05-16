from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open("108820018_蔡翔宇.pdf", "rb"))

start_page = 62
end_page = 87

# if(end_page > len(inputpdf.pages)):
#     end_page = len(inputpdf.pages)

for i in range(start_page, end_page):
    print(i)
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("out_page/108820018_蔡翔宇_%03d.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
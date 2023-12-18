

https://pypdf.readthedocs.io/en/stable/

```python title="pdf.py"

split ddia.pdf by chapter, then merge it.
import os.path

from pypdf import PdfReader, PdfWriter

input_file = "DDIA.pdf"
output_file = "out.pdf"

pdf_reader = PdfReader(input_file)
pdf_writer = PdfWriter()


def info():
    print(pdf_reader.metadata)
    print(len(pdf_reader.pages))
    print(pdf_reader.outline)


def split(begin, end):
    for page in pdf_reader.pages[begin:end]:
        pdf_writer.add_page(page)


def dest(file_name=output_file, pdf_writer=pdf_writer):
    if os.path.exists(file_name):
        os.remove(file_name)
    pdf_writer.write(file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    info()

    merger = PdfWriter()
    list_pdf = [
        (24, 45),
        (48, 86),
        (90, 126),
        (132, 162),
        (172, 215),
        (220, 240),
        (242, 289),
        (294, 334),
        (342, 397),
        (410, 453),
        (460, 503),
        (510, 566),
    ]
    for index, range_page in enumerate(list_pdf):
        print(range_page, index)
        split(*range_page)
        file_name = "%s.pdf" % index
        dest(file_name=file_name, pdf_writer=pdf_writer)
        pdf_writer = PdfWriter()

        merger.append(file_name)


    dest(pdf_writer=merger)

```
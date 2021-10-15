import pandas as pd
from xhtml2pdf import pisa

def csv_to_html(filepath):
    csv_handle = pd.read_csv(filepath)
    csv_handle.to_html("Table.html")
    fh =open(r"Table.html",'r')
    content = fh.read()
    return content

def html_to_pdf(content, output):
    # Open file to write
    result_file = open(output, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(content,dest=result_file)           

    result_file.close()

    result = pisa_status.err

    if not result:
        print("Successfully created PDF")
    else:
        print("Error: unable to create the PDF")    
    return result


if __name__ == "__main__":
    filepath = input("Enter file path\n")
    html_content = csv_to_html(filepath)
    html_to_pdf(content=html_content, output="Table.pdf")



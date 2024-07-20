import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

if __name__ == "__main__":
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
        merger.write("combainedPDF.pdf")

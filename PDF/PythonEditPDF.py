########################
#  python 3.6          #
#  �⣺PyPDF2           #
#  2019.3.18 by:Ljy    #
########################
# encoding:utf-8
from PyPDF2 import PdfFileReader, PdfFileWriter


readFile = 'C:/Users/Ljy/Desktop/test.pdf'
outFile = 'C:/Users/Ljy/Desktop/ok.pdf'
pdfFileWriter = PdfFileWriter()

 # ��ȡ PdfFileReader ����
pdfFileReader = PdfFileReader(readFile)  # ���������ʽ��pdfFileReader = PdfFileReader(open(readFile, 'rb'))
 #�ĵ���ҳ��
numPages = pdfFileReader.getNumPages()
print (numPages)
if numPages > 1:
# �ӵ�nҳ֮���ҳ�棬�����һ���µ��ļ��У����ָ��ĵ�
    n=1
    for index in range(n, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)
    # �����ÿҳ����һ�𱣴����ļ���
    pdfFileWriter.write(open(outFile, 'wb'))

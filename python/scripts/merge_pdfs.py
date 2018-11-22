# -*- coding:utf-8*-
import sys
import os
import pyPdf

def merge_pdfs(pdf_path_list, to_file):
    pdf_out = pyPdf.PdfFileWriter()
    total_page_size = 0
    f_in_handler_list = []
    for path in pdf_path_list:
        # 这里不能用 with open(), 因为with语句会自动关闭文件, 导致pdf_out.write(f_out)失败
        f = open(path, "rb")
        f_in_handler_list.append(f)

        pdf_in = pyPdf.PdfFileReader(f)
        page_size = pdf_in.getNumPages()
        total_page_size += page_size

        # 分别将page添加到输出pdf_out中
        for i in range(0, page_size):
            pdf_out.addPage(pdf_in.getPage(i))
        print "Processed file path: %s, page_size: %d" %(path, page_size)
    
    with open(to_file, "wb") as f_out:
        pdf_out.write(f_out)
        print "Merged file path: %s, page_size: %d" %(to_file, pdf_out.getNumPages())

    # close pdf_in句柄
    for f in f_in_handler_list:
        f.close ()

if __name__ == '__main__':
    # def get_pic_file_path_list():
    #     file_list = glob.glob(r'newer_self_learing_20/*.jpg')
    #     return file_list

    pdf_path_list = ["newer_self_learing_20.pdf"] * 2
    to_file = "merged.pdf"
    merge_pdfs(pdf_path_list, to_file)



#coding:utf8
import os 
import string
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import sys
import glob

def pics2pdf_with_scale(pic_file_path_list, to_pdf):
    """
    to_pdf: pdf file path ,include filename
    pic_file_path_list: 图片路径的列表
    这个是有缩放版的, 没有仔细研究
    """
    (w, h) = landscape(A4)
    (h, w) = (w, h)
    print w, h
    c = canvas.Canvas(to_pdf, pagesize = (w, h))
    c = canvas.Canvas(to_pdf)
    for f in pic_file_path_list:
        # (xsize, ysize) = Image.open(f).size

        # ratx = xsize / w
        # raty = ysize / h
        # ratxy = xsize / (1.0 * ysize)
        # if ratx > 1:
        #     ratx = 0.99
        # if raty > 1:
        #     raty = 0.99

        # rat = ratx

        # if ratx < raty:
        #     rat = raty
        # widthx = w * rat
        # widthy = h * rat
        # widthx = widthy * ratxy
        # posx = (w - widthx) / 2
        # if posx < 0:
        #     posx = 0
        # posy = (h - widthy) / 2
        # if posy < 0:
        #     pos = 0 

        # print widthx, widthy
        # c.drawImage(f, 0, 0, widthx, widthy)
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
    c.save()
    print "Image to pdf success!"



def pics2pdf(pic_file_path_list, to_pdf):
    """
    to_pdf: pdf file path ,include filename
    pic_file_path_list: 图片路径的列表
    """
    (w, h) = landscape(A4)  # 从源码中可以看出, 该函数对返回的结果做过调整, 数据大的在前
        (w, h) = (h, w)
    print "page size: ", w, h
    c = canvas.Canvas(to_pdf, pagesize = (w, h))
    for f in pic_file_path_list:
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
    c.save()


if __name__ == '__main__':
    def get_pic_file_path_list():
        file_list = glob.glob(r'newer_self_learing_20/*.jpg')
        return file_list
    pic_file_path_list = get_pic_file_path_list()
    pics2pdf(pic_file_path_list, "newer_self_learing_20.pdf")
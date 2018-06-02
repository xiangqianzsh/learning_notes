# reportlab


```python

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from matplotlib import pyplot as plt
(w, h) = landscape(A4)
c = canvas.Canvas('mypdf.pdf', pagesize = landscape(A4))
n = 0
for query in querys[:2]:
    print '='*30
    for col in cols:
        table = df_pivot.loc[query, col]
        print query, col
        # print table
        table.plot()
        # fig_name = 'figs/%s.jpg' %(query + '_' + col)
        # fig_name = fig_name.decode('utf8')
        # # plt.savefig(fig_name)
        
        # print [fig_name]
        # c.drawString(30, h-30, fig_name)    #//输出区域及内容
        # # c.drawImage(fig_name, 0, 0, w, h-100)
        # c.showPage()  
c.save()

```
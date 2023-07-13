import os
from PyQt5.QtWidgets import*
#2.hafta
from PyQt5.QtCore import Qt # En boy oranını koruyarak yeniden boyutlandırma için Qt.KeepAspectRatio sabitine ihtiyaç vardır..
from PyQt5.QtGui import QPixmap # ekranda görüntülenecek şekilde optimize edilmiş resim
from PIL import Image
#--
 
app=QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Kolay Fotoğraf Editörü")
lb_image=QLabel("Tablo")
btn_dir=QPushButton("Dosya")
lw_files = QListWidget()

btn_left=QPushButton("Sola")
btn_right=QPushButton("Sağa")
btn_flip=QPushButton("Ayna")
btn_sharp=QPushButton("keskinlik ")
btn_bw=QPushButton("Siyah Beyaz ")


row=QHBoxLayout() #ana satır
col1=QVBoxLayout()#dikey
col2=QVBoxLayout()#dikey
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image,95)
row_tools=QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)




win.show()
def filter(files,extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result


def chooseWorkdir():
    global workdir          
    workdir= QFileDialog.getExistingDirectory()
    #değişken içersindeki herşeyi dizin veya liste haline getirir

def showFilenamesList ():
    extensions=['.jpg','.jpeg','.png','.bmp']
    chooseWorkdir()
    filenames=filter(os.listdir(workdir),extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename) 

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename=filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def saveImage(self):
        '''dosyanın bir kopyasını alt klasöre kaydeder'''
        path=os.path.join(self.dir, self.save_dir)
        #dosya yolu var mı ,dosya dizin halde mi?
        if not(os.path.join.exists(path) or os.path.isdir(path)):
            os.mkdir(path)#yeni dizin
        image_path = os.path.join(path,self.filename )
        self.image.save(image_path)

workimage = ImageProcessor()
#btn_bw.clicked.connect(workimage.do_bw)
btn_dir.clicked.connect(showFilenamesList)





app.exec()
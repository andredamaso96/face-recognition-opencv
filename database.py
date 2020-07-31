import glob
import os
import sqlite3

''' open faces.db and create tables
    path is the image path
    name ir the name paths
'''
conn = sqlite3.connect('images.db')
conn.execute('''create table if not exists images (
                    id integer PRIMARY KEY,
                    name text not null,
                    path unique not null
                )''')



def getFileExt(filePath):
    filePath = filePath.split("\\")[-1:][0]
    if filePath.count(".") == 0:
        return False
    ext = filePath.split(".")
    ext = ext[len(ext)-1]
    return ext

def genimages(path):
    '''
        Generate images.
        Os.walk method is used by migratory species in the directory in the output files in the directory name, up or down
    '''
    
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            value = []
            if getFileExt(file) == "jpg":
                #print(os.path.join(root, file))
                pathFile = os.path.join(root, file)
                value.append(root)
                value.append(pathFile)
                insertImage(value)
                value=[]


#function that inserts values ​​into the database
def insertImage(values):
    sql = 'insert into images(name, path) values(?, ?)'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

genimages("dataset")
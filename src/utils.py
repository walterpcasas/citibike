import os
import zipfile
from urllib import request

def createFolder(folderpath):
    """Create folder and subfolder.
    """
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        print('Created', folderpath)


def getData(month, year, outDir):

    url = 'https://s3.amazonaws.com/tripdata/{}{:02d}-citibike-tripdata.csv.zip'.format(year, month)
    print('Getting data from:\n\t',url)

    filename = os.path.basename(url)
    outFilepath = os.path.join(outDir, filename)

    request.urlretrieve(url, outFilepath)
    print('DONE!')


def extractZip(zipPath, outDir):

    createFolder(outDir)
    with zipfile.ZipFile(zipPath, 'r') as zip:
        zip.extractall(outDir)
    print('Successfully extracted!')




if __name__ == '__main__':
    #getData(3, 2019, '/data_lids/home/walter/Lab/citibike/data/raw')
    zipPath = '/data_lids/home/walter/Lab/citibike/data/raw/202201-citibike-tripdata.csv.zip'
    outDir = '/data_lids/home/walter/Lab/citibike/data/raw/test01'
    extractZip(zipPath, outDir)
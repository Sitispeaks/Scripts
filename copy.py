import sys
import os
import shutil
import  time

def copyFiles(src, dst):
    srcFiles = os.listdir(src)
    dstFiles = dict(map(lambda x:[x, ''], os.listdir(dst)))
    filesCopiedNum = 0
    
    for file in srcFiles:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        # copy the folder. if exist, recursive call this function,
        # otherwise create a new folder then call this function
        if os.path.isdir(src_path):
            if not os.path.isdir(dst_path):
                os.makedirs(dst_path)  
            filesCopiedNum += copyFiles(src_path, dst_path)
        # copy the file. if exist, do nothing
        elif os.path.isfile(src_path):                
            if not dstFiles.get(file):
                shutil.copyfile(src_path, dst_path)
                filesCopiedNum += 1
            
    return filesCopiedNum

def test():
    src_dir = os.path.abspath(input('Please enter the source path: '))
    if not os.path.isdir(src_dir):
        print ('Error: source folder does not exist!')
        return 0
    
    dst_dir = os.path.abspath(input('Please enter the destination path: '))
    start_time=time.time()
    if os.path.isdir(dst_dir):
        num = copyFiles(src_dir, dst_dir)
    else:
        print ('Destination folder does not exist, a new one will be created.')
        os.makedirs(dst_dir)
        num = copyFiles(src_dir, dst_dir)
    end_time=time.time()
    print("Total time taken",end_time-start_time)
    print ('Copy complete:', num, 'files copied.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        copyFiles(sys.argv[1], sys.argv[2])
    else:
        test()
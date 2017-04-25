import os
def get_files_from_folder(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            print f
            print "like you:", f
            #print os.path.join(root, f)


get_files_from_folder("../WBTestdata/proxy")
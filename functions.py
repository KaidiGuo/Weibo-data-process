import os
def get_files_from_folder(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            print f
            print "like you:", f
            #print os.path.join(root, f)


get_files_from_folder("../WBTestdata/proxy")

def creat_date_list(month,i,j):
    dates = []
    for n in range(i,j):
        date = month + "-" +str(n).zfill(2)
        dates.append(date)
    return dates

# print creat_date_list("04",01,15)
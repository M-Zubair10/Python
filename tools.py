import glob
def read_file_names(path):
    return [i.split('\\')[-1] for i in glob.glob(path+'/*')]
def contains(str1,str2):
    return str1.find(str2)!=-1

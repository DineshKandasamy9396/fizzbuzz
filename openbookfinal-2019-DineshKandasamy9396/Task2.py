import os
def walk(dirname):
    my_dict ={}
    for name in os.listdir(dirname): 
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            my_dict[path] = os.path.isfile(path)
        else:
            walk(path)

cwd =" /home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/"
fout =open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/file.list.txt",mode='w')
walk(cwd)

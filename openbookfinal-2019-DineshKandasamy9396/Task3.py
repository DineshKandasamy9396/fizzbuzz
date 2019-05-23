fin = [open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/Book1.txt"),
open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/Book2.txt"),
open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/Book3.txt")]

fin_2k=open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/20k.txt")

foutrareword = open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/rarewords.list.txt",mode='w')

for book in range(len(fin)):
 filename = "book"+ str(book) + "uniqu.txt"
 foutbookuniq = open("/home/dinu/fizzbuzz-DineshKandasamy/openbookfinal-2019-DineshKandasamy9396/%s" % (filename), mode='w')
 book_read = open(book).read()
 words = book_read.split()
 book_20k_read = fin_2k.read() 
 for word in words:
    if word not in book_20k_read:
     foutrareword.write(word + '\n')
    elif word in book_20k_read:
     foutbookuniq.write(word+'\n')



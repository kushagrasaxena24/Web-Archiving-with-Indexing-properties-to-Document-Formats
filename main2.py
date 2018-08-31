import os

xc=0
results = list()
results.append("import pypub")
results.append("my_first_epub = pypub.Epub('My Second Epub')")
with open('crawled.txt', 'rt') as f:
    for line in f:
        results.append("my_first_chapter" + str(xc) + "= pypub.create_chapter_from_url('" + line.replace('\n', '') + "')")                
        results.append("my_first_epub.add_chapter(my_first_chapter" + str(xc) + ")")
        xc+=1 

results.append("my_first_epub.create_epub('D:/')")       
with open("right.py", 'w') as f:
        for l in results:
            f.write(l+"\n")
print('Creating EPUB please wait....')
os.system('python right.py' )


	


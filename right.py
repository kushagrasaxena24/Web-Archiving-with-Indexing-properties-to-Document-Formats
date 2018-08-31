import pypub
my_first_epub = pypub.Epub('My Second Epub')
my_first_chapter0= pypub.create_chapter_from_url('https://cs.wikipedia.org/wiki/Epub')
my_first_epub.add_chapter(my_first_chapter0)
my_first_chapter1= pypub.create_chapter_from_url('https://en.wikipedia.org/w/index.php?title=EPUB&action=edit&section=6')
my_first_epub.add_chapter(my_first_chapter1)
my_first_chapter2= pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/EPUB')
my_first_epub.add_chapter(my_first_chapter2)
my_first_chapter3= pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/EPUB#cite_ref-epub2.0_history_4-0')
my_first_epub.add_chapter(my_first_chapter3)
my_first_chapter4= pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/Wikipedia:About')
my_first_epub.add_chapter(my_first_chapter4)
my_first_chapter5= pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer')
my_first_epub.add_chapter(my_first_chapter5)
my_first_epub.create_epub('D:/')
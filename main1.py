import pypub
my_first_epub = pypub.Epub('My Second Epub')
my_first_chapter = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/FBReader')

my_first_epub.add_chapter(my_first_chapter)
my_first_chapter4 = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/PocketBook_eReader')

my_first_epub.add_chapter(my_first_chapter4)

my_first_chapter1 = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/Smashwords')

my_first_epub.add_chapter(my_first_chapter1)

my_first_chapter2 = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/Raster_graphics')

my_first_epub.add_chapter(my_first_chapter2)

my_first_chapter3 = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/FBReader')

my_first_epub.add_chapter(my_first_chapter3)

#my_first_chapter1 = pypub.create_chapter_from_url('https://en.wikipedia.org/wiki/EPUB')
#my_first_epub.add_chapter(my_first_chapter1)
my_first_epub.create_epub('D:/')
from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import random



class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    errors_file = ''
    queue = set()
    source_urls = {}
    crawled = set()
    errors = set()




    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.errors_file = Spider.project_name + '/errors.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.errors = file_to_set(Spider.errors_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled :
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            links, error_str = Spider.gather_links(page_url)
            Spider.add_links_to_queue(links, page_url)
            if (len(Spider.crawled))>5:
                return 0
            if len(error_str) > 0:
                Spider.errors.add(error_str)
            Spider.queue.remove(page_url)
            try:
                append_str = max(80-len(page_url), 4)*' ' + Spider.source_urls[page_url]
            except KeyError:
                append_str = ""
            Spider.crawled.add(page_url + append_str)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''

        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            err_str = "ERROR: {}  --  {}".format(page_url, str(e))
            print(err_str)
            return set(), err_str
        return finder.page_links(), ""

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links, page_url):
        xc = 0
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url) and Spider.domain_name[0] is 'h' :
                # also gather foreign links, but don't crawl from them (otherwise we might end up crawling the entire internet lol)
                Spider.crawled.add(url)
            else:
                Spider.queue.add(url)

                #Spider.source_urls[url] = page_url

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.errors, Spider.errors_file)



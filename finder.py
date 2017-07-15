class Finder():
#this permit lookup an keyword that can be in a webpages
    def lookup(self,index,keyword):
        if keyword in index:
                return index[keyword]
        else:
            return []
    def lucky_search(index,ranks,keyword):
        pages = lookup(index, keyword)
        if not pages:
            return None
        best_page - page[0]
        for candidate in pages:
            if ranks[candidate] > ranks[best_page]:
                best_page = candidate
        return best_page

#this procedure get the link of a tag in html <a>
    def get_next_target(self,s):

        start_link = s.find('<a href=')

        if start_link == -1:
            return None,0
        start_quote = s.find('"',start_link)
        end_quote = s.find('"',start_quote+1)
        url = s[start_quote+1:end_quote]
        return url,end_quote
#this procedure get all the links in a web page help by get_next_target
    def get_all_links(self,page):
        links=[]
        while True:
            url, endpos = self.get_next_target(page)

            if url:
                links.append(url) 
                page = page[endpos:]
            else:
                break
        return links
#this procedure permit add items in a list whitout duplicates
    def union(self,p,q):
        for e in q:
            if e not in p:
                p.append(e)

    def get_page(self,url):
        try:
            import urllib.request

            return  urllib.request.urlopen(url).read().decode('utf-8','replace')
        except:
            return ""

#this permit add to index a list of word that appers in a webpage
    def add_page_to_index(self,index, url, content): 
        words = content.split() 
        for word in words: 
            self.add_to_index(index, word, url) 

#this work with record_user_click indeed of the top add_to_index
    def add_to_index(self, index, keyword, url):
        l = self.lookup(index,keyword)
        if  keyword in index:
            if not url in index[keyword]:            
                index[keyword]=l.append(url)
        else:
            index[keyword]=[url]
             
    # not found, add new keyword to index 
    def compute_ranks(self,graph):
        d = 0.8 #damping factor
        numloops = 10

        ranks={}
        ngpages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / ngpages
        for i in range(0,numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d)/ngpages
                for node in graph:
                    if page in graph[node]:
                        newrank = newrank + d *(ranks[node] / len(graph[node]))
                newranks[page] = newrank
            ranks = newranks
        return ranks

#this procedure permit crawl the link in a web pages and define a depth of lookup
    def crawl_web(self,seed): 
        tocrawl = [seed] 
        crawled = [] 
        index = {}
        graph = {}
        while tocrawl: 
            page = tocrawl.pop()
            if page not in crawled: 
                content = self.get_page(page)            
                self.add_page_to_index(index, page, content) 
                outlinks = self.get_all_links(content)
                graph[page]= outlinks

                self.union(tocrawl, outlinks) 
                crawled.append(page) 
        return index,graph 
     

#this permit record de number of click by url
    def record_user_click(index,keyword,url):
        urls = lookup(index, keyword)
        if urls:
            for entry in urls:
                if entry[0] == url :
                    entry[1] = entry[1] + 1

#this create a big fake index only for test
    def make_big_index(self,size):
        index = {}
        letters = ['a','a','a','a','a','a','a','a']
        while len(index) < size:
            word = self.make_string(letters)
            self.add_to_index(index,word,'fake')
            for i in range(len(letters) - 1, 0, -1):
                if letters[i] < 'z':
                    letters[i]= chr(ord(letters[i])+1)
                    break
                else:
                    letters[i]='a'
        return index
#create a string only for test
    def make_string(self,p):
        s = ""
        for e in p:
            s = s + e
        return s
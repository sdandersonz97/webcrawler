import finder


find = finder.Finder()  





index,graph = find.crawl_web('http://sdandersonz.pythonanywhere.com/')
print (graph)
rank = find.compute_ranks(graph)
print (rank)

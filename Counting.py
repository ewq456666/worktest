from collections import Counter
import ntpath

def path_leaf(path):
    head,tail = ntpath.split(path)
    return tail
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]
fileName=[]
for index,url in enumerate(urls):
    fileName.append(path_leaf(url))
    
counts = Counter(fileName)
print(counts.most_common(3))

for key, value in counts.most_common(3):
    print(key, end=" ")
    print(value)
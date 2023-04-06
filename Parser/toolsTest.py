from html.parser import HTMLParser
import matplotlib.pyplot as plt
import numpy as np

pal = ['portalAssignmentList.html', 'Aspen_ Assignments.html', 'Aspen_ Assignments1.html']
def files(filer):
    text_file = open(filer, "r")
    pal = text_file.read()
    text_file.close()
    return(pal)

class parsing(HTMLParser):
    def __init__(self, ypoints, xpoints):
        HTMLParser.__init__(self)
        self.ypoints = ypoints
        self.xpoints = xpoints
        self.x = []
        self.end = -1
    def handle_starttag(self, tag, attrs):

        if tag == 'span':
            for elem in attrs:
                i = attrs.index(elem)
                if 'percentFieldInlineLabel' in attrs[i]:
                    self.x.append(HTMLParser.getpos(self))
                    #print(attrs[i], self.x)
        
    def handle_endtag(self, tag):
        if tag == 'html':
            self.end += 1
            print(tag)
    def handle_data(self, data):
        for i in self.x:
            if i[0] == HTMLParser.getpos(self)[0] and "%" in data:
                result = data.strip().replace('%','')
                self.ypoints.append(int(result))

ypoints = []
xpoints = []


parser = parsing(ypoints, xpoints)
for i in range(len(pal)):
    parsed = parser.feed(files(pal[i]))

ploty = np.array(ypoints)

plt.plot(ypoints)
plt.show()
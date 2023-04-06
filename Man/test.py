import json
import textwrap 


with open('file.txt') as f:
    data = f.read()
s_classes = json.loads(data)


class assignment:
    def __init__(self, nothi, noth, name, assigned, due, category, score, points, feedback = 'none'):
        self.name = name
        self.assigned = assigned
        self.due = due
        self.category = category
        self.score = score
        self.points = points
        self.feedback = feedback
    def __str__(self):
        text = 'Name: ' + self.name + '\n Assigned / Due: ' + self.assigned + '/' + self.due + '\n Category:' \
        + self.category + '\n Score: ' + self.score + self.points
        return textwrap.indent(text, '      ')
        

class weights:
    def __init__(self, cat, weight):
        self.weigh = {}
        for i in cat:
            self.weigh[cat[cat.index(i)]] = weight[cat.index(i)]

class sclass:
    def __init__(self, name, weighting, assignments):
        self.assignment = assignments
        for i in self.assignment:
            self.assignments = self.assignment[self.assignment.index(i)]
        self.weighting = weighting
        self.name = name
    def __str__(self):
        return self.name + '\n Assignments:\n ' + str(self.assignments)
    
class gradebook:
    def __init__(self, classes):
        self.classes = classes

categ = ["Homework", "Enrichment Activities", "Quiz"]
weig = [.15, .45, .4]
wet = weights(categ, weig)
na = 'AP CALCULUS'



for classy in s_classes:
    asl = []
    for ass in s_classes[classy]:
        if ass == ['']:
            break
        print(ass)
    
        asl.append(assignment(*ass))
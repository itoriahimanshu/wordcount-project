from django.http import HttpResponse
from django.shortcuts import render
import operator



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltxt = request.GET['fulltext']
    wordlist = fulltxt.split()

    worddictionary = {}
    for word in wordlist :
        if word in worddictionary:
             worddictionary[word]+=1
        else :
             worddictionary[word]=1
    sorteddic = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse = True)

    return render(request,'count.html',{'fulltxt':fulltxt, 'countit':len(wordlist),
                                         'worddictionary':sorteddic})

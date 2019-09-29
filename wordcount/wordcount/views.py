# from django.http import HttpResponse
import operator
from django.shortcuts import render, HttpResponse


def homepage(request):
    context = {
        'title': 'Word Count',
        'sub_title': 'Count every word'
    }
    return render(request, 'home.html', context)

def countpage(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split() #turn each word into a list
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    context = {
        'count': len(wordlist),
        'fulltext': fulltext,
        'worddictionary': sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    }
    return render(request, 'count.html', context)
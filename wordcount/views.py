from django.http import HttpResponse
from django.shortcuts import render
import re

def homepage(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	words = re.split('[ ?!.,-]', fulltext)

	words_dict = dict()
	for word in words:
		if word.lower() in words_dict and word:
			words_dict[word.lower()] += 1
		else:
			words_dict[word.lower()] = 1
	sorted_words = sorted(words_dict.items(), key = lambda x: x[1], reverse=True)
	print(sorted_words)
	
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 
		'sorted_words': sorted_words})
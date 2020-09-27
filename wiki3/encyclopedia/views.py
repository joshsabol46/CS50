import markdown2
import random
import re
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    entries = util.list_entries()

    if title in entries:
        content = util.get_entry(title)

        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": markdown2.markdown(content)
            # send title and content to HTML
        })
    else:
        return render(request, "encyclopedia/error.html", {
            'error_message': 'Page not found'
        })

# Search #1
# Breaks when searching for lower exact match

def search(request):
    entries = util.list_entries()
    query = request.POST.get("q")
    if util.get_entry(query):
        return redirect("wiki", title=query)
    else:
        match = []
        for i in entries:
            if query.lower() in i.lower():
                match.append(i)
        if len(match) == 0:
            return render(request, "encyclopedia/error.html", {
                'error_message': f'No results found for \'{query}\' '
            })
        else:
            return render(request, 'encyclopedia/search.html', {
                "results" : match,
                "search" : query
            })

# Search #2
# def search(request):
#     if request.method =='POST':
#         response = request.POST["q"]
#         entry = util.get_entry(response)
#         if entry:
#             print(entry)
#             return HttpResponseRedirect("wiki/"+entry)
#         else:
#             entries = util.list_entries()
#             search_entries = [i for i in entries if response.lower() in i.lower()]
#             if search_entries:
#                 return render(request, 'encyclopedia/index.html',{  
#                     "entries": search_entries
#                 })
#             else:
#                 return render(request, "encyclopedia/error.html",{
#                     "error": "The page you are looking for does not exist"
#                 })            


def add(request):

    entries = util.list_entries()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(f'title:{title}')
        print(f'content:{content}')
        if title in entries:
            return render(request, "encyclopedia/add.html", {
                'available': True
                # page already exists
            })
        else:
            util.save_entry(title, content)
            return redirect(wiki, title=title)
    return render(request, "encyclopedia/add.html", {
        'available': False

    })

def edit(request, title):
    pagecontent = util.get_entry(title)
    if request.method == 'GET':
        return render(request, "encyclopedia/edit.html", {
            'title': title,
            'content': pagecontent
        })
    if request.method == 'POST':
        pagecontent = request.POST.get('newcontent')
        util.save_entry(title, pagecontent)
        return redirect(wiki, title=title)


def random_page(request):
    entries = util.list_entries()

    # redirect to a page where the title is a random value in an array of entries
    return redirect(wiki, title=entries[random.randint(0, len(entries)-1)])  
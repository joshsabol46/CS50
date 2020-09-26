from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    if title == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize(),
            "content": util.get_entry(title)
        })

# Search #1
# def search(request):
#     if request.method =='POST':
#         response = request.POST["q"]
#         entry = util.get_entry(response)
#         if entry:
#              return HttpResponseRedirect("wiki/"+entry)
#         else:
#             entries = util.list_entries()
#             search_entries = [i for i in entries if response.lower() in i.lower()]
#             if search_entries:
#                 return render(request, 'encyclopedia/index.html',{  
#                     "entries": search_entries
#                 })
#             else:
#                 return render(request, "encyclopedia/error.html",{
#                     # "error": "The page you are looking for does not exist"
#                 })


def search(request):
    query = request.POST.get("q")
    if util.get_entry(query):
        return redirect("entry", title = query)
    else:
        all_entries = util.list_entries()
        match = []
        for i in all_entries:
            if query.lower() in i.lower():
                match.append(i)
        if len(match) == 0:
            return render(request, 'encyclopedia/error.html')
        else:
            return render(request, 'encyclopedia/wiki/search.html', {
                "results" : match,
                "search" : query
            })

def add(request):
    if request.method == "POST": # Ensures the method is POST
        header = request.POST.get("header") # Grab the header from the form input field named "header"
        content = request.POST.get("content") # Grab the content from the form input field named "content"
        test = util.get_entry(header) # Try to see if the Entry exists already by setting a test variable to = header
        if test != None: # If the header already exists, then return back to the Add entry page
            # messages.error(request,"This page already exists")
            return render(request, "encyclopedia/wiki/add.html", {
            "entries": util.list_entries() # Not sure what value this provides.
            })

        else: # Otherwise save the header and content and navigate to the new Entry page
            util.save_entry(header,content)
            # entry_new = util.get_entry(header) # Not sure what this does
            return redirect("/wiki/"+header)
    else: # Otherwise nullify the header and content values, and return to the Add entry form
        header = ""
        content = ""
        return render(request, "encyclopedia/wiki/add.html", {
            "entries": util.list_entries()
            })


def edit(request, title):
    if title == None:
        return render(request, "encyclopedia/error.html")
    else:
        if request.method == "POST": # Ensures the method is POST
            title = request.POST.get("title") # Grab the header from the form input field named "header"
            content = request.POST.get("content") # Grab the content from the form input field named "content"
            util.save_entry(title,content) # Save the header and content and navigate to the new Entry page
            return redirect("/wiki/"+title) 
            # return redirect("entry", title = title)
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": util.get_entry(title)
                })



# def edit(request, title):
#     if request.method == "POST": # Ensures the method is POST
#         header = request.POST.get("header") # Grab the header from the form input field named "header"
#         content = request.POST.get("content") # Grab the content from the form input field named "content"
#         test = util.get_entry(header) # Try to see if the Entry exists already by setting a test variable to = header
#         if test != None: # If the header already exists, then return back to the Add entry page
#             # messages.error(request,"This page already exists")
#             return render(request, "encyclopedia/wiki/add.html", {
#             "entries": util.list_entries() # Not sure what value this provides.
#             })

#         else: # Otherwise save the header and content and navigate to the new Entry page
#             util.save_entry(header,content)
#             # entry_new = util.get_entry(header) # Not sure what this does
#             return redirect("/wiki/"+header)
#     if title == None:
#         return render(request, "encyclopedia/error.html")
#     else:
#         return render(request, "encyclopedia/edit.html", {
#             "title": title,
#             "content": util.get_entry(title)
#             })

# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
# https://github.com/JTPPAT/WIKITRY2/tree/master/encyclopedia
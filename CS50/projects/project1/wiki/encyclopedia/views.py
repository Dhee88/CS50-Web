import markdown2 # type: ignore
from django.shortcuts import redirect, render  # type: ignore
from django.contrib import messages # type: ignore
from . import util
import random


def index(request):
    print("INDEX VIEW CALLED")
    entries = util.list_entries()
    print("Entries:", entries)
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request,title):
    content = util.get_entry(title)
    if content is None:
        return render(request,"encyclopedia/error.html",{
            "message": "Page not found."
        })
    return render(request,"encyclopedia/entry.html",{
        "title": title,
        "content": markdown2.markdown(content)
    })

def search(request):
    query = request.GET.get("q","")
    entries = util.list_entries()

    if query.lower() in [entry.lower() for entry in entries]:
        for entry in entries:
            if query.lower()==entry.lower():
                return redirect("entry",title=entry)
            
    results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html",{
        "results": results,
        "query": query
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()

        entries = util.list_entries()
        if title.lower() in (entry.lower() for entry in entries):
            messages.error(request,"An entry with this title already exists.")
            return render(request,"encyclopedia/create.html",{
                "title": title,
                "content": content
            })
        
        util.save_entry(title,content)
        return redirect("entry",title=title)
    return render(request, "encyclopedia/create.html")

def edit(request,title):
    if request.method =="POST":
        content = request.POST.get("content").strip()
        util.save_entry(title,content)
        return redirect("entry",title=title)
    
    content = util.get_entry(title)
    if content is None:
        return render(request,"encyclopedia/error.html",{
            "message": "Page not found for editing."
        })
    return render(request,"encyclopedia/edit.html",{
        "title":title,
        "content": content
    })

def random_page(request):
    entries  = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect("entry",title=random_entry)
    else:
        return redirect("index")
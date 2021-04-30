from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from random import randint

from . import util

class NewPageForm(forms.Form) :
    title = forms.CharField(label="Title", required = True)
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":10}), required = True)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def by_title(request, title):
    
    content = util.get_entry(title)
    if(not content):
        return render(request, "encyclopedia/page_not_found.html", {
        "title": title
    })

    return render(request, "encyclopedia/by_title.html", {
        "title": title,
        "pageContent": content
    })


def search_by_title(request):
    q = request.GET.get('q')
    return by_title(request, q)

def create_page(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewPageForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            # Save the new page
            util.save_entry(title, content)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("index"))

        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/create_page.html", {
                "form": form
            })

    return render(request, "encyclopedia/create_page.html", {
        "form": NewPageForm()
    })

def random_page(request):
    pages = util.list_entries()
    randomTitle = pages[randint(0, len(pages) - 1)]
    pageContent = util.get_entry(randomTitle)
    return render(request, "encyclopedia/by_title.html", {
        "title": randomTitle,
        "pageContent": pageContent
    })
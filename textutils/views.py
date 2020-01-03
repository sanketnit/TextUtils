
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return(render(request,'index.html'))

def analyze(request) :

    # Get text from user
    djtext = request.POST.get('text','default')

    # Checks for the functions
    removepunc = request.POST.get('removepunc','off')
    captitalize = request.POST.get('captitalize','off')
    spaceremover = request.POST.get('spaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')


    if removepunc == 'on' :
        analyzed_text = ""
        punctuations = '''!@#$%^&*()_+-=\|{}:"<>?[];',./'''
        for char in djtext :
            if char not in punctuations :
                analyzed_text = analyzed_text + char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed_text}
        djtext = analyzed_text


    if captitalize == 'on' :
        # analyzed_text = djtext.upper()
        analyzed_text = ''
        for char in djtext :
            analyzed_text = analyzed_text + char.upper()
        params = {'purpose' : 'Capitalised Text', 'analyzed_text' : analyzed_text}
        djtext = analyzed_text
    if spaceremover == 'on' :
        analyzed_text = ''
        for index, char in enumerate(djtext) :
            if not(djtext[index] == " " and djtext[index+1] == " " ):
                analyzed_text = analyzed_text + char.upper()
        params = {'purpose' : 'Extra spaces removed', 'analyzed_text' : analyzed_text}
        djtext = analyzed_text

    if newlineremover == 'on' :
        analyzed_text = ''
        for char in djtext :
            if char != "\n" and char != "\r" :
                analyzed_text = analyzed_text + char
        params = {'purpose' : 'New lines removed', 'analyzed_text' : analyzed_text}


    if (removepunc != 'on' and captitalize != 'on' and spaceremover != 'on' and newlineremover != 'on' ) :

        return HttpResponse("You have not checked any checkbox!!!")

    return render(request, 'analyze.html', params)

def about(request) :
    return render(request,'about.html')


def contact(request) :
    return render(request,'contact.html')


# I have created this file(Deb)
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    ddtext=request.POST.get('text','default')
    #print(ddtext)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in ddtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuations','analyze_text': analyzed }
        ddtext=analyzed
    if(fullcaps=="on"):
        analyzed =""
        for char in ddtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'CHANGED TO UPPER CASE', 'analyze_text': analyzed}
        ddtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in ddtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyze_text': analyzed}
        ddtext = analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(ddtext):
            if not (ddtext[index] == " " and ddtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyze_text': analyzed}
        ddtext = analyzed
    if(charactercounter=="on"):
        analyzed=len(ddtext)
        params = {'purpose': 'No Of Character In String Is', 'analyze_text': analyzed}
        ddtext = analyzed
    if (removepunc != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and charactercounter != "on" ):
        return HttpResponse("Please Select Any Option and Try Again")

    return render(request, 'analyze.html', params)
#created self not by default
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h1>Hello Aftab!<h1/>")
    params = {'name': 'Aftab', 'place': 'Bhandup'}
    return render(request, 'index.html', params)
def removepunc(request):
    rtext = request.POST.get('text','defaut')
    rpunc = request.POST.get('removepunc','off')
    rcount = request.POST.get('charcount','off')
    rcap = request.POST.get('capsall','off')
    rline = request.POST.get('linerem','off')
    anaText = ""
    punctuations = '''!()-[]{}:;'"<>,/?|/@#$%^&*!_~`'''

    if rpunc== "on":
        for char in rtext:
            if char not in punctuations:
                anaText = anaText + char
        params = {  'purpose':'Removed Punctuations',
                'analyzedText': anaText
    }
        return render(request, 'removepunc.html', params)
    elif rcount=="on":
        i=0
        j=0
        for char in rtext:
            j= j+1
            if char not in punctuations:
                i = i+1
            
        
        params = {  'purpose':'Character Counts',
                'mode': "on",
                'analyzedText1': i,
                'analyzedText2': j,}
        return render(request, 'removepunc.html', params)
    
    elif rcap == "on":
        for char in rtext:
            if char not in punctuations:
                anaText = anaText + char.upper()
        params = {  'purpose':'Puctuation Removed And Capitalized All Words',
                'analyzedText': anaText
                }
        return render(request, 'removepunc.html', params)
    
    elif rline == "on":
        for char in rtext:
            if char != "\n" and char != "\r":
                anaText = anaText + char
        params = {  'purpose':'New Line Removed',
                'analyzedText': anaText
    }
        return render(request, 'removepunc.html', params)

    else:
        anaText = "Sorry no text found"
    
    return HttpResponse("Error")

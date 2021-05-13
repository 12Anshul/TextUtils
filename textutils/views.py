from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request,'intro.html')


def intro(request):
    return render(request, 'intro.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_data = ""
        for char in djtext:
            if char not in punctuations:
                analyzed_data = analyzed_data+char
        params = {'purpose':'Analyze Text', 'analyzed': analyzed_data}
        djtext = analyzed_data
       # return render(request, 'analyze.html', params)
    if(capitalize=='on'):
        analyzed_data=""
        for char in djtext:
            analyzed_data=analyzed_data+char.upper()
        params = {'purpose': 'Capitalize The Text', 'analyzed': analyzed_data}
        djtext = analyzed_data
        #return render(request, 'analyze.html', params)
    if (newlineremover == 'on'):
        analyzed_data = ""
        for char in djtext:
            if char != '\n' and char!= '\r':
                analyzed_data = analyzed_data + char
        params = {'purpose': 'Capitalize The Text', 'analyzed': analyzed_data}
        djtext = analyzed_data
        #return render(request, 'analyze.html', params)
    if (extraspace == 'on'):
        analyzed_data = ""
        for index ,char in enumerate(djtext):
            if not(djtext[index] == '' and djtext[index+1]==''):
                analyzed_data = analyzed_data + char.upper()
        params = {'purpose': 'Capitalize The Text', 'analyzed': analyzed_data}
        djtext = analyzed_data
        #return render(request, 'analyze.html', params)
    if (charcount=='on'):
        return HttpResponse(len(djtext))
    if (removepunc != 'on' and capitalize !='on'and extraspace !='on' and newlineremover !='on'):
        return HttpResponse("Error")

    return render(request,'analyze.html',params)

#def hel(request):
  #  dj = request.GET.get('text', 'default')
   # print(dj)
    #return HttpResponse('Hello this is'+ dj)

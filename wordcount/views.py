from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dictionary={}
    for x in words:
        if x in word_dictionary:
            word_dictionary[x]=word_dictionary[x]+1
        else:
            word_dictionary[x]=1
    return render(request,'result.html',{ 'absd':text, 'temp':1,'textlen':len(text),'total':len(words), 'dict':word_dictionary.items()})

def umm(request):
    ang=request.GET['fulltext']
    um=request.GET['um']
    do=request.GET['do']
    output=ang.replace(str(um),str(do))
    return render(request,'umm.html',{'output':output,})
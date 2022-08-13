from re import L
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import Courses, Optii


MATH = [(val.id,val.className) for val in Courses.objects.filter(classType="Mathematics")]
SCIENCE = [(val.id,val.className) for val in Courses.objects.filter(classType="Science")]
SOCIAL_STUDIES = [(val.id,val.className) for val in Courses.objects.filter(classType="Social Studies")]
LANGUAGE_ARTS = [(val.id,val.className) for val in Courses.objects.filter(classType="Language Arts")]
LANGUAGE = [(val.id,val.className) for val in Courses.objects.filter(classType="Language")]
ELECTIVE = [(val.id,val.className) for val in Courses.objects.filter(classType="Elective")]
OPT2_CHOICES = [(val.id,val.crsName) for i,val in enumerate(Optii.objects.all())]
class ClassForm(forms.Form):
    opt = forms.CharField(label="Option ii", widget=forms.Select(choices=OPT2_CHOICES))
    math = forms.CharField(label = "Math", widget=forms.Select(choices=MATH))
    science = forms.CharField(label = "Science", widget=forms.Select(choices=SCIENCE))
    languageArts = forms.CharField(label = "Language Arts", widget=forms.Select(choices=LANGUAGE_ARTS))
    socialStudies = forms.CharField(label = "Social Studies", widget=forms.Select(choices=SOCIAL_STUDIES))
    elective = forms.CharField(label = "Elective", widget=forms.Select(choices=ELECTIVE))
    language = forms.CharField(label = "World Language", widget=forms.Select(choices=LANGUAGE))
    gym = forms.CharField(required=False, disabled=True,label="PE", widget=forms.TextInput({"value":"PE"}))
    studyHall = forms.CharField(required=False, disabled=True,label="Study Hall", widget=forms.TextInput({"value":"Study Hall"}))


def index(request):
    if "freshman" not in request.session:  
        request.session["freshman"] = {}
        request.session["freshman"]["Comp"] = False
    if "sophomore" not in request.session:
        request.session["sophomore"] = {}
        request.session["sophomore"]["Comp"] = False
    if "junior" not in request.session:
        request.session["junior"] = {}
        request.session["junior"]["Comp"] = False
    if "senior" not in request.session:
        request.session["senior"] = {}
    

    return render(request,"Schedule_Map/index.html",{
        "freshman" : request.session["freshman"],
        "sophomore" : request.session["sophomore"],
        "junior" : request.session["junior"],
        "senior" : request.session["senior"],
        "ninth" : "freshman",
        "tenth" : "sophomore",
        "eleventh" : "junior",
        "twelfth" : "senior",
        "9thComp" : request.session["freshman"]["Comp"],
        "10thComp" : request.session["sophomore"]["Comp"],
        "11thComp" : request.session["junior"]["Comp"],
        
    })

def setSched(request,yr):
    for i,k in enumerate(request.session.keys()):
        if i == 3:
            break
        if not(request.session[k]['Comp']) and yr == list(request.session.keys())[i+1]:
            return HttpResponseRedirect(reverse("Schedule_Map:index"))
    if yr not in request.session:
        return HttpResponseRedirect(reverse("Schedule_Map:index"))
    if request.method == "POST":

        form = ClassForm(request.POST)

        if form.is_valid():
            if yr == "freshman":
                request.session[yr]["Comp"] = True
            elif yr == "sophomore":
                request.session[yr]["Comp"] = True
            elif yr == "junior":
                request.session[yr]["Comp"] = True
            opt = form.cleaned_data["opt"]
            request.session[yr]["opt"] = Optii.objects.get(id=opt).crsName
            math = form.cleaned_data["math"]
            request.session[yr]["math"] = Courses.objects.get(pk=math).className
            language = form.cleaned_data["language"]
            request.session[yr]["language"] = Courses.objects.get(pk=language).className
            
            science = form.cleaned_data["science"]
            languageArts = form.cleaned_data["languageArts"]
            socialStudies = form.cleaned_data["socialStudies"]
            elective = form.cleaned_data["elective"]
            gym = form.cleaned_data["gym"]
            studyHall = form.cleaned_data["studyHall"]
            request.session[yr]["science"] = Courses.objects.get(pk=science).className
            request.session[yr]["languageArts"] = Courses.objects.get(pk=languageArts).className
            request.session[yr]["socialStudies"] = Courses.objects.get(pk=socialStudies).className
            request.session[yr]["elective"] = Courses.objects.get(pk=elective).className
            request.session[yr]["gym"] = "PE"
            request.session[yr]["studyHall"] = "Study Hall"
            request.session.modified = True
            return HttpResponseRedirect(reverse("Schedule_Map:index"))
        else:
            return render(request,"Schedule_Map/setSched.html", {
                "form": form,
                "grade":yr
            })


    return render(request,"Schedule_Map/setSched.html", {
        "grade":yr,
        "form": ClassForm()
    })

    

            
from django.shortcuts import render, redirect
from .models import Header, Home, FeaturedServices, Title, About, AboutContent, Skill, Statistic, Client, Service
from .models import Testimonial, Categories, Portfolio, Team, Pricing, FAQ, Info, ContactInfo, Contact, Subscribe
from .forms import ContactModelForm, SubscribeModelForm

# Create your views here.

def index(request):
    header = Header.objects.first()
    home = Home.objects.first()
    featured_services = FeaturedServices.objects.all()
    titles = Title.objects.first()
    about = About.objects.first()
    about_content = AboutContent.objects.all()
    skills = Skill.objects.all()
    statistics = Statistic.objects.all()
    clients = Client.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Categories.objects.all()
    portfolio = Portfolio.objects.all()
    team = Team.objects.all()
    pricing = Pricing.objects.all()
    faq = FAQ.objects.all()
    infos = Info.objects.all()
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        form2 = SubscribeModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('/')
        if form2.is_valid():
            Subscribe.objects.create(**form2.cleaned_data)
            return redirect('/')
    else:
        form = ContactModelForm()
        form2 = SubscribeModelForm()

    return render(request, 'index.html', context={
        'header' : header,
        'home':home,
        'featured_services':featured_services,
        'titles':titles,
        'about':about,
        'about_content':about_content,
        'skills':skills,
        'statistics':statistics,
        'clients':clients,
        'services':services,
        'testimonials':testimonials,
        'categories':categories,
        'portfolio':portfolio,
        'team':team,
        'pricing':pricing,
        'faq':faq,
        'infos':infos,
        'contact_info':contact_info,
    })
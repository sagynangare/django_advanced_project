from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import *


class HomePage(TemplateView):
    template_name = 'guitarApp/homepage.html'


    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['guitar'] = AboutGuitar.objects.all()
        return context


class VideosPage(TemplateView):
    template_name = 'guitarApp/videos.html'

    def get_context_data(self, **kwargs):
        context = super(VideosPage, self).get_context_data(**kwargs)
        context['videos'] = YoutubeVideos.objects.all()
        return context

class Guitardetails(ListView):
    template_name = 'guitarApp/aboutguitar_detail.html'
    model = AboutGuitar

    def get_context_data(self, **kwargs):
        context = super(Guitardetails, self).get_context_data(**kwargs)
        context['guitar'] = AboutGuitar.objects.all()
        return context


class Detail_Guitar(DetailView):
    model = AboutGuitar
    template_name = 'guitarApp/aboutguitar_detail.html'



class Admission(TemplateView):
    template_name = 'guitarApp/admission.html'



class BatchesPage(ListView):
    template_name = 'guitarApp/batches.html'
    model = Batches
    def get_context_data(self, **kwargs):
        context = super(BatchesPage, self).get_context_data(**kwargs)
        context['Batches'] = Batches.objects.all()
        return context



class ContactPage(TemplateView):
    template_name = 'guitarApp/contact.html'

class AboutPage(TemplateView):
    template_name = 'guitarApp/aboutus.html'


class feestructurePage(ListView):
    model = Feestructure
    template_name = 'guitarApp/feestructure.html'

    def get_context_data(self, **kwargs):
        context = super(feestructurePage, self).get_context_data(**kwargs)
        context['Feestructure'] = Feestructure.objects.all()
        return context


class BuyguitarPage(ListView):
    template_name = 'guitarApp/buyguitar.html'
    model = Buyguitar

    def get_context_data(self, **kwargs):
        context = super(BuyguitarPage, self).get_context_data(**kwargs)
        context['buyguitar'] = Buyguitar.objects.all()
        return context
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from books.models import Book


def pbadmin_index(request):
    books = Book.objects.all()
    return render_to_response('pbadmin_index.html', {"books": books})


def approve(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.beneficiary.approved = True
        user.beneficiary.save()
        return HttpResponseRedirect(reverse('unapproved'))
    return render_to_response('unapproved_users.html')


def campaigns(self):
    return HttpResponse('WOw')


def create_a_campaign(self):
    return render_to_response('create_a_campaign.html')

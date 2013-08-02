from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.urlresolvers import reverse

from books.models import Book
from profiles.tasks import sendemail


def approve(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user:
        user.beneficiary.is_approved = True
        user.beneficiary.save()
        sendemail(sub="approve_sub", msg="approve_msg",
                  to=user.email, user=user)
        return HttpResponseRedirect(reverse('customadmin:unapproved'))
    return render_to_response('unapproved_users.html')


class UnapprovedUsers(ListView):
    template_name = 'customadmin/unapproved_users.html'
    context_object_name = 'unapproved_users'

    def get_queryset(self):
        """
        Returns the unapproved users related to beneficiary in
        the database

        """

        return User.objects.filter(beneficiary__is_approved=False)


class CustomAdminIndex(ListView):
    template_name = 'customadmin/customadmin_index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()

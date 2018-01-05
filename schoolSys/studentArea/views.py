from django.shortcuts import render, get_list_or_404

# Create your views here.


def cust_login(request):
    return render(request, 'admin/cust_login.html')


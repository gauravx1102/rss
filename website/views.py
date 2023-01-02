import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage


from .models import Contact, Document


def index(request):
    records = Document.objects.all().order_by('-id')[:3]
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
    context = {
        'records' : records,
        'is_latest_record': is_latest_record,
    }
    return render(request,'website/home.html', context)


def notice(request):
    records = Document.objects.all().order_by('-id')
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
    context = {
        'records' : records,
        'is_latest_record': is_latest_record,
    }
    return render(request,'website/notice.html', context)


def ask_your_query(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        school_name = request.POST.get('school_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        base_url = f"{ request.scheme }://{ request.META.get('HTTP_HOST') }"

        contact.name = name
        contact.school_name = school_name
        contact.phone = phone
        contact.email = email
        contact.message = message
        contact.file_url = "{}{}".format(base_url, uploaded_file_url)
        contact.save()

        # subject = 'New Query from Website'
        # message = "Name: {} <br>, School Name: {} <br>, Phone: {} <br>, Email: {} <br>, Message: {}"
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['rsswebsite2022@gmail.com']
        # send_mail(subject, message, email_from, recipient_list)

        # return render(request, 'website/success.html')
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
        context = {
            'is_latest_record': is_latest_record,
        }
        return render(request,'website/success.html', context)

    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
    context = {
        'is_latest_record': is_latest_record,
    }
    return render(request,'website/ask_your_query.html', context)


def contact(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
    context = {
        'is_latest_record': is_latest_record,
    }
    return render(request,'website/contact.html', context)


def about_us(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    is_latest_record = Document.objects.filter(created_at__gte=date_from).count()
    context = {
        'is_latest_record': is_latest_record,
    }
    return render(request,'website/about_us.html', context)


def send_email(request):
    return

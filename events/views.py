from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Event, Registration
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('event_list')

    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,f'Hoş geldiniz,{user.username}! Kaydınız başarıyla tamamlandı.')
            return redirect('event_list')

    else:
        form=RegisterForm()
    return render(request,'events/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # <-- form.user yerine form.get_user() olmalı
            login(request, user)
            messages.success(request, f'Hoş geldiniz, {user.username}!')
            return redirect('event_list')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request,'Başarıyla çıkış yaptınız.')
    return redirect('login')

def event_list_view(request):
    query = request.GET.get('q', '').strip()
    now = timezone.now()

    
    events = Event.objects.all().order_by('date')

    
    if query:
        events = events.filter(
            Q(title__icontains=query) | Q(location__icontains=query)
        )

    user_registered_event_ids = []
    if request.user.is_authenticated:
        user_registered_event_ids = list(Registration.objects.filter(
            user=request.user
        ).values_list('event_id', flat=True))

    context = {
        'events': events,
        'user_registered_event_ids': user_registered_event_ids,
        'query': query,
        'now': now,
    }
    return render(request, 'events/event_list.html', context)

    context={
        'events':events,
        'user_registered_event_ids':user_registered_event_ids,
    }

    return render(request,'events/event_list.html',context)

@login_required(login_url='login')
def register_event_view(request, event_id):
    
    event = get_object_or_404(Event, id=event_id)

    
    if event.is_past:
        messages.error(request, f'"{event.title}" etkinliğinin tarihi geçtiği için kayıt olunamaz.')
        return redirect('event_list')

    
    if Registration.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, f'"{event.title}" etkinliğine zaten kayıtlısınız.')
        return redirect('event_list')

    
    if event.is_full:
        messages.error(request, f'Üzgünüz, "{event.title}" için kontenjan dolmuştur!')
        return redirect('event_list')

    
    Registration.objects.create(user=request.user, event=event)
    messages.success(request, f'Tebrikler! "{event.title}" etkinliğine kaydınız başarıyla alındı.')
    return redirect('event_list')

@login_required(login_url='login')
def my_registrations_view(request):
    registrations=Registration.objects.filter(user=request.user).select_related('event').order_by('-registered_at')
    return render(request,'events/my_registrations.html',{'registrations':registrations})

@login_required(login_url='login')
def cancel_registration_view(request,registration_id):
    registration=get_object_or_404(Registration,id=registration_id,user=request.user)
    event_title=registration.event.title
    registration.delete()
    messages.info(request,f'"{event_title}" etkinliği için kaydınız iptal edildi')
    return redirect('my_registrations')
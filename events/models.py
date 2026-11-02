from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='organized_events',verbose_name='Organizatör')
    title=models.CharField(max_length=200,verbose_name='Etkinlik Başlığı')
    description=models.TextField(verbose_name='Açıklama')
    location=models.CharField(max_length=200,verbose_name='Konum / Yer')
    date=models.DateTimeField(verbose_name='Etkinlik Traihi ve Saati')
    capacity=models.PositiveIntegerField(verbose_name='Kontenjan')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.title

    @property
    def registered_count(self):
        return self.registrations.count()

    @property
    def remaining_capacity(self):
        return max(0,self.capacity-self.registered_count)

    @property
    def is_full(self):
        return self.registered_count >= self.capacity

    class Meta:
        ordering=['date']
        verbose_name='Etkinlik'
        verbose_name_plural='Etkinlikler'

class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='registrations',verbose_name='Kullanıcı')
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='registrations',verbose_name='Etkinlik')
    registered_at=models.DateTimeField(auto_now_add=True,verbose_name='Kayıt Tarihi')

    class Meta:
        unique_together=('user','event')
        verbose_name='Etkinlik Kaydı'
        verbose_name_plural='Etkinlik Kayıtları'

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"
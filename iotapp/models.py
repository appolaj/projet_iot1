from django.db import models
from django.core.mail import send_mail
import telepot
# Create your models here.
from django.db import models


class Dht(models.Model):
 temp = models.FloatField(null=True)
 hum = models.FloatField(null=True)
 dt = models.DateTimeField(auto_now_add=True,null=True)
 def __str__(self):
  return str(self.temp)

 def save(self, *args, **kwargs):
  if self.temp < 2 :
   #send message sur telegram
   token = '5836647326:AAGdsf_gGOjyos9qUa1D1Bkkf2jtlE_0-Cw'
   rece_id = 2025982008
   bot = telepot.Bot(token)
   bot.sendMessage(rece_id, 'Attention!')
   print(bot.sendMessage(rece_id, 'temperature severe:' + str(self.temp) ))
  # print(bot.sendMessage(rece_id, 'OK.'))

   send_mail(
    'temperature dépasse la normale: ' + str(self.temp),
    'anomalie dans la machine le ,' + str(self.dt),
    'ayoub.belhaj1@ump.ac.ma',
    ['ayoub5belhaj@gmail.com'],
    fail_silently=False,
   )


   #if self.temp < 12:
    # send message sur telegram
    #token = '5836647326:AAGdsf_gGOjyos9qUa1D1Bkkf2jtlE_0-Cw'
    #rece_id = 2025982008
    #bot = telepot.Bot(token)
    #bot.sendMessage(rece_id, 'Attention!')
    #print(bot.sendMessage(rece_id, 'temperature critique:' + str(self.temp)))
    # print(bot.sendMessage(rece_id, 'OK.'))

    #send_mail(
     #'temperature dépasse la normale: ' + str(self.temp),
     #'anomalie dans la machine le ,' + str(self.dt),
     #'ayoub.belhaj1@ump.ac.ma',
     #['ayoub5belhaj@gmail.com'],
     #fail_silently=False,
    #)
  return super(Dht, self).save(*args, **kwargs)






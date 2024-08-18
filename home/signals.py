from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        group_name = 'usuarios_comuns'
        
        try:
            group = Group.objects.get(name=group_name)
            instance.groups.add(group)
        except Group.DoesNotExist:
            print(f'Grupo "{group_name}" não encontrado.')
        
        instance.is_staff = True
        instance.save()




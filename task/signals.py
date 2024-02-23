from django.db.models.signals import post_save
from django.db.backends.signals import connection_created
from django.dispatch import receiver
from django.utils import timezone
from user_manager.models import CustomUser
from task.models import Task, Tag, Priority


@receiver(post_save, sender=CustomUser)
def create_default_tags_and_priorities(sender, instance, created, **kwargs):
    if created:
        default_tag = 'Tarea'
        Tag.objects.create(tag_name=default_tag, owner_tag=instance)
        
        default_prioritie = 'Normal'
        Priority.objects.create(priority_level=default_prioritie, owner_priority=instance)


@receiver(connection_created)
def update_expired_tasks(sender, **kwargs):

    current_time = timezone.now()
    expired_tasks = Task.objects.filter(status__in=['Pendiente', 'En progreso'], deadline__lt=current_time)
    expired_tasks.update(status='Expirada')


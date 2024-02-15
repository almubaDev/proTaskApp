from django.db.models.signals import post_save
from django.dispatch import receiver
from user_manager.models import CustomUser
from task.models import Tag, Priority

@receiver(post_save, sender=CustomUser)
def create_default_tags_and_priorities(sender, instance, created, **kwargs):
    if created:
        default_tag = 'Tarea'
        Tag.objects.create(tag_name=default_tag, owner_tag=instance)
        
        default_prioritie = 'Normal'
        Priority.objects.create(priority_level=default_prioritie, owner_priority=instance)

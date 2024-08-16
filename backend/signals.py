from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FlotaDP, DiarioDePesca

@receiver(post_save, sender=FlotaDP)
def update_diario_pesca(sender, instance, **kwargs):
    # Obtener todos los registros de DiarioDePesca relacionados con este FlotaDP
    diarios = DiarioDePesca.objects.filter(flotaDP_id=instance)
    
    # Actualizar los campos relevantes en DiarioDePesca
    for diario in diarios:
        diario.embarcacion = instance.embarcacion.id
        diario.fecha = instance.fecha
        diario.zona_pesca = instance.zona_pesca
        diario.p_flota_dolares = instance.costo_cap_x_dolar
        diario.t_flota = instance.toneladas_recibidas
        # Actualiza otros campos según sea necesario
        diario.save()
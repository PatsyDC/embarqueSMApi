
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models 
import os
from datetime import datetime
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, dni, nombrey_apellido, password=None, **extra_fields):
        if not dni:
            raise ValueError('El DNI es obligatorio')
        user = self.model(dni=dni, nombrey_apellido=nombrey_apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, nombrey_apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(dni, nombrey_apellido, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_ADMIN = 'ADMIN'
    USER_TYPE_EMBARCACIONES = 'Embarcaciones'
    USER_TYPE_PROCESO = 'Proceso'
    
    USER_TYPE_CHOICES = [
        (USER_TYPE_ADMIN, 'Admin'),
        (USER_TYPE_EMBARCACIONES, 'Embarcaciones'),
        (USER_TYPE_PROCESO, 'Proceso'),
    ]

    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    idgeneral = models.CharField(max_length=50, blank=True, null=True)
    nombrey_apellido = models.CharField(max_length=100)
    imagen_usuario = models.ImageField(upload_to='usuarios', blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    tipo_usurio = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombrey_apellido']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombrey_apellido


class Embarcaciones(models.Model):
    nombre = models.CharField(max_length=255)
    costo_zarpe = models.DecimalField(max_digits=8, decimal_places=2)
    bonificacion = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    fecha = models.DateField()
    boner = models.DecimalField(max_digits=8, decimal_places=2)

class Especies(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    fecha = models.DateField()

class ZonaPesca(models.Model):
    nombre = models.CharField(max_length=255)

class TarifasCostos(models.Model):
    nombre_t = models.CharField(max_length=255)
    tarifa = models.DecimalField(max_digits=9, decimal_places=4)

class Viveres(models.Model):
    embarcacion = models.ForeignKey(Embarcaciones,on_delete=models.CASCADE)
    costo_zarpe = models.DecimalField(max_digits=5, decimal_places=2)

class MecanismosI(models.Model):
    item = models.CharField(max_length=255)
    costo_dia = models.DecimalField(max_digits=5, decimal_places=2)

class CostoGalonB_05(models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=11, decimal_places=3)

class CostoGalonHielo(models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=11, decimal_places=3)

class CostoGalonAgua(models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=11, decimal_places=3)

class CostoTipoCambio(models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=11, decimal_places=3)

class FlotaDP(models.Model):                                                      
    fecha = models.DateField()
    tipo_cambio = models.DecimalField(max_digits=9, decimal_places=2)
    embarcacion = models.ForeignKey(Embarcaciones,on_delete=models.CASCADE)
    zona_pesca = models.ForeignKey(ZonaPesca,on_delete=models.CASCADE)
    horas_faena = models.CharField(max_length=255)
    kilos_declarados = models.DecimalField(max_digits=9, decimal_places=2)
    especie = models.JSONField()
    otro = models.CharField(max_length=255, null=True, blank=True)
    kilo_otro = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    precio_otro = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True) #
    toneladas_procesadas= models.DecimalField(max_digits=9, decimal_places=2)
    toneladas_recibidas = models.DecimalField(max_digits=9, decimal_places=2)
    costo_basico = models.DecimalField(max_digits=9, decimal_places=2) #
    participacion = models.DecimalField(max_digits=9, decimal_places=2) #
    bonificacion = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True) #
    total_participacion = models.DecimalField(max_digits=9, decimal_places=2)#
    aporte_REP= models.DecimalField(max_digits=9, decimal_places=2)#
    gratificacion = models.DecimalField(max_digits=9, decimal_places=2)#
    vacaciones = models.DecimalField(max_digits=9, decimal_places=2)#
    cts = models.DecimalField(max_digits=9, decimal_places=2)#
    essalud = models.DecimalField(max_digits=9, decimal_places=2)#
    senati = models.DecimalField(max_digits=9, decimal_places=2)#
    SCTR_SAL = models.DecimalField(max_digits=9, decimal_places=2)#
    SCTR_PEN = models.DecimalField(max_digits=9, decimal_places=2)#
    poliza_seguro = models.DecimalField(max_digits=9, decimal_places=2)#
    total_tripulacion =  models.DecimalField(max_digits=9, decimal_places=2)
    consumo_gasolina = models.DecimalField(max_digits=9, decimal_places=2)
    costo_gasolina = models.DecimalField(max_digits=9, decimal_places=2)#
    total_gasolina = models.DecimalField(max_digits=9, decimal_places=2)
    galon_hora = models.DecimalField(max_digits=9, decimal_places=2) #
    consumo_hielo = models.DecimalField(max_digits=9, decimal_places=2)
    total_hielo = models.DecimalField(max_digits=9, decimal_places=2)
    costo_hilo = models.DecimalField(max_digits=9, decimal_places=2)#
    consumo_agua = models.DecimalField(max_digits=9, decimal_places=2)
    costo_agua = models.DecimalField(max_digits=9, decimal_places=2)#
    total_agua = models.DecimalField(max_digits=9, decimal_places=2)
    consumo_viveres = models.DecimalField(max_digits=9, decimal_places=2)
    total_vivieres = models.DecimalField(max_digits=9, decimal_places=2)
    dias_inspeccion = models.DecimalField(max_digits=9, decimal_places=2)
    total_servicio_inspeccion = models.DecimalField(max_digits=9, decimal_places=2)
    total_derecho_pesca = models.DecimalField(max_digits=9, decimal_places=2)
    total_costo = models.DecimalField(max_digits=9, decimal_places=2)
    costo_tm_captura = models.DecimalField(max_digits=9, decimal_places=2)
    csot = models.DecimalField(max_digits=9, decimal_places=2)
    ###
    toneladas_procesadas_produccion= models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    toneladas_NP = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'{self.fecha} - {self.embarcacion} - {self.zona_pesca}'

class DiarioDePesca(models.Model):
    embarcacion = models.IntegerField()  
    especie = models.IntegerField()
    fecha = models.DateField()
    numero_alcance = models.IntegerField()
    zona_pesca = models.ForeignKey(ZonaPesca,on_delete=models.CASCADE)
    estrato = models.CharField(max_length=255)
    profundidad = models.IntegerField()
    tiempo_efectivo = models.TimeField()
    rango_talla_inicial = models.IntegerField()
    rango_talla_final = models.IntegerField()
    moda = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=9, decimal_places=2)
    ar = models.IntegerField()
    numero = models.IntegerField()
    flotaDP_id = models.ForeignKey(FlotaDP,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.embarcacion} - {self.fecha}"

class CostoTripulacion(models.Model):
    costo_basico = models.DecimalField(max_digits=9, decimal_places=2)
    participacion = models.DecimalField(max_digits=9, decimal_places=2)
    bonificacion = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    total_participacion = models.DecimalField(max_digits=9, decimal_places=2)
    aporte_REP= models.DecimalField(max_digits=9, decimal_places=2)
    gratificacion = models.DecimalField(max_digits=9, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=9, decimal_places=2)
    CTS = models.DecimalField(max_digits=9, decimal_places=2)
    ESSALUD = models.DecimalField(max_digits=9, decimal_places=2)
    SENATI = models.DecimalField(max_digits=9, decimal_places=2)
    SCTR_SAL = models.DecimalField(max_digits=9, decimal_places=2)
    SCTR_PEN = models.DecimalField(max_digits=9, decimal_places=2)
    poliza_seguro = models.DecimalField(max_digits=9, decimal_places=2)
    total_CT = models.DecimalField(max_digits=9, decimal_places=2)

class ConsumoGasolina(models.Model):
    embarcacion = models.IntegerField()
    consumo_gasolina = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2) 

class DerechoPesca(models.Model):
    item = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=9, decimal_places=2) 

class ToneladasProduccion(models.Model):
    dni = models.CharField(max_length=8, null=True, blank=True)
    fecha = models.DateField()
    embarcacion = models.ForeignKey(Embarcaciones,on_delete=models.CASCADE)
    zona_pesca = models.ForeignKey(ZonaPesca,on_delete=models.CASCADE)
    toneladas_procesables = models.DecimalField(max_digits=9, decimal_places=2)
    toneladas_procesadas= models.DecimalField(max_digits=9, decimal_places=2)
    toneladas_NP = models.DecimalField(max_digits=9, decimal_places=2)



#class Consumo(models.Model):
    #consumo_gasolina = models.DecimalField(max_digits=9, decimal_places=2)
    #consumo_hielo = models.DecimalField(max_digits=9, decimal_places=2)
    #consumo_agua = models.DecimalField(max_digits=9, decimal_places=2)
    

from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.db.models.functions import TruncWeek, TruncMonth
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes

#------------Usuario--------------------
from rest_framework.views import APIView
class UserListCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#------------token--------------------

@api_view(['POST'])
@parser_classes([JSONParser, FormParser])
def obtain_tokens(request):
    if request.method == 'POST':
        dni = request.data.get('dni')
        password = request.data.get('password')

        # Validación básica de los datos de entrada
        if not dni or not password:
            return Response({'error': 'Debe proporcionar DNI y contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        # Autenticación del usuario
        user = authenticate(request, username=dni, password=password)

        if user is None:
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generar tokens de acceso y refresh
        refresh = RefreshToken.for_user(user)
        tokens = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

        return Response(tokens, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUser(request):
    user = request.user

    # Obtener la URL completa de la imagen
    full_image_url = None
    if user.imagen_usuario:
        full_image_url = request.build_absolute_uri(user.imagen_usuario.url)

    # Serializar el usuario con la URL completa de la imagen
    user_data = CustomUserSerializer(user, context={'request': request}).data
    user_data['imagen_usuario'] = full_image_url

    return Response(user_data) 

# DIARIO DE PESCA
class DiarioDePescaListView(generics.ListCreateAPIView):
    queryset = DiarioDePesca.objects.all()
    serializer_class = DiarioDePescaSerializer

class DiarioDePescaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiarioDePesca.objects.all()
    serializer_class = DiarioDePescaSerializer

class DiarioDePescaDeleteView(generics.DestroyAPIView):
    queryset = DiarioDePesca.objects.all()
    serializer_class = DiarioDePescaSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

#embarcaciones
class EmbarcacionesListCreateView(generics.ListCreateAPIView):
    queryset = Embarcaciones.objects.all()
    serializer_class = EmbarcacionesSerializer

class EmbarcacionesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Embarcaciones.objects.all()
    serializer_class = EmbarcacionesSerializer

#especies
class EspeciesListCreateView(generics.ListCreateAPIView):
    queryset = Especies.objects.all()
    serializer_class = EspeciesSerializer

class EspeciesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especies.objects.all()
    serializer_class = EspeciesSerializer

class EspeciesPrecioView(generics.GenericAPIView):
    queryset = Especies.objects.all()
    serializer_class = EspeciesSerializer

    def get(self, request, *args, **kwargs):
        nombre = self.kwargs['nombre']
        try:
            especie = Especies.objects.get(nombre=nombre)
            # Aquí asumimos que tienes un campo 'precio' en tu modelo Especies
            precio = especie.precio
            return Response({'precio': precio}, status=status.HTTP_200_OK)
        except Especies.DoesNotExist:
            return Response({'error': 'Especie no encontrada'}, status=status.HTTP_404_NOT_FOUND)

#Zona Pesca
class ZonaPescaListCreateView(generics.ListCreateAPIView):
    queryset = ZonaPesca.objects.all()
    serializer_class = ZonaPescaSerializer

#TarifaCosto
class TarifaCostoListCreateView(generics.ListCreateAPIView):
    queryset = TarifasCostos.objects.all()
    serializer_class = TarifasCostosSerializer

class TarifaCostoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TarifasCostos.objects.all()
    serializer_class = TarifasCostosSerializer

class TarifaCostoView(generics.GenericAPIView):
    queryset = TarifasCostos.objects.all()
    serializer_class = TarifasCostosSerializer

    def get(self, request, *args, **kwargs):
        nombre_t = self.kwargs['nombre_t']
        try:
            tarifas_costo = TarifasCostos.objects.get(nombre_t=nombre_t)
            # Utilizamos el campo 'tarifa' del modelo TarifasCostos
            tarifa = tarifas_costo.tarifa
            return Response({'tarifa': tarifa}, status=status.HTTP_200_OK)
        except TarifasCostos.DoesNotExist:
            return Response({'error': 'Tarifa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

#viveres
class ViveresListCreateView(generics.ListCreateAPIView):
    queryset = Viveres.objects.all()
    serializer_class = ViveresSerializer

#mecanismo
class MecanismoListCreateView(generics.ListCreateAPIView):
    queryset = MecanismosI.objects.all()
    serializer_class = MecanismosISerializer

class MecanismoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MecanismosI.objects.all()
    serializer_class = MecanismosISerializer

# ListCreateAPIView para CostoGalonB_05
class CostoGalonB_05_ListCreateView(generics.ListCreateAPIView):
    queryset = CostoGalonB_05.objects.all()
    serializer_class = CostoGalonB_05_Serializer

# RetrieveUpdateDestroyAPIView para CostoGalonB_05
class CostoGalonB_05_RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostoGalonB_05.objects.all()
    serializer_class = CostoGalonB_05_Serializer

#HIELO
class CostoHielo_ListCreateView(generics.ListCreateAPIView):
    queryset = CostoGalonHielo.objects.all()
    serializer_class = CostoHieloSerializer

class CostoHielo_RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostoGalonHielo.objects.all()
    serializer_class = CostoHieloSerializer

# ListCreateAPIView para CostoGalonAgua
class CostoGalonAguaListCreateView(generics.ListCreateAPIView):
    queryset = CostoGalonAgua.objects.all()
    serializer_class = CostoGalonAguaSerializer

# RetrieveUpdateDestroyAPIView para CostoGalonAgua
class CostoGalonAguaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostoGalonAgua.objects.all()
    serializer_class = CostoGalonAguaSerializer

# ListCreateAPIView para CostoTipoCambio
class CostoTipoCambioListCreateView(generics.ListCreateAPIView):
    queryset = CostoTipoCambio.objects.all()
    serializer_class = CostoTipoCambioSerializer

# RetrieveUpdateDestroyAPIView para CostoTipoCambio
class CostoTipoCambioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostoTipoCambio.objects.all()
    serializer_class = CostoTipoCambioSerializer

# FlotaDP
class FlotaDPListCreateView(generics.ListCreateAPIView):
    queryset = FlotaDP.objects.all()
    serializer_class = FlotaDPSerializer


class FlotaDPRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlotaDP.objects.all()
    serializer_class = FlotaDPSerializer

class FlotaDPPartialUpdateView(generics.UpdateAPIView):
    queryset = FlotaDP.objects.all()
    serializer_class = FlotaDPSerializer
    http_method_names = ['patch']  # Solo permitir el método PATCH

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Solo actualizar los campos específicos
            instance.toneladas_procesadas_produccion = serializer.validated_data.get('toneladas_procesadas_produccion', instance.toneladas_procesadas_produccion)
            instance.toneladas_NP = serializer.validated_data.get('toneladas_NP', instance.toneladas_NP)
            instance.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiarioDePescaPorFlotaView(APIView):
    def get(self, request, flota_id):
        diarios = DiarioDePesca.objects.filter(flotaDP_id=flota_id)
        serializer = DiarioDePescaSerializer(diarios, many=True)
        return Response(serializer.data)

class tonelasFlotaXTiempo(APIView):
    def get(self, request, *args, **kwargs):
        # Agrupar por semana
        toneladas_semanal = FlotaDP.objects.annotate(week=TruncWeek('fecha')).values('week').annotate(
            total_toneladas_recibidas=Sum('toneladas_recibidas'),
            total_toneladas_procesadas=Sum('toneladas_procesadas')
        ).order_by('week')

        # Calcular porcentaje para cada semana
        for data in toneladas_semanal:
            if data['total_toneladas_recibidas'] > 0:
                data['porcentaje_procesadas'] = round(
                    (data['total_toneladas_procesadas'] / data['total_toneladas_recibidas']) * 100 , 2
                )
            else:
                data['porcentaje_procesadas'] = 0

        # Agrupar por mes
        toneladas_mensual = FlotaDP.objects.annotate(month=TruncMonth('fecha')).values('month').annotate(
            total_toneladas_recibidas=Sum('toneladas_recibidas'),
            total_toneladas_procesadas=Sum('toneladas_procesadas')
        ).order_by('month')

        # Calcular porcentaje para cada mes
        for data in toneladas_mensual:
            if data['total_toneladas_recibidas'] > 0:
                data['porcentaje_procesadas'] = round(
                    (data['total_toneladas_procesadas'] / data['total_toneladas_recibidas']) * 100, 2
                )
            else:
                data['porcentaje_procesadas'] = 0

        # Devolver los resultados como JSON
        data = {
            'semanal': list(toneladas_semanal),
            'mensual': list(toneladas_mensual)
        }
        return JsonResponse(data)

class FlotasConLancesView(APIView):
    def get(self, request):
        response_data = []

        # Obtener todas las flotas
        flotas = FlotaDP.objects.all()
        
        # Recorrer todas las flotas
        for flota in flotas:
            # Serializar los datos de FlotaDP
            flota_data = {
                "id": flota.id,
                "fecha": flota.fecha,
                "tipo_cambio": flota.tipo_cambio,
                "horas_faena": flota.horas_faena,
                "kilos_declarados": flota.kilos_declarados,
                "otro": flota.otro,
                "kilo_otro": flota.kilo_otro,
                "precio_otro": flota.precio_otro,
                "toneladas_procesadas": flota.toneladas_procesadas,
                "toneladas_recibidas": flota.toneladas_recibidas,
                "costo_basico": flota.costo_basico,
                "participacion": flota.participacion,
                "bonificacion": flota.bonificacion,
                "total_participacion": flota.total_participacion,
                "aporte_REP": flota.aporte_REP,
                "gratificacion": flota.gratificacion,
                "vacaciones": flota.vacaciones,
                "cts": flota.cts,
                "essalud": flota.essalud,
                "senati": flota.senati,
                "SCTR_SAL": flota.SCTR_SAL,
                "SCTR_PEN": flota.SCTR_PEN,
                "poliza_seguro": flota.poliza_seguro,
                "total_tripulacion": flota.total_tripulacion,
                "consumo_gasolina": flota.consumo_gasolina,
                "costo_gasolina": flota.costo_gasolina,
                "total_gasolina": flota.total_gasolina,
                "galon_hora": flota.galon_hora,
                "consumo_hielo": flota.consumo_hielo,
                "total_hielo": flota.total_hielo,
                "costo_hilo": flota.costo_hilo,
                "consumo_agua": flota.consumo_agua,
                "costo_agua": flota.costo_agua,
                "total_agua": flota.total_agua,
                "consumo_viveres": flota.consumo_viveres,
                "total_vivieres": flota.total_vivieres,
                "dias_inspeccion": flota.dias_inspeccion,
                "total_servicio_inspeccion": flota.total_servicio_inspeccion,
                "total_derecho_pesca": flota.total_derecho_pesca,
                "total_costo": flota.total_costo,
                "costo_tm_captura": flota.costo_tm_captura,
                "csot": flota.csot,
                "embarcacion": flota.embarcacion.id,
                "zona_pesca": flota.zona_pesca.id,
                # Lista para almacenar los lances relacionados
                "lances": []
            }

            # Obtener los lances asociados a esta flota
            lances = DiarioDePesca.objects.filter(flotaDP_id=flota)

            # Recorrer todos los lances asociados a esta flota
            for lance in lances:
                # Serializar los datos de DiarioDePesca
                lance_data = {
                    "id": lance.id,
                    "embarcacion": lance.embarcacion,
                    "especie": lance.especie,
                    "fecha": lance.fecha,
                    "numero_alcance": lance.numero_alcance,
                    "estrato": lance.estrato,
                    "profundidad": lance.profundidad,
                    "tiempo_efectivo": lance.tiempo_efectivo,
                    "rango_talla_inicial": lance.rango_talla_inicial,
                    "rango_talla_final": lance.rango_talla_final,
                    "moda": lance.moda,
                    "porcentaje": lance.porcentaje,
                    "ar": lance.ar,
                    "numero": lance.numero,
                    "zona_pesca": lance.zona_pesca.id,
                    "flotaDP_id": lance.flotaDP_id.id
                }

                # Agregar el lance a la lista de lances en flota_data
                flota_data["lances"].append(lance_data)

            # Agregar la flota con sus lances al response_data
            response_data.append(flota_data)

        # Retornar la respuesta en formato JSON
        return Response(response_data)

#Derecho de pesca
class DerechoPescaListCreateView(generics.ListCreateAPIView):
    queryset = DerechoPesca.objects.all()
    serializer_class = DerechoPescaSerializer

class DerechoPescaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DerechoPesca.objects.all()
    serializer_class = DerechoPescaSerializer
#ejemplo:
class ConsumoGasolinaListCreateView(generics.ListCreateAPIView):
    queryset = ConsumoGasolina.objects.all()
    serializer_class = ConsumoGasolinaSerializer

class ConsumoGasolinaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsumoGasolina.objects.all()
    serializer_class = ConsumoGasolinaSerializer




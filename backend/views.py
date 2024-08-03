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

class DiarioDePescaPorFlotaView(APIView):
    def get(self, request, flota_id):
        diarios = DiarioDePesca.objects.filter(flotaDP_id=flota_id)
        serializer = DiarioDePescaSerializer(diarios, many=True)
        return Response(serializer.data)

# ListCreateAPIView para CostoTripulacion
class CostoTripulacionListCreateView(generics.ListCreateAPIView):
    queryset = CostoTripulacion.objects.all()
    serializer_class = CostoTripulacionSerializer

# RetrieveUpdateDestroyAPIView para CostoTripulacion
class CostoTripulacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostoTripulacion.objects.all()
    serializer_class = CostoTripulacionSerializer

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




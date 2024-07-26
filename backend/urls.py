from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from backend import views


urlpatterns = [
    path('crear/users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('token/', obtain_tokens, name='token_obtain'),
    path('diarios-de-pesca/', DiarioDePescaListView.as_view(), name='diario_de_pesca_list'),
    path('diarios-de-pesca/<int:pk>/', DiarioDePescaDetailView.as_view(), name='diario_de_pesca_detail'),
    path('diarios-de-pesca/<int:pk>/delete/', DiarioDePescaDeleteView.as_view(), name='diario_de_pesca_delete'),
    path('embarcaciones/', EmbarcacionesListCreateView.as_view(), name='embarcaciones-list-create'),
    path('embarcaciones/<int:pk>/', EmbarcacionesRetrieveUpdateDestroyView.as_view(), name='embarcaciones-crud'),
    path('especies/', EspeciesListCreateView.as_view(), name='especies-list-create'),
    path('especies/<int:pk>/', EspeciesRetrieveUpdateDestroyView.as_view(), name='especies-crud'),
    path('especies/precio/<str:nombre>/', EspeciesPrecioView.as_view(), name='especies-precio'),
    path('zona-pesca/', ZonaPescaListCreateView.as_view(), name='zona-pesca-create'),
    path('tarifa-costo/', TarifaCostoListCreateView.as_view(), name='tarifa-costo-create'),
    path('tarifa-costo/<int:pk>/', TarifaCostoDetailView.as_view(), name='t_c_detail'),
    path('viveres/', ViveresListCreateView.as_view(), name='viveres-embarcacion-create'),
    path('mescanismo/', MecanismoListCreateView.as_view(), name='mescanismo-i-create'),
    path('mescanismo/<int:pk>/', MecanismoRetrieveUpdateDestroyView.as_view(), name='mescanismo-crud'),
    path('costogalonb_05/', CostoGalonB_05_ListCreateView.as_view(), name='costogalonb_05_list_create'),
    path('costogalonb_05/<int:pk>/', CostoGalonB_05_RetrieveUpdateDestroyView.as_view(), name='costogalonb_05_detail'),
    path('costoHielo/', CostoHielo_ListCreateView.as_view(), name='hielo_create'),
    path('costoHielo/<int:pk>/', CostoHielo_RetrieveUpdateDestroyView.as_view(), name='hielo_detail'),
    path('costogalonagua/', CostoGalonAguaListCreateView.as_view(), name='costogalonagua_list_create'),
    path('costogalonagua/<int:pk>/', CostoGalonAguaRetrieveUpdateDestroyView.as_view(), name='costogalonagua_detail'),
    path('costotipocambio/', CostoTipoCambioListCreateView.as_view(), name='costotipocambio_list_create'),
    path('costotipocambio/<int:pk>/', CostoTipoCambioRetrieveUpdateDestroyView.as_view(), name='costotipocambio_detail'),
    path('flotadp/', FlotaDPListCreateView.as_view(), name='flotadp_list_create'),
    path('flotadp/<int:pk>/', FlotaDPRetrieveUpdateDestroyView.as_view(), name='flotadp_detail'),
    path('costotripulacion/', CostoTripulacionListCreateView.as_view(), name='costotripulacion_list_create'),
    path('costotripulacion/<int:pk>/', CostoTripulacionRetrieveUpdateDestroyView.as_view(), name='costotripulacion_detail'),
    path('consumo-gasolina/', ConsumoGasolinaListCreateView.as_view(), name='consumo-gasolina-list-create'),
    path('consumo-gasolina/<int:pk>/', ConsumoGasolinaRetrieveUpdateDestroyView.as_view(), name='consumo-gasolina-retrieve-update-destroy'),
    path('derechopescas/', DerechoPescaListCreateView.as_view(), name='derechopescas_list_create'),
    path('derechopescas/<int:pk>/', DerechoPescaRetrieveUpdateDestroyView.as_view(), name='derechopescas_retrieve_update_destroy'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
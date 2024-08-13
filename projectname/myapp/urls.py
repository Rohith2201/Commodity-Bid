from django.urls import path
from .views import signup, list_commodity, get_commodity_bids, accept_bid, get_user_commodities
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('commodity/list/', list_commodity, name='list_commodity'),
    path('commodity/<int:id>/bids/', get_commodity_bids, name='get_commodity_bids'),
    path('commodity/<int:id>/accept-bid/', accept_bid, name='accept_bid'),
    path('commodity/my-commodities/', get_user_commodities, name='get_user_commodities'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

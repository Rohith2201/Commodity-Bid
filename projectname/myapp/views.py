from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Commodity, Bid
from .serializers import CommoditySerializer, BidSerializer, UserSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def signup(request):
    data = request.data
    user = User.objects.create_user(
        username=data['email'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        password='defaultpassword'  # Consider generating or requiring a password
    )
    user_serializer = UserSerializer(user)
    return Response({
        "status": "success",
        "message": "User created successfully",
        "payload": {"user_id": user_serializer.data['id']}
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_commodity(request):
    data = request.data
    data['owner'] = request.user.id
    serializer = CommoditySerializer(data=data)
    if serializer.is_valid():
        commodity = serializer.save()
        return Response({
            "status": "success",
            "message": "Commodity listed successfully",
            "payload": {
                "commodity_id": commodity.id,
                "quote_price_per_month": commodity.quote_price_per_month,
                "created_at": commodity.created_at
            }
        })
    return Response({"status": "error", "message": "Commodity could not be listed", "payload": {}}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_commodity_bids(request, id):
    bids = Bid.objects.filter(commodity_id=id)
    if not bids.exists():
        return Response({"status": "error", "message": "No bids found", "payload": []})
    serializer = BidSerializer(bids, many=True)
    return Response({"status": "success", "message": "Bids for commodity fetched successfully", "payload": serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_bid(request, id):
    data = request.data
    try:
        bid = Bid.objects.get(id=data['bid_id'], commodity_id=id)
        commodity = bid.commodity
        commodity.status = "rented"
        commodity.save()
        return Response({"status": "success", "message": "Bid has been accepted successfully", "payload": {}})
    except Bid.DoesNotExist:
        return Response({"status": "error", "message": "Bid not found", "payload": {}}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_commodities(request):
    commodities = Commodity.objects.filter(owner=request.user)
    serializer = CommoditySerializer(commodities, many=True)
    return Response({"status": "success", "message": "Commodities fetched successfully", "payload": serializer.data})

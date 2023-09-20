from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Transfer, UserAccount
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from django.db import transaction

permission_classes= [IsAuthenticated]

def post(self, request, *args, **kwargs):
    request_data= request.data
    amount= Decimal(request_data.get('amount'))
    receiving_user_id= request_data.get('receiving_user_id')
    with transaction.atomic():##with this transaction block, changes will be committed only when 
     #whole transaction has been completed, this guarantees the atomicity
     initiator_account= UserAccount.objects.select_for_upadate(nowait=True).filter(user=request.user).first()
    #Here nowait=True means that it will not wait and give an immediate error..
     if initiator_account.balance < amount:
        return Response({
            "status":"error",
            "message":"You do not have enough funds",
            "payload":""
        }, status= status.HTTP_400_BAD_REQUEST)

     transfer= Transfer.objects.create(
        initiated_by=request.user,
        transfer_to=receiving_user_id,
        amount= amount
     )    
    
     initiator_account.balance = initiator_account.balance- amount
     receiving_user_account= UserAccount.objects.filter(user_id=receiving_user_id).first()
     receiving_user_account.balance= receiving_user_account.balance+ amount
     initiator_account.save()
     receiving_user_account.save()
     return Response({
        "status":"successs",
        "message": "Successfully transferred",
        "payload": "",

     }, status= status.HTTP_200_OK)

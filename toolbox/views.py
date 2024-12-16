# python imports
from datetime import datetime

# django imports
from django.shortcuts import render
from django.db.models import Sum, F

# third party imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# project imports
from .models import Numbers

@api_view(['GET'])
def difference(request):
    # Get input and return errors early
    n = request.query_params.get('number', None)
    if n is None:
        return Response({"error": "input 'number' not found"}, status=status.HTTP_400_BAD_REQUEST)
    # check to see if the number exists
    try:
        numbers = Numbers.objects.filter(number__lte=n)
    except Numbers.DoesNotExist:
        return Response({"error": "number not found"}, status=status.HTTP_404_NOT_FOUND)

    sum_of_squares = numbers.aggregate(sum_of_squares=Sum(F('number') ** 2))['sum_of_squares']
    square_of_sum = numbers.aggregate(square_of_sum=Sum('number'))['square_of_sum'] ** 2

    data = {
            "datetime": datetime.now(),
            "value": abs(square_of_sum - sum_of_squares),
            "number": n,
            "occurences": numbers.last().request_ct,
            "last_datetime": numbers.last().request_last_timestamp  # since n is based on the last object / up to the last object
        }
    
    # is this worth putting in a post save signal? -thn 15:15
    # no because post signal would trigger with admin saves, not just on requests -thn 15:18
    numbers.last().request_last_timestamp = datetime.now()
    numbers.last().request_ct += 1

    return Response(data, status=status.HTTP_200_OK)
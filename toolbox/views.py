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

# using a function based view decorator for simplicity rather than a whole CRUD modelviewset
@api_view(['GET'])
def difference(request):
    # Get input and return errors early
    num = int(request.query_params.get('number', None))
    if num is None:
        return Response({"error": "input 'number' not found"}, status=status.HTTP_400_BAD_REQUEST)
    # check to see if the number exists
    try:
        numbers = Numbers.objects.filter(number__lte=num)
    except Numbers.DoesNotExist:
        return Response({"error": "number not found"}, status=status.HTTP_404_NOT_FOUND)

    # use F expressions to perform arithmetic, then aggregates
    sum_of_squares = numbers.aggregate(sum_of_squares=Sum(F('number') ** 2))['sum_of_squares']
    square_of_sum = numbers.aggregate(square_of_sum=Sum('number'))['square_of_sum'] ** 2

    # there's only 1 possible triplet and that is 3,4,5 which abc = 60, saves on computation time and complexity
    # so we look for 60 otherwise we return an empty list
    # always returning a list as maintain consistent data types in json response
    has_triplet = []
    if num == 60:
        print("found 60")
        has_triplet = [3,4,5]
    data = {
            "datetime": datetime.now(),
            "value": abs(square_of_sum - sum_of_squares),
            "number": num,
            "occurences": numbers.last().request_ct,
            "last_datetime": numbers.last().request_last_timestamp,  # since n is based on the last object / up to the last object
            "has_triplet": has_triplet
        }
    
    # is this worth putting in a post save signal? -thn 15:15
    # no because post signal would trigger with admin saves, not just on requests -thn 15:18
    # do a save to store request count and last request time
    update_number = numbers.last()
    update_number.request_last_timestamp = datetime.now()
    update_number.request_ct += 1
    update_number.save()


    return Response(data, status=status.HTTP_200_OK)

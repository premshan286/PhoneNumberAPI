from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import os
from PhoneSearchApi.models import PhoneNumber
from PhoneSearchApi.serializer import PhoneNumberSerializer

def index(request):
    responseList = ['<p>Phone Search index</p>']
    responseList.append('<p>Search using one of the following api calls</p>')
    responseList.append('<p><a href=/search-by-country-code-api?countrycode=1>search by Country Code</a></p>')
    responseList.append('<p><a href=/search-by-region-code-api?regioncode=1>search by Region Code</a></p>')
    responseList.append('<p><a href=/search-by-localexchange-code-api?localexchangecode=1>search by Local Exchange Code</a></p>')
    responseList.append('<p><a href=/search-by-number-api?number=1>search by Number Code</a></p>')
    responseList.append('<p><a href=/search-api?countrycode=1&regioncode=1&localexchangecode=1&number=1>search by Number Code</a></p>')

    return HttpResponse(''.join(responseList))

def search_by_countryCode_api(request):
    """
    List all phone numbers matching the country code in the query string.
    """
    if request.method == 'GET':
        countrycode = request.GET.get('countrycode')
        if ((countrycode is not None) and len(countrycode) > 0):
            _phoneNumbers = PhoneNumber.getPhoneNumbersByCountryCode(countrycode)
            if (len(_phoneNumbers) > 0):
                serializer = PhoneNumberSerializer(_phoneNumbers, many=True)
                return JsonResponse(serializer.data, safe=False)
        return JsonResponse('No phone number found that matches the criteria', safe=False)
           
        
def search_by_regionCode_api(request):
    """
    List all phone numbers matching the region code in the query string.
    """
    if request.method == 'GET':
        regioncode = request.GET.get('regioncode')
        if ((regioncode is not None) and len(regioncode) > 0):
            _phoneNumbers = PhoneNumber.getPhoneNumbersByRegionCode(regioncode)
            if (len(_phoneNumbers) > 0):
                serializer = PhoneNumberSerializer(_phoneNumbers, many=True)
                return JsonResponse(serializer.data, safe=False)
        return JsonResponse('No phone number found that matches the criteria', safe=False)
        
def search_by_localExchangeCode_api(request):
    """
    List all phone numbers matching the local exchange code in the query string.
    """
    if request.method == 'GET':
        localExchangecode = request.GET.get('localexchangecode')
        if ((localExchangecode is not None) and len(localExchangecode) > 0):
            _phoneNumbers = PhoneNumber.getPhoneNumbersByLocalExchangeCode(localExchangecode)
            if (len(_phoneNumbers) > 0):
                serializer = PhoneNumberSerializer(_phoneNumbers, many=True)
                return JsonResponse(serializer.data, safe=False)
        return JsonResponse('No phone number found that matches the criteria', safe=False)
        
def search_by_number_api(request):
    """
    List all phone numbers matching the number in the query string.
    """
    if request.method == 'GET':
        number = request.GET.get('number')
        if ((number is not None) and len(number) > 0):
            _phoneNumbers = PhoneNumber.getPhoneNumbersByNumber(number)
            if (len(_phoneNumbers) > 0):
                serializer = PhoneNumberSerializer(_phoneNumbers, many=True)
                return JsonResponse(serializer.data, safe=False)
        return JsonResponse('No phone number found that matches the criteria', safe=False)

def search_api(request):
    """
    List all phone numbers matching the combination of country code, region code, local exchange code and number in the query string.
    """
    if request.method == 'GET':
        countrycode = request.GET.get('countrycode')
        regioncode = request.GET.get('regioncode')
        localExchangecode = request.GET.get('localexchangecode')
        number = request.GET.get('number')
        
        if ((countrycode is None) or len(countrycode) == 0):
            countrycode = ''
        if ((regioncode is None) or len(regioncode) == 0):
            regioncode = ''
        if ((localExchangecode is None) or len(localExchangecode) == 0):
            localExchangecode = ''
        if ((number is None) or len(number) == 0):
            number = ''
        
        _phoneNumbers = PhoneNumber.getPhoneNumbersFiltered(countrycode, regioncode, localExchangecode, number)
        if (len(_phoneNumbers) > 0):
                serializer = PhoneNumberSerializer(_phoneNumbers, many=True)
                return JsonResponse(serializer.data, safe=False)
        return JsonResponse('No phone number found that matches the criteria', safe=False)
    
 




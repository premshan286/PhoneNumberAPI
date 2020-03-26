from django.db import models
import  re   # regular expression to parse the phone number string
import os   

#variables to hold the cached data (Contents parsed from the txt file)
PhoneNumber_list = []

# Create your models here.
class PhoneNumber(models.Model):
    countryCode = models.TextField(default='1')
    regionCode = models.TextField()
    localExchangeCode = models.TextField()
    number = models.TextField()
    extension = models.TextField()
    
    def __str__(self):
        return "{}-({}){}-{} x{}".format(self.countryCode, self.regionCode, self.localExchangeCode, self.number, self.extension)
    
    
    def __init__(self, countryCode, regionCode, localExchangeCode, number, extension):
        if (len(countryCode) == 0):
            self.countryCode = '1'
        else: 
            self.countryCode = countryCode
        self.regionCode = regionCode 
        self.localExchangeCode = localExchangeCode 
        self.number = number 
        self.extension = extension 

    #Initialize and cache the Phone number data with the contents of the txt file   
    def importDataFromTxtFile():
        phonePattern = re.compile(r'''
            \D*         # optional separator is any number of non-digits
            (\d*)       # international code is optional and can be any number of digits
            \D*         # optional separator is any number of non-digits
            (\d{3})     # area code is 3 digits (e.g. '800')
            \D*         # optional separator is any number of non-digits
            (\d{3})     # local exchange code is 3 digits 
            \D*         # optional separator
            (\d{4})     # rest of number is 4 digits 
            \D*         # optional separator
            (\d*)       # extension is optional and can be any number of digits
            (.*)        # ignore any characters after the first extension
            $           # end of string
            ''', re.VERBOSE)
        
        dataFile = os.path.join( os.getcwd(),'code_challenge_data_1.txt' )
        with open(dataFile, 'r') as f:
            phoneList = f.readlines()
            
        for aPhone in phoneList:
            print (aPhone)
            phoneParse = phonePattern.search(aPhone)
            if (phoneParse != None):
                PhoneNumber_list.append(PhoneNumber(phonePattern.search(aPhone).groups()[0], 
                                                    phonePattern.search(aPhone).groups()[1], 
                                                    phonePattern.search(aPhone).groups()[2], 
                                                    phonePattern.search(aPhone).groups()[3], 
                                                    phonePattern.search(aPhone).groups()[4]))
                                                    

                     #Return the list of flights that match the criteria based on Origin and Destination   
    def getPhoneNumbersByCountryCode(countryCodeParam):
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (countryCodeParam == x.countryCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers

    
    def getPhoneNumbersByRegionCode(regionCodeParam):
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (regionCodeParam == x.regionCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
        
    def getPhoneNumbersByLocalExchangeCode(localExchangeCodeParam):
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (localExchangeCodeParam == x.localExchangeCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
    def getPhoneNumbersByNumber(numberParam):
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (numberParam == x.number), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
    def getPhoneNumbersFiltered(countryCodeParam, regionCodeParam, localExchangeCodeParam, numberParam):
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: ((numberParam in x.number) and (localExchangeCodeParam in x.localExchangeCode) and (regionCodeParam in x.regionCode) and (countryCodeParam in x.countryCode)), PhoneNumber_list))
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
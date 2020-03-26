from django.db import models
import  re   # regular expression to parse the phone number string
import os   

#variables to hold the cached data (Contents parsed from the txt file)
PhoneNumber_list = []

# Create your models here.
class PhoneNumber(models.Model):
    """
    A class used to represent a Phone Number object and have search methods to be exposed thru' REST API
    
    Attributes
    ----------
    countryCode : str
        country code for the phone number
    regionCode : str
        region code for the phone number
    localExchangeCode : str
        localExchange code for the phone number
    number : str
        last 4 digits number for the phone number
    extension: str
        extension for the phone number

    Example:
        1 334 213 5543 ext 323
        Country code = 1
        Region code = 334
        Local Exchange code = 213
        Number (last 4 digits) = 5543
        Extension = 323
        
    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    
    
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
        
        """import the data file and populate the internal phone number collection object.

        Use Regular Expression to parse the strings from the file and instantiate the individual Phone Number objects. 
        Add each individual instance to the collection object as part of the initialization process
        
        """
        
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
                                                    

    #Return the list of phone numbers that match the criteria based on country code parameter   
    def getPhoneNumbersByCountryCode(countryCodeParam):
        
        """API call to search the phone numbers by Country code.

        Parameters
        ----------
        countryCodeParam : str
            The country code that need be searched on

        """
        
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (countryCodeParam == x.countryCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers

    
    #Return the list of phone numbers that match the criteria based on region code parameter   
    def getPhoneNumbersByRegionCode(regionCodeParam):
        
        """API call to search the phone numbers by Region code.

        Parameters
        ----------
        regionCodeParam : str
            The region code that need be searched on

        """
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (regionCodeParam == x.regionCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
        
    #Return the list of phone numbers that match the criteria based on local exchange code parameter   
    def getPhoneNumbersByLocalExchangeCode(localExchangeCodeParam):
        
        """API call to search the phone numbers by local exchange code.

        Parameters
        ----------
        localExchangeCodeParam : str
            The local exchange code that need be searched on

        """
            
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (localExchangeCodeParam == x.localExchangeCode), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
    #Return the list of phone numbers that match the criteria based on number (last 4 digits)  parameter   
    def getPhoneNumbersByNumber(numberParam):
        
        """API call to search the phone numbers by number (last 4 digits)

        Parameters
        ----------
        numberParam : str
            The number that need be searched on

        """            
            
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: (numberParam == x.number), PhoneNumber_list))
        for aPhone in filteredPhoneNumbers:
            print (aPhone)
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
    
    #Return the list of phone numbers that match the criteria based on country code, region code, local exchange and number parameters  
    def getPhoneNumbersFiltered(countryCodeParam, regionCodeParam, localExchangeCodeParam, numberParam):
        
        """API call to search the phone numbers using the different attributes.

        Parameters
        ----------
        
        countryCodeParam : str
            The country code that need be searched on

        regionCodeParam : str
            The region code that need be searched on

        localExchangeCodeParam : str
            The local exchange code that need be searched on

        numberParam : str
            The number that need be searched on
        """
            
        filteredPhoneNumbers = []
        if (len(PhoneNumber_list) == 0):
            PhoneNumber.importDataFromTxtFile()	
        filteredPhoneNumbers = list(filter(lambda x: ((numberParam in x.number) and (localExchangeCodeParam in x.localExchangeCode) and (regionCodeParam in x.regionCode) and (countryCodeParam in x.countryCode)), PhoneNumber_list))
        print ('returning Phone Number count: ' + str(len(filteredPhoneNumbers)))
        return filteredPhoneNumbers
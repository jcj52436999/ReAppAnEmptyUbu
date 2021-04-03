#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# mthdGenStrVariables.py as part of reAppAnEmptyUbu.py
# Created originally in 2018 as a simplistic exercise in broad-spectrum py use
# @author Joe Jackson 



def genStrVariables():   # stringPiecesDict
    #'''
    #aSpace = str(32)      # String.fromCharCode(32);    
    #aDblQuote = str(34)   # String.fromCharCode(34); 
    #aSnglQuote = str(39)   # String.fromCharCode(39);  
    #aComma = str(44)      # String.fromCharCode(44); 
    #aColon = str(58)      # String.fromCharCode(58); 
    #aSemiColon = str(59)      # String.fromCharCode(59); 
    #aForeSlash = str(47)      # String.fromCharCode(47); 
    #aBackSlash = str(92)      # String.fromCharCode(92);  
    #aLF = str(10)      # String.fromCharCode(10); 
    #aCR = str(13)      # String.fromCharCode(13); 
    #aLfCr = aLF + aCR 
    #aCrLf = aCR + aLF 
    #aColonSpaceDblQuote = aColon + aSpace + aDblQuote
    #example = "example" 
    #'''
    #'''
    screenWidthAvail = self.width()
    screenHeightAvail = self.height()
    
    # in JS
    #var screenWidthAvail = screen.availWidth ;  
    #var screenHeightAvail = screen.availHeight ; 
    #'''  
    stringPiecesDict = ({"aSpace": str(32), "aDblQuote": str(34)},
            {"aSnglQuote": str(39), "aComma": str(44)},
            {"aColon": str(58), "aSemiColon": str(59)},
            {"aForeSlash": str(47), "aBackSlash": str(92)},
            {"aLF": str(10), "aCR": str(13)},
            {"aLfCr": str(10) + str(13), "aCrLf": str(13) + str(10)},
            {"aColonSpaceDblQuote": str(58) + str(32) + str(34)}
            )
    return stringPiecesDict






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:13:33 2019

@author: rzd
"""

from getdata import request
from train_data import interprete
interpreter=interprete()
entity={}
datas=request()
map_condition={"maximum":"highPic",
              "minimum":"lowPic",
              "different percentage":"diffPer",
              "open price":"openPri",
              "yesterday price":"yesPic",
              "change amount":"diffAmo",
              "exchange rate":"buyPic"
              }
def get_entity_and_intent(message): #get entity and intent 
    entities={}
    entity_and_intent=interpreter.parse(message)
    intent=entity_and_intent["intent"]["name"]
    entity=entity_and_intent["entities"]
    for ent in entity:
         entities[ent["value"]] = str(ent["entity"])
    return entities,intent
def get_request_data(message,currency_information={},condition=None):
    result=None
    entity,intent=get_entity_and_intent(message)
    if datas!=None: #if get JSON data successfully,search for currency's information ,else return the failure of data request
        if entity:#if there are currency's kind or conditon return the requested information ,else return nothing                   
            for key,value in entity.items():
                   if value=="currency":
                        code="USD{}".format(key.upper())
                        for data in datas:
                            for datanum,currencyInformation in data.items():
                                if currencyInformation["code"]==code:
                                    currency_information=currencyInformation
            for key,value in entity.items():
                    if value=="condition":
                        condition=map_condition[key]
            if currency_information and condition!=None:
                result=currency_information[condition]    
            return result,currency_information,condition                                           
        else:
            return result,currency_information,condition                
    else:
        return "Data request fail",currency_information,condition    
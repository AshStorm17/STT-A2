#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I 

def uspses(headers,content):
	detect = False
	detect |= headers['server'] == 'Secure Entry Server'.lower()
	if detect : 
		return "USP Secure Entry Server (United Security Providers)"

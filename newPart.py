import json
import os
import math
import pprint
from owlready2 import *
from partPicker import get_label, get_subclasses_recur, get_subclasses_onelevel, get_obo_elem, get_indivs

onto = get_ontology("Bart2.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")


def find_part(computer, missingClass):
	# computer is an individual of class Computer
	# missingClass is the class ID of the missing component
	# for each type: determine compatibility and utility
	# sync_reasoner()
	options = get_indivs(str(missingClass).split(".")[-1])
	if missingClass == obo.CPU:
		print("CPU missing")
		# CPU socket against mobo
		# get MOBO CPU socket
		for component in computer.hasPart:
			if component in list(onto.search(is_a=obo.Motherboard)):
				# print(component.is_a[0].is_a)
				indices = [i for i, s in enumerate(component.is_a[0].is_a) if 'CPUSocket' in str(s)]
				cpuMobo = str(component.is_a[0].is_a[indices[0]]).split("&")[1].strip().split(" ")[-1]
		# check options (currently ignoring intel because no cpu socket yet)
		# return best from replacements
		# for now cheapest
		cheapest = None
		minPrice = 99999
		for o in options[3:]: # REMOVE SLICING AFTER ADDING HASCPUSOCKET TO INTEL
			indices = [i for i, s in enumerate(o.is_a[0].is_a) if 'CPUSocket' in str(s)]
			CPUsocket = str(o.is_a[0].is_a[indices[0]]).split("&")[1].split(" ")[2]
			if cpuMobo != CPUsocket:
				continue
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest
	elif missingClass == obo.GPU:
		print("GPU missing")
		cheapest = None
		minPrice = 99999
		for o in options:
			# return best from replacements
			# for now cheapest
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest
		# MAXram? Or no checks?
	elif missingClass == obo.Memory:
		print("RAM missing")
		# get MOBO MaxRAM
		for component in computer.hasPart:
			if component in list(onto.search(is_a=obo.Motherboard)):
				indices = [i for i, s in enumerate(component.is_a[0].is_a) if 'MaxRAM' in str(s)]
				maxRAM = str(component.is_a[0].is_a[indices[0]]).split("&")[2].split(" ")[2].split(".")[1][:-1]
		# return best from replacements
		# for now cheapest
		memorySizes = ["VeryLowMemory", "LowMemory", "MediumMemory", "HighMemory", "UltraHighMemory"]
		cheapest = None
		minPrice = 99999
		for o in options: # CHECK CORRECT DDR VERSION?
			# print(o.is_a[0].is_a)
			indices = [i for i, s in enumerate(o.is_a[0].is_a) if 'Memory' in str(s)]
			ramSize = str(o.is_a[0].is_a[indices[0]]).split("&")[-1].split(".")[-1]
			# print(ramSize)
			if (ramSize not in memorySizes) or memorySizes.index(ramSize) > memorySizes.index(maxRAM):
				continue
			if len(o.item_price)==0:
				print("No item price known")
				continue
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest
	elif missingClass == obo.Motherboard:
		print("Mobo missing")
		# CPU socket and MAXram
		ramSize = None
		CPUsocket = None
		for component in computer.hasPart:
			if component in list(onto.search(is_a=obo.Memory)):
				indices = [i for i, s in enumerate(component.is_a[0].is_a) if 'Memory' in str(s)]
				ramSize = str(component.is_a[0].is_a[indices[0]]).split("&")[-1].split(".")[-1]
			elif component in list(onto.search(is_a=obo.CPU)) and not component in list(onto.search(is_a=obo.INTEL)): #REMOVE SECOND PART WHEN INTEL HAS CPU SOCKET
				indices = [i for i, s in enumerate(component.is_a[0].is_a) if 'CPUSocket' in str(s)]
				CPUsocket = str(component.is_a[0].is_a[indices[0]]).split("&")[1].split(" ")[2]
		if ramSize == None or CPUsocket==None:
			print("Cannot select motherboard without knowing RAM and CPU")
			return None
		# check against possible motherboards
		memorySizes = ["VeryLowMemory", "LowMemory", "MediumMemory", "HighMemory", "UltraHighMemory"]
		cheapest = None
		minPrice = 99999
		for o in options:
			indices = [i for i, s in enumerate(o.is_a[0].is_a) if 'CPUSocket' in str(s)]
			cpuMobo = str(o.is_a[0].is_a[indices[0]]).split("&")[1].split(" ")[2]
			indices = [i for i, s in enumerate(o.is_a[0].is_a) if 'MaxRAM' in str(s)]
			maxRAM = str(o.is_a[0].is_a[indices[0]]).split("&")[2].split(" ")[2].split(".")[1][:-1]
			if (ramSize not in memorySizes) or memorySizes.index(ramSize) > memorySizes.index(maxRAM) or CPUsocket != cpuMobo:
				continue
			if len(o.item_price)==0:
				print("No item price known")
				continue
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest
	elif missingClass == obo.PSU:
		print("PSU missing")
		cheapest = None
		minPrice = 99999
		for o in options:
			# return best from replacements
			# for now cheapest
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest
		# Wattage? Or no checks?
	else:
		cheapest = None
		minPrice = 99999
		for o in options:
			# return best from replacements
			# for now cheapest
			if len(o.item_price)==0:
				print("No item price known")
				continue
			if o.item_price[0] < minPrice:
				cheapest = o
				minPrice = o.item_price[0]
		return cheapest

obo_parts = []
parts = ['Corsair_200R_1', "'AMD_-_Ryzen_5_2600'_1", 'EVGA_04G-P4-6251-KR_1', 'B450_TOMAHAWK_1', 'Corsair_-_CXM_550_W_80_1', 'Kingston_A400120GB_1', 'CMZ8GX3M1A1600C10_1']
for x in parts:
	obo_part = onto.search(iri = "*" + x)
	if len(obo_part) > 0:
		obo_parts.append(obo_part[0])
new_computer = obo.Computer("Obo_comp_1", namespace = onto, hasPart = obo_parts)

sync_reasoner()
newpart = find_part(new_computer, obo.CPU)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.PSU)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.GPU)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.Memory)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.Case)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.Storage)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.Motherboard)
print(newpart, newpart.item_price)
newpart = find_part(new_computer, obo.Cooling)
print(newpart, newpart.item_price)
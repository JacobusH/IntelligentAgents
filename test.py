import json
import os
import math
import pprint
from owlready2 import *
from partPicker import get_label, get_subclasses_recur, get_subclasses_onelevel

# onto = get_ontology("onto2.owl").load()
onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
# obo = get_namespace("http://webprotege.stanford.edu/")
obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
# print(list(onto.classes()))

### working list all classes
# for x in list(onto.classes()):
# 	x = str(x)
# 	class_name = ""
# 	if 'webprotege' in x:
# 		_id = x.split('.')[3]
# 		class_name = obo[_id].label[0]
# 	else: # ont1
# 		_id = x.split('.')[1]
# 		class_name = _id
# print(class_name)

### working get wildcard label
# search_label = onto.search(label = "Keyboard")
# print(search_label[0])

### working get subclasses
# search_subclasses = onto.search(subclass_of = obo['RDpBs6DXJfwjWljvKnjFFK7']) # bleh finally got this POS to work
# for x in search_subclasses:
# 	parent = str(x.is_a[0])
# 	if 'RDpBs6DXJfwjWljvKnjFFK7' in parent: 
# 		print('X: %s' , x)
# 		print('ISA: %s' , x.is_a[0])


### working save individuals
# new_gpu1 = obo.Corsair_200R("indiv_case_1")
# new_gpu2 = obo.Corsair_200R("indiv_case_2")
# new_gpu3 = obo.Corsair_200R("indiv_case_3")
# onto.save("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl")

### working get individuals
# for i in obo.Corsair_200R.instances(): # has direct indivs
# 	print(i)
# for i in obo.Case.instances(): # only has bottom level indivs
# 	print(i)


# test = get_subclasses_onelevel('Motherboard')
test1 = get_subclasses_onelevel('MotherboardBrands')
test2 = get_subclasses_onelevel('MSI')


tmp = 'tmp'


# ['MotherboardBrands', 'MSI', 'MSI_GTX_1050_Ti_GAMING_X_4G', 'MSI_RX_580_ARMOR_8G_OC']

# xpUFBIdmzwyCPpbfIg4hh.MotherboardBrands
# xpUFBIdmzwyCPpbfIg4hh.CPU
# xpUFBIdmzwyCPpbfIg4hh.Case
# xpUFBIdmzwyCPpbfIg4hh.Cooling
# xpUFBIdmzwyCPpbfIg4hh.GPU
# xpUFBIdmzwyCPpbfIg4hh.Memory
# xpUFBIdmzwyCPpbfIg4hh.Motherboard
# xpUFBIdmzwyCPpbfIg4hh.PSU
# xpUFBIdmzwyCPpbfIg4hh.Storage
# xpUFBIdmzwyCPpbfIg4hh.DDR2
# xpUFBIdmzwyCPpbfIg4hh.DDR3
# xpUFBIdmzwyCPpbfIg4hh.DDR4
# xpUFBIdmzwyCPpbfIg4hh.EVGA_02G-P4-6150-KR
# xpUFBIdmzwyCPpbfIg4hh.EVGA_04G-P4-6251-KR
# xpUFBIdmzwyCPpbfIg4hh.Gigabyte_GV-N1050OC-2GD

### recursive indentation...
# # default with a level of 0, and an indent of 4 characters
# 	def write(p, depth=0, indent=4):
# 		if p==None:
# 			return
# 		# here we multiply the level by the number of indents
# 		# and then you multiply that number with a space character
# 		# which will magically show as that number of spaces.
# 		print("{}{}".format(" "*(indent*depth), p.value))
# 		if p.down!=None:
# 			# then you do not need your print(…, end='') hack
# 			# simply increase the depth
# 			write(p.down, depth=depth+1, indent=indent)
# 		# and for siblings, do not increase the depth
# 		write(p.right, depth=depth, indent=indent)
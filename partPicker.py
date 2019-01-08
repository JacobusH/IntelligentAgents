import json
import os
import math
import pprint
from owlready2 import *

# def get_classes():
# 	onto = get_ontology("ont1.owl").load()
# 	obo = get_namespace("http://webprotege.stanford.edu/")
# 	# print(list(onto.classes()))
# 	return obo.R0GjvQkVctYs9B2XQILYoO.label




onto = get_ontology("onto2.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/")
# print(list(onto.classes()))

for x in list(onto.classes()):
	x = str(x)
	class_name = ""
	if 'webprotege' in x:
		_id = x.split('.')[3]
		class_name = obo[_id].label[0]
	else: # ont1
		_id = x.split('.')[1]
		class_name = _id

	# print(class_name)

print("subclass of")
onto.search(is_a = onto.WirelessKeyboard)
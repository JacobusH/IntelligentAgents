import json
import os
import math
import pprint
from owlready2 import *

is_debug = True

def get_label(x):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\JamesOnt2.owl").load()
	else:
		onto = get_ontology("JamesOnt2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/")
	is_str = isinstance(x, str)

	if x.name != None:
		if hasattr(x, '_label'):
			return x._label[0]
		elif hasattr(x, '_name'):
			return x._name
	elif is_str:
		if 'webprotege' in x:
			x = str(x)
			_id = x.split('.')[3]
			return obo[_id].label[0]
		else: 
			return x.split('.')[1]

def get_classes():
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\JamesOnt2.owl").load()
	else:
		onto = get_ontology("JamesOnt2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/") # for web version only

	classes = []
	for x in list(onto.classes()):
		x = str(x)
		class_name = ""
		if 'webprotege' in x:
			class_name = get_label(x)
		### web version only
		# else: # ont1
		# 	_id = x.split('.')[1]
		# 	class_name = _id
		else: 
			class_name = x.split('.')[1]

		classes.append(class_name)
	return classes

def get_subclasses(class_id):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\JamesOnt2.owl").load()
	else:
		onto = get_ontology("JamesOnt2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/") # web version only

	subclasses = []
	search_subclasses = onto.search(subclass_of = obo[class_id]) # bleh finally got this POS to work
	for x in search_subclasses:
		subclasses.append(get_label(x))
	return subclasses





	








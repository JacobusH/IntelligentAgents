import json
import os
import math
import pprint
from owlready2 import *

def get_label(x):
	onto = get_ontology("onto2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/")

	x = str(x)
	_id = x.split('.')[3]
	return obo[_id].label[0]

def get_classes():
	onto = get_ontology("onto2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/")

	classes = []
	for x in list(onto.classes()):
		x = str(x)
		class_name = ""
		if 'webprotege' in x:
			class_name = get_label(x)
		else: # ont1
			_id = x.split('.')[1]
			class_name = _id

		classes.append(class_name)
	return classes

def get_subclasses(class_id):
	onto = get_ontology("onto2.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/")

	subclasses = []
	search_subclasses = onto.search(subclass_of = obo[class_id]) # bleh finally got this POS to work
	for x in list(search_subclasses):
		subclasses.append(get_label(x))
	return subclasses





	








import json
import os
import math
import pprint
from owlready2 import *

is_debug = True

def get_label(x):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	# obo = get_namespace("http://webprotege.stanford.edu/")
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
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
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	# obo = get_namespace("http://webprotege.stanford.edu/")
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")

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

def get_subclasses_recur(class_id, is_IRIS = False):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	# obo = get_namespace("http://webprotege.stanford.edu/")
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")

	search_subclasses = None
	if is_IRIS:
		search_subclasses = onto.search(subclass_of = IRIS[class_id]) # bleh finally got this POS to work
	else:
		search_subclasses = onto.search(subclass_of = obo[class_id])

	subclasses = []
	for x in search_subclasses:
		print(x)
		subclasses.append(get_label(x))
	return subclasses

def get_subclasses_onelevel(class_id):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")

	subclasses = []
	search_subclasses = onto.search(subclass_of = obo[class_id]) 
	for x in search_subclasses:
		# search thru all parents
		for parent in x.is_a:
			cur_parent = str(parent)
			if class_id in cur_parent: 
				subclasses.append(get_label(x))
	return subclasses

def get_indivs(class_id):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")

	indivs = []
	for i in obo[class_id].instances(): # only has bottom level indivs
		print("indiv: %s", i)
		indivs.append(i)
	return(indivs)

def get_obo_elem(elem_id):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James16.owl").load()
	else:
		onto = get_ontology("James16.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	return obo[elem_id]




	








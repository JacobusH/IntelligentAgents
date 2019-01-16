import json
import os
import math
import pprint
from owlready2 import *

is_debug = True


def get_label(x):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# sync_reasoner()
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
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	sync_reasoner()

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
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# sync_reasoner()

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
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# sync_reasoner()

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
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# sync_reasoner()

	indivs = []
	for i in obo[class_id].instances(): # only has bottom level indivs
		print("indiv: %s", i)
		indivs.append(i)
	return(indivs)

def get_obo_elem(elem_id):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# sync_reasoner()
	return obo[elem_id]

def save_computer(comp_name, parts):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	# make the computer
	obo_parts = []
	for x in parts:
		obo_part = onto.search(iri = "*" + x)
		if len(obo_part) > 0:
			obo_parts.append(obo_part[0])
	new_computer = obo.Computer(comp_name, namespace = onto, hasPart = obo_parts)
	onto.save("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl")

def recur_find_parent(cur_parent, possib_parents):
	if cur_parent is None or cur_parent == []:
		return None
	else:
		for new_parent in cur_parent.is_a: # is one of our direct parents a match?
			new_parent_name = new_parent.name
			for par in possib_parents:
				if par == new_parent_name: # we have a match
					return par
				elif par == 'Motherboard' and par in new_parent_name: # mobo is a bit special
					return par
		return recur_find_parent(new_parent, possib_parents) # keep going

def find_missing_parts(comp_name):
	onto = None
	if is_debug:
		onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\Shared1.owl").load()
	else:
		onto = get_ontology("Shared1.owl").load()
	obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
	all_parts = get_subclasses_onelevel('RDpBs6DXJfwjWljvKnjFFK7')
	comp_parts = onto.search(iri = "*" + comp_name)[0].hasPart
	comp_has = []
	for part in comp_parts:
		comp_has.append(recur_find_parent(part, all_parts))
	# now get the diff 
	comp_needs = list(set(all_parts) - set(comp_has))
	return comp_needs




	








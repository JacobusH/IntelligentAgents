import json
import os
import math
import pprint
from owlready2 import *
from partPicker import get_label

onto = get_ontology("onto2.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/")
# print(list(onto.classes()))

### working list all classes
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

### working get wildcard label
# search_label = onto.search(label = "Keyboard")
# print(search_label[0])



### working search sublcasses of
search_subclasses = onto.search(subclass_of = obo["R6KTEriqId00kTIZki5blq"]) # bleh finally got this POS to work
for x in list(search_subclasses):
  print(get_label(x))



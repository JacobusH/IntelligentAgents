import json
import os
import math
import pprint
from owlready2 import *
from partPicker import get_label, get_subclasses

# onto = get_ontology("onto2.owl").load()
onto = get_ontology("JamesOnt4.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/")
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



### working search sublcasses of, webversion
# search_subclasses = onto.search(subclass_of = obo["R6KTEriqId00kTIZki5blq"]) # bleh finally got this POS to work
# for x in list(search_subclasses):
#   print(get_label(x))

# ### subclasses, desktop version
# search_subclasses = onto.search(subclass_of = obo["R6KTEriqId00kTIZki5blq"]) # bleh finally got this POS to work
# for x in list(search_subclasses):
#   onto = get_ontology("./JamesOnt4.owl").load()
# 	obo = get_namespace("http://webprotege.stanford.edu/")
# 	x = str(x)
# 	_id = x.split('.')[3]
# 	return obo[_id].label[0]

# for x in get_subclasses("RDpBs6DXJfwjWljvKnjFFK7"):
# 	print(x)

# print(get_subclasses("RDpBs6DXJfwjWljvKnjFFK7"))

search_subclasses = onto.search(subclass_of = obo['RDpBs6DXJfwjWljvKnjFFK7']) # bleh finally got this POS to work
for x in search_subclasses:
	print(x)

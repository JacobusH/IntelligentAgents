import json
import os
import math
import pprint
# from owlready2 import onto_path
from owlready2 import *


##########
# Main
##########
onto = get_ontology("onto_1.owl").load()
obo = get_namespace("http://webprotege.stanford.edu/")
print(list(onto.classes()))
print(obo.R0GjvQkVctYs9B2XQILYoO.label)
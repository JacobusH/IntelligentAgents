from owlready2 import *

class MyShared:
  global onto
  global obo
  global test

  def __init__(self):
    test = "test"
    if is_debug:
      onto = get_ontology("E:\\Homework\\Intelligent Agents\\PartPicker\\James25.owl").load()
    else:
      onto = get_ontology("James25.owl").load()
    obo = get_namespace("http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh")
    sync_reasoner()
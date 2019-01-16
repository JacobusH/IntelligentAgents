import tkinter as tk
from tkinter import ttk, Scrollbar, Listbox, font
from partPicker import get_classes, get_subclasses_recur, get_subclasses_onelevel, get_obo_elem, get_indivs
import math
import random

def assemble_parts(self):
	parts = []
	compName 	= self.comp_name.get()
	case 			= self.label_val_case['text']
	cpu 			= self.label_val_cpu['text']
	cooling 	= self.label_val_cooling['text']
	gpu 			= self.label_val_gpu['text']
	mem 			= self.label_val_mem['text']
	mobo 			= self.label_val_mobo['text']
	psu 			= self.label_val_psu['text']
	storage 	= self.label_val_storage['text']
	if case != "No Selection":
		parts.append(case)
	if cpu != "No Selection":
		parts.append(cpu)
	if cooling != "No Selection":
		parts.append(cooling)
	if gpu != "No Selection":
		parts.append(gpu)
	if mem != "No Selection":
		parts.append(mem)
	if mobo != "No Selection":
		parts.append(mobo)
	if psu != "No Selection":
		parts.append(psu)
	if storage != "No Selection":
		parts.append(storage)
	return parts

def replace_right_label(self, obo_elem, possib_parents):
  # find what parent this elem belongs to
  le_parent = recur_find_parent(self, obo_elem, possib_parents)
  # and then place the element as that parent's value in the build section
  if le_parent == "Case":
    self.label_val_case['text'] = obo_elem.name
  elif le_parent == "CPU":
    self.label_val_cpu['text'] = obo_elem.name
  elif le_parent == "Cooling":
    self.label_val_cooling['text'] = obo_elem.name
  elif le_parent == "GPU":
    self.label_val_gpu['text'] = obo_elem.name
  elif le_parent == "Memory":
    self.label_val_mem['text'] = obo_elem.name
  elif le_parent == "Motherboard":
    self.label_val_mobo['text'] = obo_elem.name
  elif le_parent == "PSU":
    self.label_val_psu['text'] = obo_elem.name
  elif le_parent == "Storage":
    self.label_val_storage['text'] = obo_elem.name

def recur_find_parent(self, cur_parent, possib_parents):
  if cur_parent is None or cur_parent == []:
    return None
  else:
    for new_parent in cur_parent.is_a: # is one of our direct parents a match?
      new_parent_name = new_parent.name
      for par in possib_parents:
        if par in new_parent_name: # we have a match
          return par
    return recur_find_parent(self, new_parent, possib_parents) # keep going
  

# i would do this simpler but each label val needs its own reference for text replacement...
def create_right_labels(self, frame):
		entry_text = "No Selection"
		### CPU
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_cpu = tk.Label(frame_tmp, text="CPU", width=10, anchor="w")
		label_name_cpu.pack(side="left", pady=8)
		self.label_val_cpu = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_cpu.pack(side="left")
		### Case
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_case = tk.Label(frame_tmp, text="Case", width=10, anchor="w")
		label_name_case.pack(side="left", pady=8)
		self.label_val_case = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_case.pack(side="left")
		### Cooling
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_cooling = tk.Label(frame_tmp, text="Cooling", width=10, anchor="w")
		label_name_cooling.pack(side="left", pady=8)
		self.label_val_cooling = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_cooling.pack(side="left")
		### GPU
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_gpu = tk.Label(frame_tmp, text="GPU", width=10, anchor="w")
		label_name_gpu.pack(side="left", pady=8)
		self.label_val_gpu = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_gpu.pack(side="left")
		### Memory
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_mem = tk.Label(frame_tmp, text="Memory", width=10, anchor="w")
		label_name_mem.pack(side="left", pady=8)
		self.label_val_mem = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_mem.pack(side="left")
		### Mobo
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_mobo = tk.Label(frame_tmp, text="Motherboard", width=10, anchor="w")
		label_name_mobo.pack(side="left", pady=8)
		self.label_val_mobo = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_mobo.pack(side="left")
		### PSU
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_psu = tk.Label(frame_tmp, text="PSU", width=10, anchor="w")
		label_name_psu.pack(side="left", pady=8)
		self.label_val_psu = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_psu.pack(side="left")
		### Storage
		frame_tmp = tk.Frame(frame)
		frame_tmp.pack(side="top")
		label_name_storage = tk.Label(frame_tmp, text="Storage", width=10, anchor="w")
		label_name_storage.pack(side="left", pady=8)
		self.label_val_storage = tk.Label(frame_tmp, text=entry_text, width=22, anchor="e", wraplength=120)
		self.label_val_storage.pack(side="left")

### if we didn't need named label vals could use this...
# for x in get_subclasses_onelevel("RDpBs6DXJfwjWljvKnjFFK7"): # for x in Parts
# 	frame_tmp = tk.Frame(frame_bot_right)
# 	frame_tmp.pack(side="top")
# 	self.create_entry_label(x, "Super long name that really really doesn't matter", frame_tmp)
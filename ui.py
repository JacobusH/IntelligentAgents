import tkinter as tk
from tkinter import ttk, Scrollbar, Listbox, font
from partPicker import get_classes, get_subclasses_recur, get_subclasses_onelevel, get_obo_elem, get_indivs, save_computer, find_missing_parts
from ui_helpers import create_right_labels, replace_right_label, assemble_parts, recur_indent
from newPart import find_part
import math
import random
from owlready2 import *

class Application(tk.Frame):
	is_debug = False
	onto = None
	obo = None

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		pad=3
		# create the ui
		self.create_widgets()

	def create_widgets(self):
		# init title frame
		self.create_title_frame()
		# init top frame
		self.create_top_parameters()
		# init middle frame
		frame_middle = tk.Frame(self, height=(rootHeight / 3) - 20, width=(rootWidth / 3) - 20)
		frame_middle.pack(side="bottom")
		self.create_mid_left_onto(frame_middle)
		self.create_mid_results(frame_middle)
		self.create_mid_right_build(frame_middle)
		# init bottom frame
		self.create_bottom_stats()

	#####
	# CREATE FRAMES
	#####
	def create_title_frame(self):
		frame_title = tk.Frame(self)
		frame_title.pack(side="top")
		self.title = tk.Label(frame_title, text="PC Part Picker", font=("Cambria", 28))
		self.title.pack(side="top")

	def create_top_parameters(self):
		frame_top = tk.Frame(self)
		# frame_top = tk.LabelFrame(self, text="PC Part Picker", pady=15)
		frame_top.pack(side="top")
		self.cur_cost_label = tk.Label(frame_top, text="Max Price")
		self.cur_cost_label.pack(side="left")
		self.cur_cost_val = tk.Entry(frame_top, width=10)
		self.cur_cost_val.pack(side="left", padx=10, pady=10)
		self.price_btn = tk.Button(frame_top, text="Set Price", fg="black", command=self.set_price)
		self.price_btn.pack(side="right")

	# MAKE LEFT COLUMN
	def create_mid_left_onto(self, frame_middle):
		frame_bot_left = tk.Frame(frame_middle, height=frame_colHeight, width=frame_colWidth)
		frame_bot_left.pack(side="left", fill="none", expand=True, padx=20, pady=20)
		### Computer | subclasses
		# self.create_combo_label("Pre-Built Computer", 'Computer', frame_bot_left)
		# ### Memory | subclasses
		# self.create_combo_label("Memory", "Memory", frame_bot_left)
		# ### Parts | subclasses
		# self.create_combo_label("Parts", "RDpBs6DXJfwjWljvKnjFFK7", frame_bot_left)
		# ### Peripherals | subclasses
		# # self.create_combo_label("Peripherals", "R6KTEriqId00kTIZki5blq", frame_bot_left)
		
		for x in get_subclasses_onelevel("RDpBs6DXJfwjWljvKnjFFK7"): # for x in Parts
			frame_tmp = tk.Frame(frame_bot_left)
			frame_tmp.pack(side="top")
			tmp_btn = tk.Button(frame_tmp, text=x, fg="black")
			tmp_btn.config(pady=2, width=17, height=2, command= lambda t=x, btn = tmp_btn: self.part_clicked(t, tmp_btn))
			tmp_btn.pack(side="top")

	# MAKE MIDDLE COLUMN
	def create_mid_results(self, frame_middle):
		frame_bot_mid = tk.Frame(frame_middle, bd=4, height=frame_colHeight, width=frame_colWidth)
		frame_bot_mid.pack(side="left")
		frame_scrollbar = tk.Frame(frame_bot_mid)
		frame_scrollbar.pack(side="left", fill="both", expand=True, padx=20, pady=20)

		# make scrollbar & listbox
		self.scrollbar = Scrollbar(frame_scrollbar)
		self.scrollbar.pack(side="right", fill="y")
		self.listbox = Listbox(frame_scrollbar, yscrollcommand=self.scrollbar.set, width=math.floor((rootWidth / 5) - 100 ), height=math.floor((rootHeight / 3) - 100 ))
		self.listbox.bind('<<ListboxSelect>>', self.lb_onselect)
		# for i in range(1000):
		# 	self.listbox.insert("end", str(i))
		self.listbox.pack(side="left", fill="both")
		self.scrollbar.config(command=self.listbox.yview)

	# MAKE RIGHT COLUMN
	def create_mid_right_build(self, frame_middle):
		frame_bot_right = tk.Frame(frame_middle, height=frame_colHeight, width=frame_colWidth)
		frame_bot_right.pack(side="left", fill="none", expand=True, padx=20, pady=20)
		# make the right labels and button
		create_right_labels(self, frame_bot_right)
		
	def create_bottom_stats(self):
		frame_bottom = tk.Frame(self)
		frame_bottom.pack(side="bottom")

		self.cur_cost_label = tk.Label(frame_bottom, text="Current Cost")
		self.cur_cost_label.pack(side="left")
		self.cur_cost_val = tk.Label(frame_bottom, text="100")
		self.cur_cost_val.pack(side="left", padx=10, pady=10)
	
	#####
	# HELPER FUNCTIONS
	#####
	def create_combo_label(self, label_name, combo_id, frame, is_IRIS = False):
		label_computer = tk.Label(frame, text=label_name, width=20, anchor="w")
		label_computer.pack(side="top")
		self.combo_computer = ttk.Combobox(frame, values=get_subclasses_onelevel(combo_id))
		self.combo_computer.current(1)
		self.combo_computer.pack(side="top")
		self.combo_computer.bind("<<ComboboxSelected>>", self.combo_selected)

	def create_entry_label(self, label_name, entry_text, frame):
		label_name = tk.Label(frame, text=label_name, width=10, anchor="w")
		label_name.pack(side="left", pady=8)
		label_val = tk.Label(frame, text=entry_text, width=22, anchor="e", wraplength=120)
		label_val.pack(side="left")
	
	#####
	# CALLBACKS
	#####
	def set_price(self, event):
		print("hallo")

	def part_clicked(self, text, btn):
		selected_piece = text
		sub_pieces = get_subclasses_recur(selected_piece)
		# now delete everything currently in the listbox
		self.listbox.delete(0, tk.END)
		recur_indent(self, text, sub_pieces, 0, 0)
		# special for memory only...
		if text == "Memory":
			for i in get_indivs("Memory"):
				self.listbox.insert("end", "{}".format(i.name))

	def save_computer(self):
		parts = assemble_parts(self)
		# save the comp to the onto so we can get it later
		new_computer = save_computer(self.comp_name.get(), parts)
		# for each missing part find the best part to suggest
		missing_parts = find_missing_parts(self.comp_name.get())
		missing_parts_obo = []
		for x in missing_parts:
			missing_parts_obo.append(get_obo_elem(x))
		sync_reasoner()
		# now find the suggested part
		new_parts = []
		# need to do mobo last
		le_mobo = None 
		for x in missing_parts_obo:
			if x.name != "Motherboard":
				good_part = find_part(new_computer, x)
				if good_part != None:
					new_parts.append(good_part)
					self.listbox_sugg.insert("end", "{}{}".format("Computer: ", (" " * 2) +self.comp_name.get())) # computer
					self.listbox_sugg.insert("end", "{}{}".format((" " * 4) +x._name, (" " * 10) +good_part.name)) # part , name
					self.listbox_sugg.insert("end", "{}{}".format(((" " * 10) +"Price: "), good_part.item_price[0])) # price
					self.listbox_sugg.insert("end", "{}{}".format(((" " * 10) +"Delivery Days: "), good_part.delivery_days[0])) # delivery days
			else:
				le_mobo = x
		# now do mobo
		if le_mobo != None:
			good_part = find_part(new_computer, x)
			new_parts.append(good_part)
			self.listbox_sugg.insert("end", "{}{}".format("Computer: ", (" " * 2) +self.comp_name.get())) # computer
			self.listbox_sugg.insert("end", "{}{}".format((" " * 4) +x._name, (" " * 10) +good_part.name)) # part , name
			self.listbox_sugg.insert("end", "{}{}".format(((" " * 10) +"Price: "), good_part.item_price[0])) # price
			self.listbox_sugg.insert("end", "{}{}".format(((" " * 10) +"Delivery Days: "), good_part.delivery_days[0])) # delivery days


	def toggle_geom(self, event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom

	### UNUSED
	def combo_selected(self, event):
		selected_piece = self.combo_computer.get()
		sub_pieces = get_subclasses_recur(selected_piece)
		# now delete everything currently in the listbox
		self.listbox.delete(0, tk.END)
		# now add the subpieces
		cur_parent = None
		last_parent = None
		for idx, elem in enumerate(sub_pieces):
			cur_parent = get_obo_elem(elem)
			if idx != 0:
				self.listbox.insert("end", "{:>15s}".format(elem))
			else:
				self.listbox.insert("end", elem)
			last_parent = cur_parent
		
	def lb_onselect(self, event):
		w = event.widget
		if w.curselection(): # we have an actual selection
			index = int(w.curselection()[0])
			value = w.get(index).lstrip().rstrip()
			# Place a randomly selected individual into the build
			indivs = get_indivs(value)
			if len(indivs) > 0:
				obo_elem = random.sample(indivs, 1)[0]
				possib_parents = get_subclasses_onelevel('RDpBs6DXJfwjWljvKnjFFK7')
				replace_right_label(self, obo_elem, possib_parents)
			else:
				print("Error: no individuals for this class")



# init the app
root = tk.Tk()
root.title("PC Part Picker")
root.attributes('-fullscreen', True)
# root.geometry("1500x1000")
# root.bind('<Escape>',lambda e: root.destroy())
root.bind('<Escape>',lambda e: root.iconify())
root.wm_state('iconic')
rootHeight = 700 # root.winfo_height()
rootWidth = 700 # root.winfo_width()
frame_colHeight = (rootHeight / 3) - 20
frame_colWidth = (rootWidth / 3) - 20
app = Application(master=root)

# method calls to the window manager class
app.master.title("PC Part Picker")
app.master.maxsize(1000, 400)

# start the app
app.mainloop()
import tkinter as tk
from tkinter import ttk, Scrollbar, Listbox, font
from partPicker import get_classes, get_subclasses
import math

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		pad=3
		self.create_widgets()

	def create_widgets(self):
		# init title frame
		self.create_title_frame()
		# init top frame
		self.create_top_parameters()
		# init middle frame
		frame_middle = tk.Frame(self, height=(rootHeight / 3) - 20, width=(rootWidth / 3) - 20, background = "pink")
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
		self.price_btn = tk.Button(frame_top, text="Set Price", fg="black", command=self.search)
		self.price_btn.pack(side="right")

	def create_mid_left_onto(self, frame_middle):
		frame_bot_left = tk.Frame(frame_middle, height=frame_colHeight, width=frame_colWidth)
		frame_bot_left.pack(side="left", fill="none", expand=True, padx=20, pady=20)
		### Computer | subclasses
		self.create_combo_label("Pre-Built Computer", "RzT3FDGFiwtff6PlbuV91w", frame_bot_left)
		### Memory | subclasses
		self.create_combo_label("Memory", "http://webprotege.stanford.edu/project/xpUFBIdmzwyCPpbfIg4hh#Memory", frame_bot_left, True)
		### Parts | subclasses
		self.create_combo_label("Parts", "RDpBs6DXJfwjWljvKnjFFK7", frame_bot_left)
		### Peripherals | subclasses
		self.create_combo_label("Peripherals", "R6KTEriqId00kTIZki5blq", frame_bot_left)

	def create_mid_results(self, frame_middle):
		frame_bot_mid = tk.Frame(frame_middle, bd=4, height=frame_colHeight, width=frame_colWidth)
		frame_bot_mid.pack(side="left")
		frame_scrollbar = tk.Frame(frame_bot_mid)
		frame_scrollbar.pack(side="left", fill="both", expand=True, padx=20, pady=20)

		# make scrollbar & listbox
		scrollbar = Scrollbar(frame_scrollbar)
		scrollbar.pack(side="right", fill="y")
		listbox = Listbox(frame_scrollbar, yscrollcommand=scrollbar.set, width=math.floor((rootWidth / 3) - 100 ), height=math.floor((rootHeight / 3) - 100 ))
		for i in range(1000):
			listbox.insert("end", str(i))
			listbox.pack(side="left", fill="both")
		scrollbar.config(command=listbox.yview)

	def create_mid_right_build(self, frame_middle):
		frame_bot_right = tk.Frame(frame_middle, height=frame_colHeight, width=frame_colWidth)
		frame_bot_right.pack(side="left", fill="none", expand=True, padx=20, pady=20)

		# for x in get_subclasses("RDpBs6DXJfwjWljvKnjFFK7"):	### NOTE: recursively gets subclasses... we want only first level
		for x in ['Case', 'MotherBoard', 'PSU', 'GPU', 'CPU', 'Case']:
			frame_tmp = tk.Frame(frame_bot_right)
			frame_tmp.pack(side="top")
			self.create_entry_label(x, "Super long name that really really doesn't matter", frame_tmp)

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
		combo_computer = ttk.Combobox(frame, values=get_subclasses(combo_id, is_IRIS))
		combo_computer.current(1)
		combo_computer.pack(side="top")

	def create_entry_label(self, label_name, entry_text, frame):
		label_name = tk.Label(frame, text=label_name, width=10, anchor="w")
		label_name.pack(side="left", pady=8)
		label_val = tk.Label(frame, text=entry_text, width=22, anchor="e", wraplength=120)
		label_val.pack(side="left")

	#####
	# CALLBACKS
	#####
	def say_hi(self):
		print("hi there, everyone!")

	def search(self):
		print("searching")

	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom



# init the app
root = tk.Tk()
root.title("PC Part Picker")
root.attributes('-fullscreen', True)
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
import tkinter as tk
from tkinter import ttk, Scrollbar, Listbox
from partPicker import get_classes, get_subclasses

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		# init top frame
		self.create_top_parameters()

		# init middle frame
		frame_middle = tk.Frame(self)
		frame_middle.pack(side="bottom")
		self.create_mid_left_onto(frame_middle)
		self.create_mid_results(frame_middle)
		self.create_mid_right_build(frame_middle)

		# init bottom frame
		self.create_bottom_stats()

	def create_combo_label(self, label_name, combo_id, frame):
		label_computer = tk.Label(frame, text=label_name, width=20, anchor="w")
		label_computer.pack(side="top")
		combo_computer = ttk.Combobox(frame, values=get_subclasses(combo_id))
		combo_computer.current(1)
		combo_computer.pack(side="top")

	def create_entry_label(self, label_name, entry_text, frame):
		label_name = tk.Label(frame, text=label_name, width=10, anchor="w")
		label_name.pack(side="left")
		label_val = tk.Label(frame, text=entry_text, width=10, anchor="e")
		label_val.pack(side="left")

	def create_top_parameters(self):
		frame_top = tk.Frame(self)
		frame_top.pack(side="top")

		self.cur_cost_label = tk.Label(frame_top, text="Max Price")
		self.cur_cost_label.pack(side="left")
		self.cur_cost_val = tk.Entry(frame_top, width=10)
		self.cur_cost_val.pack(side="left", padx=10, pady=10)
		self.price_btn = tk.Button(frame_top, text="Set Price", fg="black", command=self.search)
		self.price_btn.pack(side="right")

	def create_mid_left_onto(self, frame_middle):
		frame_bot_left = tk.Frame(frame_middle)
		frame_bot_left.pack(side="left")

		### Computer | subclasses
		self.create_combo_label("Pre-Built Computer", "RzT3FDGFiwtff6PlbuV91w", frame_bot_left)

		### Memory | subclasses
		self.create_combo_label("Memory", "RkhO2IgjEo6T4KIS84RuJr", frame_bot_left)

		### Parts | subclasses
		self.create_combo_label("Parts", "RDpBs6DXJfwjWljvKnjFFK7", frame_bot_left)

		### Peripherals | subclasses
		self.create_combo_label("Peripherals", "R6KTEriqId00kTIZki5blq", frame_bot_left)

	def create_mid_results(self, frame_middle):
		frame_bot_mid = tk.Frame(frame_middle, bd=4)
		frame_bot_mid.pack(side="left")
		frame_scrollbar = tk.Frame(frame_bot_mid)
		frame_scrollbar.pack(side="left")

		scrollbar = Scrollbar(frame_scrollbar)
		scrollbar.pack(side="right", fill="y")

		listbox = Listbox(frame_scrollbar, yscrollcommand=scrollbar.set)
		for i in range(1000):
			listbox.insert("end", str(i))
			listbox.pack(side="left", fill="both")

		scrollbar.config(command=listbox.yview)

	def create_mid_right_build(self, frame_middle):
		frame_bot_right = tk.Frame(frame_middle)
		frame_bot_right.pack(side="left")

		for x in get_subclasses("RDpBs6DXJfwjWljvKnjFFK7"):
			frame_tmp = tk.Frame(frame_bot_right)
			frame_tmp.pack(side="top")
			self.create_entry_label(x, "value", frame_tmp)

	def create_bottom_stats(self):
		frame_bottom = tk.Frame(self)
		frame_bottom.pack(side="bottom")

		self.cur_cost_label = tk.Label(frame_bottom, text="Current Cost")
		self.cur_cost_label.pack(side="left")
		self.cur_cost_val = tk.Label(frame_bottom, text="100")
		self.cur_cost_val.pack(side="left", padx=10, pady=10)
	

	def say_hi(self):
		print("hi there, everyone!")

	def search(self):
		print("searching")



# init the app
root = tk.Tk()
app = Application(master=root)

# method calls to the window manager class
app.master.title("PC Part Picker")
app.master.maxsize(1000, 400)

# start the app
app.mainloop()
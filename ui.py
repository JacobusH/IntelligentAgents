import tkinter as tk
from partPicker import get_classes

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.create_top_parameters()

		frame_bottom = tk.Frame(self)
		frame_bottom.pack(side="bottom")
		self.create_bot_left_onto(frame_bottom)
		self.create_bot_mid_results(frame_bottom)
		self.create_bot_right_build(frame_bottom)

		# frame_bottom = tk.Frame(self)
		# frame_bottom.pack(side="bottom")

		# self.hi_there = tk.Button(frame_bottom)
		# self.hi_there["text"] = "Hello World\n(click me)"
		# self.hi_there["command"] = self.say_hi
		# self.hi_there.pack(side="left")

		# self.quit = tk.Button(frame_bottom, text="QUIT", fg="red", command=self.master.destroy)
		# self.quit.pack(side="bottom")

		# self.test = tk.Label(frame_bottom, text="TestTest")
		# self.test.pack(side="right")

	def create_top_parameters(self):
		frame_top = tk.Frame(self)
		frame_top.pack(side="top")

		self.price_label = tk.Label(frame_top, text="Max Price")
		self.price_label.pack(side="left")
		self.price_entry = tk.Entry(frame_top, width=10)
		self.price_entry.pack(side="left", padx=10, pady=10)
		self.price_btn = tk.Button(frame_top, text="Search", fg="black", command=self.search)
		self.price_btn.pack(side="right")

	def create_bot_left_onto(self, frame_bottom):
		frame_bot_left = tk.Frame(frame_bottom)
		frame_bot_left.pack(side="left")

		self.test = tk.Label(frame_bot_left, text=get_classes())
		self.test.pack(side="left")

		

	def create_bot_mid_results(self, frame_bottom):
		frame_bot_mid = tk.Frame(frame_bottom)
		frame_bot_mid.pack(side="left")

		self.testt = tk.Label(frame_bot_mid, text="middy")
		self.testt.pack(side="left")

	def create_bot_right_build(self, frame_bottom):
		frame_bot_right = tk.Frame(frame_bottom)
		frame_bot_right.pack(side="left")

		self.testtt = tk.Label(frame_bot_right, text="righty")
		self.testtt.pack(side="left")


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
import tkinter as tk
from tkinter import filedialog, Text, simpledialog
import os
import webbrowser
import time
import pickle

def shortcut():
	root = tk.Tk()
	root.title('Shortcut Creator')
	apps = []
	websites = []
	shortcuts = {}
	try:
		with open('data\\shortcuts.pickle', 'rb') as f:
			old_shortcuts = pickle.load(f)
		shortcuts.update(old_shortcuts)

	except EOFError:
		pass

	def updateScreen(frame):
		for widget in frame.winfo_children():
			widget.destroy()

		for website in websites:
			label = tk.Label(frame, text=website, bg="gray")
			label.pack()
		for app in apps:
			label = tk.Label(frame, text=app, bg="gray")
			label.pack()

	def openApp(frame):

		filename = filedialog.askopenfilename(initialdir=r"/", title="Select an App", 
		filetypes=(("executables","*.exe"), ("all files","*.*")))
		if not filename:
			return
		else:
			apps.append(filename)

			updateScreen(frame)

	def openWebsite(frame):

		url = simpledialog.askstring(title="Website: ", prompt="Enter your website url here: ")

		if not url:
			return
		else:
			websites.append(url)
		
			updateScreen(frame)

	def save():
		shortcutName = simpledialog.askstring(title="Save Shortcut", prompt="Enter shortcut name here: ")
		shortcutVoiceCommand = simpledialog.askstring(title="Voice Command", prompt="Enter a special voice command to activate your shortcut here:")
		filename = os.getcwd() + r"\\" + str(shortcutName) + ".txt"
		if os.path.isfile(filename):
			os.remove(filename)
		with open(filename, 'w') as f:
			for app in apps:
				f.write(app + ",")
			f.write("\n")
			for website in websites:
				f.write(website + ",")
			
		shortcuts.update({shortcutVoiceCommand : shortcutName})

	def load(frame):
		shortcutName = simpledialog.askstring(title="Load Shortcut", prompt="Enter shortcut name here: ")
		filename = os.getcwd() + r"\\" + str(shortcutName) + ".txt"
		with open(filename, 'r') as f:
			old_apps = f.readline()
			old_apps = old_apps.split(",")
			old_apps = [x for x in old_apps if x.strip()]
			old_websites = f.readline()
			old_websites = old_websites.split(",")
			old_websites = [x for x in old_websites if x.strip()]
			apps.extend(old_apps)
			websites.extend(old_websites)

		for app in apps:
			label = tk.Label(frame, text=app, bg="gray")
			label.pack()
		
		for website in websites:
			label = tk.Label(frame, text=website, bg="gray")
			label.pack()


	def testShortcut():
		for app in apps:
			os.startfile(app)
		
		for website in websites:
			webbrowser.open(website, new=0, autoraise=True)


	canvas = tk.Canvas(root, height=400, width=700, bg="#999999")

	canvas.pack()

	frame = tk.Frame(root, bg="white")
	frame.place(relwidth=0.8, relheight=0.55, relx=0.1, rely=0.1)

	openAppButton = tk.Button(root, text="Open App", padx=10, pady=5, fg='#000000', bg='#999999', command=lambda:openApp(frame))
	openAppButton.pack()

	openWebsiteButton = tk.Button(root, text="Open Website", padx=10, pady=5, fg='#000000', bg='#999999', command=lambda:openWebsite(frame))
	openWebsiteButton.pack()

	runButton = tk.Button(root, text="Test Shortcut", padx=10, pady=5, fg='#000000', bg='#999999', command=lambda:testShortcut())
	runButton.pack()

	saveButton = tk.Button(root, text="Save Shortcut", padx=20, pady=5, fg='#000000', bg='#999999', command=lambda:save())
	saveButton.pack()

	loadButton = tk.Button(root, text="Load Shortcut", padx=20, pady=5, fg='#000000', bg='#999999', command=lambda:load(frame))
	loadButton.pack()

	root.mainloop()

	if os.path.isfile("data\\shortcuts.pickle"):
		os.remove("data\\shortcuts.pickle")

	with open('data\\shortcuts.pickle', 'wb') as f:
		pickle.dump(shortcuts, f)

if __name__ == "__main__":
	shortcut()
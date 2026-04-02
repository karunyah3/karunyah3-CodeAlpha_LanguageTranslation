import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END)
    lang = lang_entry.get()
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)

# Create window
root = tk.Tk()
root.title("Language Translator")
root.geometry("400x400")

# Input label
tk.Label(root, text="Enter Text:").pack()

# Input box
input_text = tk.Text(root, height=5)
input_text.pack()

# Language input
tk.Label(root, text="Target Language (ta, hi, fr):").pack()
lang_entry = tk.Entry(root)
lang_entry.pack()

# Translate button
tk.Button(root, text="Translate", command=translate_text).pack()

# Output label
tk.Label(root, text="Translated Text:").pack()

# Output box
output_text = tk.Text(root, height=5)
output_text.pack()

# Run app
root.mainloop()
import os
from groq import Groq
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk  
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ"))

def solve_math():
    problem = entry.get().strip()
    
    if problem == "":
        messagebox.showwarning("Анхаар!", "Та бодлогоо оруулна уу!")
        return

    try:
        response = client.chat.completions.create(   
            messages=[
                {"role": "user", "content": f"Тооны бодлого бод: {problem}"}
            ],
            model="llama-3.3-70b-versatile"
        )

        answer = response.choices[0].message.content
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, answer)
        result_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Алдаа гарлаа", str(e))

root = tk.Tk()
root.title(" AI Math Solver")
root.geometry("600x500")
root.config(bg="#1e1e2f") 

try:
    img = Image.open("ai_icon.jpg").resize((100, 100))  
    ai_icon = ImageTk.PhotoImage(img)
    icon_label = tk.Label(root, image=ai_icon, bg="#1e1e2f")
    icon_label.pack(pady=10)
except:
    pass  

title_label = tk.Label(
    root, text="AI Тоо бодогч", 
    font=("Helvetica", 22, "bold"), fg="#00ffcc", bg="#1e1e2f"
)
title_label.pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 18), width=30, justify="center")
entry.pack(pady=10)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=5)

solve_btn = tk.Button(
    btn_frame, text="Бодолт авах", font=("Helvetica", 14, "bold"),
    command=solve_math, bg="#00bfff", fg="white", width=15
)
solve_btn.grid(row=0, column=0, padx=10)

exit_btn = tk.Button(
    btn_frame, text="Гарах", font=("Helvetica", 14, "bold"),
    command=root.quit, bg="#ff4c4c", fg="white", width=15
)
exit_btn.grid(row=0, column=1, padx=10)

result_text = scrolledtext.ScrolledText(
    root, height=10, font=("Courier New", 18), bg="#2b2b3a", fg="#ffffff", wrap=tk.WORD
)
result_text.pack(pady=20, padx=10, fill="both", expand=True)
result_text.config(state="disabled")

root.mainloop()
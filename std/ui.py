import tkinter as tk
from tkinter import messagebox
import subprocess
import tempfile
import os
import ctypes


def _monitor_count():

    try:
        return int(ctypes.windll.user32.GetSystemMetrics(80))
    except:
        return 1


def _open_rdp(host,user,multi,ask):

    mons=_monitor_count()
    use_multi=False

    if multi:

        if mons>=2:

            if ask:

                use_multi=messagebox.askyesno(
                    "RDP",
                    f"Detectats {mons} monitors.\nVols obrir amb 2 monitors?"
                )

            else:

                use_multi=True

    lines=[f"full address:s:{host}"]

    if use_multi:
        lines.append("use multimon:i:1")
    else:
        lines.append("use multimon:i:0")

    content="\n".join(lines)+"\n"

    fd,path=tempfile.mkstemp(prefix="std_",suffix=".rdp")
    os.close(fd)

    with open(path,"w") as f:
        f.write(content)

    subprocess.Popen(["mstsc",path])


def run_app():

    root=tk.Tk()
    root.title("STD 7")
    root.geometry("400x250")

    tk.Label(root,text="STD RDP Test",font=("Segoe UI",14)).pack(pady=20)

    multi=tk.BooleanVar()
    ask=tk.BooleanVar()

    tk.Checkbutton(root,text="Multimonitor",variable=multi).pack()
    tk.Checkbutton(root,text="Preguntar",variable=ask).pack()

    tk.Button(
        root,
        text="Obrir RDP",
        command=lambda:_open_rdp("127.0.0.1","",multi.get(),ask.get())
    ).pack(pady=20)

    root.mainloop()
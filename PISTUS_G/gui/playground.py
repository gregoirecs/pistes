"""Used to play with the code in order to learn the basics of Tkinter.

"""

# Import the library tkinter
import tkinter as tk
# Import the ttk widgets of tkinter
from tkinter import ttk
# Import the function configure_style
from gui_config import configure_style


###################### You'll copy here the code to play with ######################

""" QUESTION 15 : 
"""
"""
window = tk.Tk()
window.title("Playground")
configure_style()
first_frame = ttk.Frame(window, style="Sample.TFrame")
first_label = ttk.Label(first_frame, text="First label", style="Sample.TLabel")
first_text_field_var = tk.StringVar(value="")
first_text_field = ttk.Entry(first_frame, textvariable=first_text_field_var)
first_button = ttk.Button(first_frame, text="First button")
first_label.pack(fill=tk.Y, expand=True)
first_text_field.pack()
first_button.pack()
first_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
window.mainloop()
"""

"""QUESTION 16 :
     POSITION OF THE WIDGET : 
     LIGNE 9, ON A FAIT EN SORTE QUE LE LABEL SOIT COLLÉ A GAUCHE
     ALORS QUE DE BASE IL EST PLACE EN HAUT
     EN LE COLLANT A GAUCHE, IL N'Y A PLUS RIEN AU DESSUS 
     DE LA ZONE TEXTE DONC ELLE REMONTE ET SE MET EN HAUT'
     
     
     
     """
"""QUESTION 17 : """

"""

window = tk.Tk()
window.title("Playground")
configure_style()

first_frm = ttk.Frame(window, style="Sample.TFrame")
ttk.Label(first_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 0)", style="Sample.TLabel").grid(row=1, column=0, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 1)", style="Sample.TLabel").grid(row=1, column=1, padx=10, pady=10)
first_frm.columnconfigure(0, weight=1)
first_frm.columnconfigure(1, weight=1)
# Ce qui est modifié pour la question 17 : 
first_frm.pack(fill=tk.BOTH, expand=True)

second_frm = ttk.Frame(window, style="SampleBottom.TFrame")
ttk.Label(second_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 2)", style="Sample.TLabel").grid(row=0, column=2, padx=10, pady=10)
second_frm.pack()

window.mainloop() 

"""
# SUITE QUESTION 17: 
"""
window = tk.Tk()
window.title("Playground")
configure_style()

first_frm = ttk.Frame(window, style="Sample.TFrame")
ttk.Label(first_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10, sticky='ew')
ttk.Label(first_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 0)", style="Sample.TLabel").grid(row=1, column=0, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 1)", style="Sample.TLabel").grid(row=1, column=1, padx=10, pady=10)
first_frm.columnconfigure(0, weight=1)
first_frm.columnconfigure(1, weight=1)
# Ce qui est modifié pour la question 17 : 
first_frm.pack(fill=tk.BOTH, expand=True)

second_frm = ttk.Frame(window, style="SampleBottom.TFrame")
ttk.Label(second_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 2)", style="Sample.TLabel").grid(row=0, column=2, padx=10, pady=10)
second_frm.pack()

window.mainloop()
"""

# EVENT HANDLING : 
"""
entries = {}
buttons = {}

def click_ok_handler():
    print("The user clicked OK")

def check_first_ent(*args):
    text_field_content = entries["first_ent"][1].get().strip()
    print("The user typed {}".format(text_field_content) )
    if text_field_content[-1] == "#":
        ok_enabled_state()
    else:
        ok_disabled_state()

def ok_enabled_state():
    buttons["OK"].configure(state=["!disabled"])
    print("The button is now enabled")

def ok_disabled_state():
    buttons["OK"].configure(state=["disabled"])
    print("The button is now disabled")

window = tk.Tk()
window.title("Playground")
configure_style()
first_frm = ttk.Frame(window, style="Tab.TFrame")

first_ent_var = tk.StringVar(value="")
first_ent = ttk.Entry(first_frm, textvariable=first_ent_var)
first_ent_var.trace("w", check_first_ent)
entries["first_ent"] = (first_ent, first_ent_var)
first_ent.pack()

button = ttk.Button(first_frm, state="disabled", text="OK", command=click_ok_handler)
buttons["OK"] = button
button.pack()
first_frm.pack()
window.mainloop()
"""
"""Question 18"""
"""
radio_buttons = {} #dico vide pour stocker les boutons radio
buttons = {} #dico pour stocker les boutons

def click_ok_handler():
    # si quelqu'un clique sur le bouton OK, alors la fonction est appelé
    # et on ecrit qu'il a clique sur OK
    print("The user clicked OK")

def rb_selected(*args):
    # fonction appelé à chaque fois que la selection des boutons radio change
    current_value = radio_buttons["enable_disable"][2].get() #on recupere la valeur du bouton selectionné
    if current_value == 'E':
        # si le bouton doit etre active on appelle la fonction qui l'active
        ok_enabled_state()
    elif current_value == 'D':
        # sinon on appelle la fonction qui le désactive
        ok_disabled_state()

def ok_enabled_state():
    buttons["OK"].configure(state=["!disabled"])
    #le bouton devient actif lorsque cette fonction est appelé
    print("The button is now enabled")
    # on indique que le button est actif

def ok_disabled_state():
    buttons["OK"].configure(state=["disabled"])
    #le bouton devient inactif lorsque cette fonction est appelé
    print("The button is now disabled")
    #on indique que le button est actif

window = tk.Tk() #on créé  une fenetre tkinter
window.title("Playground") #son titre est Playground
configure_style()
first_frm = ttk.Frame(window, style="Tab.TFrame") # on fait un cadre comme précedemment

rb_value = tk.StringVar(value="") #creation d'une variable
rb_value.trace("w", rb_selected) # a chaque fois que la variable rb_value est modifié on appelle rb_selected,
# cela signifie que la selection des boutons radio change
enable_rb = ttk.Radiobutton(first_frm, text='Enable', value='E', variable=rb_value)
# on crée des boutons radio au sein du cadre, un 'Enable', ils sont liés a la variable rb_value
disable_rb = ttk.Radiobutton(first_frm, text='Disable', value='D', variable=rb_value)
# l'autre 'disable'
radio_buttons["enable_disable"] = (enable_rb, disable_rb, rb_value)
# on ajoute les boutons radio au dico radio_buttons, on associe la rb_value à la clé "enable_diable"
enable_rb.pack() # affichage bouton enable
disable_rb.pack()# affichage bouton disable

button = ttk.Button(first_frm, state="disabled", text="OK", command=click_ok_handler)
# on ajoute un bouton ok, qui est d'abord désactivé
buttons["OK"] = button #ajout bouton ok au dico button
button.pack() #affichage button ok
first_frm.pack() #affichage du cadre
window.mainloop()
"""



""" QUESTION 19 : 
    
How boxes are created ?
on créé une liste avec les couleurs : colors
on utilise le tkk.Comobox widget : il crée une liste deroulante
dite combobox alors on doit specifier les valeurs que l'on souhaite
afficher dans le menu deroulant, ce sont les couleurs du dictionnaire colors '
il s'affiche dans la fenetre que l'on indique en premier argument
Par la suite on stocke ce combobox dans un dictionnaire pour en garder trace

Event Handling ?
on utilise la methode 'bind' : 
on a un evenement <<ComboboxSelected>> qui s'ative lorsque une couleur est 
selectionné, alors cela implique l'appel de la fct combo_selected
qui reconnait la couleur actuelle selectionné et l'affiche au dessus'

de maniere generale bind permet d'associer des événements à des widgets dans l'interface utilisateur Tkinter
"""
"""
combo_boxes = {}
buttons = {}
control_labels = {}

window = None

def combo_selected():
    current_color = combo_boxes["color"].get()
    control_labels["color_ctrl"].configure(text="The selected color is {}".format(current_color))

def destroy_window():
    window.destroy()

window = tk.Tk()
window.title("Playground")
configure_style()
first_frm = ttk.Frame(window, style="Tab.TFrame")

ctrl_label = ttk.Label(first_frm)
control_labels["color_ctrl"] = ctrl_label
ctrl_label.pack()

colors = ["red", "green", "blue", "yellow"]
color_combo = ttk.Combobox(first_frm, values=colors)
combo_boxes["color"] = color_combo
color_combo.bind("<<ComboboxSelected>>", \
        lambda event: combo_selected())
color_combo.pack()

button = ttk.Button(first_frm, text="Destroy", command=destroy_window)
buttons["OK"] = button
button.pack()

first_frm.pack()
window.mainloop()
"""


#Autre test : 
"""
username_lbl_text = "message 1 : "
password_lbl_text = "message 2 : "

window = tk.Tk()
window.title("Playground")
configure_style()
frame = ttk.Frame(window, style="Sample.TFrame")

style = ttk.Style()
style.configure("Sample.TFrame", background="white")

first_label = ttk.Label(frame, text= username_lbl_text)
first_label.pack(fill=tk.Y)
    
first_text_field_var = tk.StringVar(value="")
first_text_field = ttk.Entry(frame, textvariable=first_text_field_var)
first_text_field.pack()

second_label = ttk.Label(frame, text=password_lbl_text)
second_label.pack(fill=tk.Y)

second_text_field_var = tk.StringVar(value="")
second_text_field = ttk.Entry(frame, textvariable=second_text_field_var, show='*')
second_text_field.pack()
    
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
window.mainloop()
"""

# Text in the button "Login".
login_btn_text = "1"

    # Text in the button clear.
clear_btn_text = "2"

    # Text in the button cancel.
cancel_btn_text = "3"

    ############ TODO: WRITE HERE THE CODE TO IMPLEMENT THIS FUNCTION ##########
window = tk.Tk()
configure_style()
first_frm = ttk.Frame(window, style="Tab.TFrame")
button_login = ttk.Button(first_frm, text=login_btn_text)
button_login.pack()
button_clear = ttk.Button(first_frm, text=clear_btn_text)
button_clear.pack()
button_cancel = ttk.Button(first_frm, text=cancel_btn_text)
button_cancel.pack()
first_frm.pack()
window.mainloop()
#####################################################################################

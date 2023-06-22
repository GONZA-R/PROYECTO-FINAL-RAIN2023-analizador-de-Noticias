import tkinter as tk

def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel(ventana_principal)
    boton_volver = tk.Button(ventana_secundaria, text="Volver", command=ventana_secundaria.destroy)
    boton_volver.pack()

# Crear ventana principal
ventana_principal = tk.Tk()

# Crear botón que abrirá la ventana secundaria
boton_abrir = tk.Button(ventana_principal, text="Abrir", command=abrir_ventana_secundaria)
boton_abrir.pack()

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()

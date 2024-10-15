import menu
import sys
import gestor_clientes

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.iniciar()
    else:
        app = gestor_clientes.MainWindow()
        app.mainloop()


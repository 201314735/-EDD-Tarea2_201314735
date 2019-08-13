import os
import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library



global matriz

def paint_menu(win):
    paint_title(win,' FILAS ')          #paint title
    win.addstr(7,21, 'Ingresar número de filas: ')
    filas = window.getch()
    filas=int(str(chr(filas)))

    paint_title(win, ' COLUMNAS ')  # paint title
    win.addstr(7, 21, 'Ingresar número de columnas: ')
    columnas = window.getch()
    columnas=int(str(chr(columnas)))
    global matriz
    matriz= [filas],[columnas]
    k=0

    pos=0
    while k < filas:
        l = 0
        while l < columnas:
            pos=pos+1
            l=l+1
        k=k+1

    paint_title(win, ' POSICIÓN')  # paint title
    win.addstr(7, 21, 'Posición de fila a linealizar: ')
    i = window.getch()
    i=int(str(chr(i)))
    i=i-1

    paint_title(win, ' POSICIÓN ')  # paint title
    win.addstr(7, 21, 'Posición de columna a linealizar: ')
    j = window.getch()
    j=int(str(chr(j)))
    j=j-1

    paint_title(win, ' SELECCIONAR')  # paint title
    win.addstr(7, 21, '1. Mapeo por Filas: ')
    win.addstr(8, 21, '2. Mapeo por Columnas: ')
    opc = window.getch()

    win.timeout(-1)                         #wait for an input thru the getch() function

    if opc==49:

        resultado = (i*columnas)+j
        paint_title(win, ' RESULTADO')  # paint title
        win.addstr(7, 21, 'Resultado = Posición: '+str(resultado))

        file = open("Graphiz.dot", "w")
        file.write("digraph Programa {\n")
        file.write("\n\tsubgraph matriz{\nnode[shape=box]\n")

        file.write("tbl [ shape=plaintext\n label=<\n  <table border='0' cellborder='1' color='blue' cellspacing='0'>")

        x=0

        while x < filas:
            file.write("\n <tr>")
            y = 0
            while y < columnas:
               if (i == x and j == y):
                   file.write("<td bgcolor='lightblue'>"+str(x)+","+str(y)+"</td>")
               else:
                   matriz=[x],[y]
                   file.write("<td>"+str(x)+","+str(y)+"</td>")
               y=y+1
            file.write("</tr>")
            x = x+1
        file.write("\n </table>\n>];}")

        file.write("\n\tsubgraph filas{")
        file.write("tabl [ shape=plaintext\n label=<\n  <table border='0' cellborder='1' color='blue' cellspacing='0'>")
        file.write("\n <tr>")

        w=0
        while w<pos:
            file.write("<td>"+str(w)+"</td>")
            w=w+1
        file.write("\n </tr>")
        file.write("\n <tr>")

        z=0

        while z<filas:
            c = 0
            while c<columnas:
                if (i == z and j == c):
                    file.write("<td bgcolor='lightblue'>"+str(z)+","+str(c)+"</td>")
                else:
                    matriz=[z],[c]
                    file.write("<td>"+str(z)+","+str(c)+"</td>")
                c=c+1
            z=z+1

        file.write("</tr>")
        file.write("\n </table>\n>];}")

        file.write("\n\t}")
        file.close()

        os.system("dot -Tpng Graphiz.dot -o Graphiz.png")
        os.system("xdg-open Graphiz.png")

        esc = window.getch()
        if (esc==27):
            paint_menu(window)
        win.timeout(-1)


    if opc==50:

        resultado = (j*filas)+i
        paint_title(win, ' RESULTADO')  # paint title
        win.addstr(7, 21, 'Resultado = Posición: '+str(resultado))

        file = open("Graphiz.dot", "w")
        file.write("digraph Programa {\n")
        file.write("\n\tsubgraph matriz{\nnode[shape=box]\n")

        file.write("tbl [ shape=plaintext\n label=<\n  <table border='0' cellborder='1' color='blue' cellspacing='0'>")

        x=0

        while x < filas:
            file.write("\n <tr>")
            y = 0
            while y < columnas:
               if (i == x and j == y):
                   file.write("<td bgcolor='lightblue'>"+str(x)+","+str(y)+"</td>")
               else:
                   matriz=[x],[y]
                   file.write("<td>"+str(x)+","+str(y)+"</td>")
               y=y+1
            file.write("</tr>")
            x = x+1
        file.write("\n </table>\n>];}")

        file.write("\n\tsubgraph columnas{")
        file.write("tabl [ shape=plaintext\n label=<\n  <table border='0' cellborder='1' color='blue' cellspacing='0'>")
        file.write("\n <tr>")

        w=0
        while w<pos:
            file.write("<td>"+str(w)+"</td>")
            w=w+1
        file.write("\n </tr>")
        file.write("\n <tr>")

        z=0

        while z<columnas:
            c = 0
            while c<filas:
                if (i == c and j == z):
                    file.write("<td bgcolor='lightblue'>"+str(c)+","+str(z)+"</td>")
                else:
                    matriz=[c],[z]
                    file.write("<td>"+str(c)+","+str(z)+"</td>")
                c=c+1
            z=z+1

        file.write("</tr>")
        file.write("\n </table>\n>];}")

        file.write("\n\t}")
        file.close()

        os.system("dot -Tpng Graphiz.dot -o Graphiz.png")
        os.system("xdg-open Graphiz.png")

        esc = window.getch()
        if (esc==27):
            paint_menu(window)
        win.timeout(-1)




def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()


stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)

curses.endwin() #return terminal to previous state
from search import *
import tkinter as tk
"""
CS 481 Project 2, NQueensProblem Genetic Search
Colin Hughes
"""

def print_row(i, numb):
    # iterate through positions and mark where the queen is
    print("[" + str(i) + "]", end='')
    for x in range(numb):
        if x == i:
            print(" X ", end='')
        else:
            print(" - ", end='')
    print()  # print newline

def print_queen(path, numb):
    print(str(numb) + "QueensProblem result:")
    for i in path:
        print_row(i, numb)

def string_row(i, numb):
    # iterate through positions and mark where the queen is
    str_result = ""
    for x in range(numb):
        if x == i:
            str_result += " x "
        else:
            str_result += " - "
    return str_result

def string_queen(path, numb):
    str_result = ""
    for i in path:
        str_result += string_row(i, numb) + "\n"
    return str_result

def queen_gen(numb=8, gennumb=10, mutnumb=0.1, pnumb=100):
    # retrieve inputs from GUI
    numb = int(e_q.get())
    gennumb = int(e_g.get())
    mutnumb = float(e_m.get())
    pnumb = int(e_p.get())
    # correct mutation to be in range of 0-1
    mutnumb = min(1,mutnumb)
    mutnumb = max(0,mutnumb)

    # perform the genetic search
    nqn = NQueensProblem(numb)
    gn_path = genetic_search(nqn, ngen=gennumb, pmut=mutnumb, n=pnumb)
    # change label displaying pairs found
    l_pair.configure( text="Minimum Attacking Pairs Found: "+ str(int(NQueensProblem.gen_h(nqn, gn_path) / 2)) )
    # change label to show the position of the pieces
    # print_queen(gn_path, len(gn_path))
    l_table.configure( text=string_queen(gn_path, len(gn_path)) )

if __name__ == '__main__':
    # GUI
    window = tk.Tk()  # create the window

    # create all frames in advance
    f_entry = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)
    f_entry.grid(row=0, column=0)
    f_table = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
    f_table.grid(row=1, column=0)

    # run button
    b_run = tk.Button(master=f_entry, text="RUN SEARCH", height=3, width=14, bg="grey", command=queen_gen)
    b_run.pack(side=tk.LEFT)

    # queen entry
    f_q = tk.Frame(master=f_entry, relief=tk.FLAT, borderwidth=5)
    l_q = tk.Label(master=f_q, text="Number of Queens")
    l_q.pack()
    e_q = tk.Entry(master=f_q, width=8, justify=tk.RIGHT)
    e_q.pack()
    e_q.insert(0, 8)
    f_q.pack(side=tk.LEFT)

    # generation entry
    f_g = tk.Frame(master=f_entry, relief=tk.FLAT, borderwidth=5)
    l_g = tk.Label(master=f_g, text="Number of Generations")
    l_g.pack()
    e_g = tk.Entry(master=f_g, width=8, justify=tk.RIGHT)
    e_g.pack()
    e_g.insert(0, 10)
    f_g.pack(side=tk.LEFT)

    # mutation entry
    f_m = tk.Frame(master=f_entry, relief=tk.FLAT, borderwidth=5)
    l_m = tk.Label(master=f_m, text="Rate of Mutation (0~1)")
    l_m.pack()
    e_m = tk.Entry(master=f_m, width=8, justify=tk.RIGHT)
    e_m.pack()
    e_m.insert(0, 0.1)
    f_m.pack(side=tk.LEFT)

    # population entry
    f_p = tk.Frame(master=f_entry, relief=tk.FLAT, borderwidth=5)
    l_p = tk.Label(master=f_p, text="Size of Population")
    l_p.pack()
    e_p = tk.Entry(master=f_p, width=8, justify=tk.RIGHT)
    e_p.pack()
    e_p.insert(0, 100)
    f_p.pack(side=tk.LEFT)

    # table
    l_pair = tk.Label(master=f_table, text="Minimum Attacking Pairs Found: N/A", font=("Arial", 16))
    l_pair.pack()
    l_table = tk.Label(master=f_table, text="", font=("Arial", 24))
    l_table.pack()

    # display the window
    window.mainloop()

import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3

import csv
from aquisicao_dados import aquisicao_dados
from classificacao import classificação
from leitura import leitura_amostras


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Times New Roman', size=18, slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#B6B6B6')
        self.controller = controller
        self.controller.geometry('800x600')

        label = tk.Label(self, text="All Aditive Analyser", font=controller.title_font, bg="#B6B6B6")
        label.pack(side="top", fill="x", pady=90, padx = 300)

        button1 = tk.Button(self, text="Adicionar novas medidas", font=controller.title_font,
                            command=lambda: controller.show_frame("PageOne"), height=5, width=20)
        button1.pack(padx=10, pady=10)

        button2 = tk.Button(self, text="Ver medidas salvas", font=controller.title_font,
                            command=lambda: controller.show_frame("PageTwo"), height=5, width=20)
        button2.pack(padx=10, pady=10)


class PageOne(tk.Frame):
    lista = leitura_amostras()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#B6B6B6')
        self.controller = controller

        def Resposta():
            # Aquisição dos Dados
            dados, nova_amostra = aquisicao_dados(E_temp.get(), E_acid.get(), E_turbid.get(), E_densid.get())

            # Classificação do Aditivo e Salvar a Nova Amostra
            value = classificação(dados, nova_amostra)
            resultado = tk.Label(self, text="O aditivo é: " + str(value), bg='#CDCDCD')
            resultado.grid(row=3, column=3)

            # PageOne.lista.append(nova_amostra)

        button = tk.Button(self, text="<-- MENU", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=0)

        label = tk.Label(self, text="Digite as medidas \n obtidas experimentalmente:", bg='#B6B6B6')
        label.grid(row=1, column=2, pady=20)

        L_temp = tk.Label(self, text="T.combustão (ºC):", bg='#B6B6B6')
        L_temp.grid(row=2, column=1, pady=20)
        L_acid = tk.Label(self, text="Grau de acidez (Ph):", bg='#B6B6B6')
        L_acid.grid(row=3, column=1, pady=20)
        L_turbid = tk.Label(self, text="Turbidez (1 a 6):", bg='#B6B6B6')
        L_turbid.grid(row=4, column=1, pady=20)
        L_densid = tk.Label(self, text="Densidade (kg/l):", bg='#B6B6B6')
        L_densid.grid(row=5, column=1, pady=20)

        E_temp = tk.Entry(self, borderwidth='2')
        E_temp.grid(row=2, column=2, pady=20)
        E_temp.insert(0, "0.000")
        E_acid = tk.Entry(self, borderwidth='2')
        E_acid.grid(row=3, column=2, pady=20)
        E_acid.insert(0, "0.000")
        E_turbid = tk.Entry(self, borderwidth='2')
        E_turbid.grid(row=4, column=2, pady=20)
        E_turbid.insert(0, "0.000")
        E_densid = tk.Entry(self, borderwidth='2')
        E_densid.grid(row=5, column=2, pady=20)
        E_densid.insert(0, "0.000")

        button_2 = tk.Button(self, text="Cálculo da composição",
                             command=Resposta)
        button_2.grid(row=2, column=3, padx=30)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#B6B6B6')
        self.controller = controller

        def Reload():
            resultados.delete(0, "end")
            arquivo_aquisicao = leitura_amostras()
            for item in arquivo_aquisicao:
                resultados.insert('end', item)

        button = tk.Button(self, text="<-- MENU",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=0)

        label = tk.Label(self, text="Resultados anteriores", font=controller.title_font)
        label.grid(row=1, column=1, pady=10)

        resultados = tk.Listbox(self, height=30, width=110)
        resultados.grid(row=2, column=1)

        # attaching it to root window
        scrollbar = tk.Scrollbar(self)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.grid(row=2, column=2,sticky=tk.NS)

        resultados.config(yscrollcommand=scrollbar.set)

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=resultados.yview)

        button_r = tk.Button(self, text="Reload",
                             command=Reload)
        button_r.grid(row=3, column=1, pady=5)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

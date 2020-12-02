from tkinter import *
check = 0
bhop = 0
class Application:
    #funçao para criar a interfaçe, ela cria os containers e as labels da interfaçe
    def __init__(self, master=None):
        #define fonte e containers
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        #entry para botar a pergunta
        self.a = Entry(self.quartoContainer)
        self.a["width"] = 40
        self.a["font"] = self.fontePadrao
        self.a.pack(side=LEFT)

        #script do botao
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "enviar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.pergunta #chama a funçao pergunta ao clicar no botão
        self.autenticar.pack(side=RIGHT)

        #label onde fica a resposta
        self.mensagem = Label(self.segundoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack(side=LEFT)


        #label onde fica a pergunta
        self.oldmensagem = Label(self.primeiroContainer, text=""""Informações sobre a formatação das perguntas: Perguntas de especulação começam com "Será" (Exemplo: "Será que vai chuver hoje")
Perguntas de decisão começam com "Eu deveria" (Exemplo: "Eu deveria comer fora hoje?")
Perguntas de escolha entre varias começam com "Qual" (Exemplo: "Qual genero de musica deveria ouvir?")
Perguntas de data ou horario começam com "Quando" (Exemplo: "Quando foi proclamada a independencia do Brasil?")
Perguntas de quantidade começam com "Quanto" (Exemplo: "Quanto está o dollar hoje?")
Perguntas de ordem começam com "Me" (Exemplo: "Me conte uma piada?")
""", font=self.fontePadrao)
        self.oldmensagem.pack(side=RIGHT)     

    #função para a resposta do horoscopo
    def signo(self):
        a = self.a.get()
        global verificacao
        global bhop
        if a.lower() == "aries" or a.lower() == "áries":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Agradeça aos antepassados pela sabedoria recebida que será valorosa nestes tempos de mudanças e de provações."
            bhop = 1
        if a.lower() == "touro":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Mesmo no feriado, negociações de trabalho estarão em andamento. A semana sinaliza mudanças nas parcerias e novas conexões."
            bhop = 1
        if a.lower() == "gêmeos" or a.lower() == "gemeos":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Mercúrio, seu planeta regente, andando para a frente, movimentará a semana com ideias criativas e soluções originais."
            bhop = 1
        if a.lower() == "câncer" or a.lower() == "cancer":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Encontre um ponto de equilíbrio entre o que você deseja e o que será possível realizar neste período de restrições."
            bhop = 1
        if a.lower() == "leão" or a.lower() == "leao":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Semana importante na carreira. Ganhe popularidade e projeção. Mercúrio andando para a frente facilitará divulgações e comunicações de trabalho."
            bhop=1
        if a.lower() == "virgem":
            self.oldmensagem["text"] = ""
            verificacao = 1
            self.mensagem["text"] = "Negociações financeiras terão andamento positivo nesta semana, com Mercúrio já em movimento direto."
            bhop=1
        if a.lower() == "libra":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Determine objetivos, planeje uma viagem com antecedência e inicie relações num novo padrão."
            bhop=1
        if a.lower() == "escorpião" or a.lower() == "escorpiao":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Novidades chegarão por todos os lados, nesta semana. Pense positivo e impulsione novo projeto de trabalho."
            bhop=1
        if a.lower() == "sagitário" or a.lower() == "sagitario":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Entendimento com parceiros, equipe e amizades movimentarão negócios, nesta semana."
            bhop=1
        if a.lower() == "capricórnio" or a.lower() == "capricornio":
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Aprove um projeto, amplie comunicações profissionais e aposte em metas mais altas. Mercúrio em movimento direto impactará diretamente na carreira."
            bhop=1
        if a.lower() == "aquário" or a.lower() == "aquario":
            bhop = 1
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "A semana será decisiva no amor. Renove os sentimentos e aumente a confiança nos projetos da vida íntima. Mercúrio em movimento direto trará mais otimismo."
        if a.lower() == "peixes":
            bhop = 1
            verificacao = 1
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Decisões financeiras envolverão a família e o amor. A semana favorecerá o casamento e associações."
        else:
            if bhop == 0:
                self.oldmensagem["text"] = "Não conseguimos responder isso"
                self.mensagem["text"] =  ""
            else:
                bhop = 0

    #funçao que é chamada quando o botão é presionado, ela faz a conversão das perguntas, e da as respostas       
    def pergunta(self):
        global check
        listaPerguntas=["Eu deveria comer fora hoje?","Qual meu horoscopo de hoje?","Eu deveria trocar de roupa?","Qual genero de musica deveria ouvir?","Eu deveria ir jogar VideoGame?",
        "Quando vai acabar as aulas do curso tecnico?","Será que vai chover hoje?","Eu deveria assistir Bakemonogatari?","Quando é o dia dos finados?",
        "Quantos livros tem a bíblia?","Quanto está o dólar hoje?","Quando foi proclamada a independencia do Brasil?",
        "Quantos paises existem no mundo?","Será que a terra é plana?",
        "Qual o tempo para cozinhar um ovo?", "Quais são as cores do arco íris?","Me conta uma piada?","Me recomenda uma musica?","Quem é o presidente do Brasil?"]
        listaRespostas=["Depende, como está o clima?","Depende, qual seu signo?","Sim, ela não está apropriada com o clima de hoje!","Você deveria ouvir ROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCK.","Não!! Você está em aula cara!",
        "Dia 4 de Dezembro.","Sim, hoje vai chover.","Sim, assista.","2 de novembro.",
        "73 livros.", "Atualmente um dolar esta no valor de 5,31 no Real brasileiro.",
        "Dia 7 de setembro de 1822.","Atualmente existem 193 países internacionalmente reconhecidos.","Não, até onde eu saiba.","12 minutos.",
        "O arco-íris aparece em sete cores: Violeta, anil, azul, verde, amarelo, laranja e vermelho.","Por que o penguim atirou o relogio pela janela? Porque ele queria ver o tempo voar."
        ,"Alvin e os Esquilos Caneta Azul","Jair Messias BOLSONAROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"]
        a = self.a.get()
        verificacao = 0
        if  a.lower() == "ensolarado":
            self.oldmensagem["text"] = ""
            self.mensagem["text"] = "Então não saia!"
            check = 0
        else:
            if a.lower() == "chuvoso" or a.lower() == "umido":
                self.oldmensagem["text"] = ""
                self.mensagem["text"] = "Saia, mas não esqueça do Guarda-Chuva!!"
                check = 0
            else:
                if check == 1:
                    self.oldmensagem["text"] = "Não conseguimos responder isso"   
                    check = 0 
                else:
                    if check == 2:
                        self.signo()
                        check = 0              
                    else:
                        if a.__contains__("?") == False:
                            self.mensagem["text"] = ""
                            self.oldmensagem["text"] = "Favor inserir uma pergunta!!"
                        perguntaConvertida = [g.lower() for g in listaPerguntas] 
                        for x in perguntaConvertida:
                            while a.lower()==x:
                                for i in listaRespostas:
                                    if perguntaConvertida.index(x) == listaRespostas.index(i):
                                        verificacao = 1
                                        b = listaRespostas.index(i)
                                        b1 = perguntaConvertida.index(x)
                                        if b1 == 0:
                                            self.oldmensagem["text"] = listaRespostas[b]
                                            self.mensagem["text"] = ""
                                            break
                                        else:
                                            if b1 == 1:
                                                self.oldmensagem["text"] = listaRespostas[b]
                                                self.mensagem["text"] = ""
                                                check = 2
                                            else:
                                                self.mensagem["text"] = "Resposta: " + listaRespostas[b]
                                                self.oldmensagem["text"] = "Pergunta: " + a
                                                break
                                break 
                        if verificacao == 0:
                            self.oldmensagem["text"] = "A pergunta não pode ser respondida!! Favor verificar a ortografia ou a estrutura da pergunta."
                            self.mensagem["text"] = "Se ainda não funcionou, a pergunta pode não estar no nosso banco de dados."

root = Tk()
Application(root)
root.mainloop()
import lightbulb
import random
import requests
import string

bot = lightbulb.BotApp(token=open("tokens/token_ds.txt", "r").read(),
                       default_enabled_guilds=(int(open("tokens/ds_channel_id.txt", "r").read())))


@bot.command
@lightbulb.command("msg_roboo", "Saudações JFNA, Witec e Roboo!")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("*Olá, JFNA, Witec e Roboo!*")


# Piada

p1 = "Por que os químicos são ótimos em resolver problemas?\nR.: Porque eles têm todas as soluções!"
p2 = "Por que o desenvolvedor faliu?\nR.: Porque ele usou todo o seu cache."
p3 = "Você já ouviu falar do cara que roubou o calendário?\nR.: Ele pegou 12 meses!"
p4 = "O que ganha o melhor dentista do mundo?\nR.: Uma pequena placa."
p5 = "Meus professores me disseram que eu nunca seria muito porque procrastino muito.\n" \
     " Eu disse a eles: “Esperem para ver!”"
p6 = "Minha memória ficou tão ruim que realmente me fez perder o emprego. Ainda estou empregado.\n" \
     " Só não consigo lembrar onde..."
p7 = "Quando em uma candidatura a emprego perguntam quem deve ser notificado em caso de emergência, sempre escrevo:\n" \
     " “Um médico muito bom”."
p8 = "Por que o médico está sempre calmo?\nR.: Porque ele tem muitos pacientes."
p9 = "Por que o livro de matemática parece tão triste?\nR.: Por causa de todos os seus problemas."
p10 = "Qual é a comida favorita de um lobisomem?\nR.: Lobisomens não são reais."
p11 = "Como chamar um cão mágico?\nR.: Um Labracadabrador."
p12 = "Por que os pássaros voam para climas mais quentes no inverno?\nR.: É muito mais fácil do que caminhar!"
p13 = "Seja como um próton. Sempre seja positivo."
p14 = "Que tipo de carro o Yoda dirige?\nR.: Toyoda."
p15 = "O que o zero diz a um oito?\nR.: Cinto legal."
p16 = "Quantos profissionais de marketing são necessários para arrumar uma lâmpada?\n" \
      "R.: Nenhum, eles já automatizaram o processo."
p17 = "Quer ouvir uma piada sobre o potássio?\n K."
p18 = "O que você faz quando suas piadas sobre ciência não tem graça?\nR.: Continue tentando até conseguir uma reação."
p19 = "Por que o dinossauro atravessou a rua?\nR.: Porque as galinhas ainda não existiam!"
p20 = "O que um pato subatômico diz?\nR.: Quark."
p21 = "O que o Oceano Atlântico disse ao Oceano Índico?\nR.: “Experimente e seja mais Pacífico!”"
p22 = "Um homem entra em uma biblioteca e pede ao bibliotecário livros sobre paranóia. " \
      "O bibliotecário sussurra: “Eles estão bem atrás de você!”"
p23 = "Por que os coalas não contam como ursos?\nR.: Eles não têm as coalificações certas."
p24 = "Algumas pessoas comem caracóis. Eles não devem gostar de fast food."
p25 = "Como você chama uma pilha de gatinhos?\nR.: Um meowntanha."
p26 = "O que fica mais úmido quanto mais seca?\nR.: Uma toalha."
p27 = "Eu tenho uma piada sobre viagem no tempo, mas não vou contar. Vocês não gostaram."
p28 = "Alguém conhece uma boa piada sobre o sódio?\nR.: Na…"
p29 = "Como você chama o monstro mais inteligente de todos?\nR.: FrankEinstein"
p30 = "Você ouviu sobre todos os significados ocultos do Rei Leão? Sim, está cheio de simbalismo."
p31 = "Qual é a fruta que anda de trem?\nR.: O kiwiiiiiiii!"
p32 = "Por que enviar SPAM é algo justificável?\nR.: Porque os fins justificam os emails!"
p33 = "Que tipo de computador está bombando nas redes sociais?\nR.: O deskTOP⇧"
p34 = "Qual o endereço do site do cavalo?\nR.: www.cavalo pontocom pontocom pontocom."
p35 = "Por que o mouse é muito mimado?\nR.: Porque tudo o que ele quer, o mouse pad."
p36 = "Qual doença se pode pegar ao usar notebook?\nR.: A LAPTOPspirose."
p37 = "O que uma impressora falou para a outra?\nR.: Essa folha aí no chão é sua, ou é impressão minha?"
p38 = "O que o Schwarzenegger disse quando instalaram o Windows XP pra ele?\nR.: Instala o Vista, baby."
p39 = "O que é um terapeuta?\nR.: 1024 gigapeutas."
p40 = "Para qual santo você reza quando esquece a senha?\nR.: São Login."
p41 = "E quando precisa comprar um novo computador?\nR.: Santa Ifigênia."
p42 = "O dono do site esqueceu a própria senha, qual o nome do filme?\nR.: Esqueceram Admin."
p43 = "Quando você percebe que seu computador está velho?\nR.: Quando a placa-mãe já virou avó."
p44 = "Por que antigamente a Internet não subia de elevador?\nR.: Porque era Internet de-escada"
p45 = "Como se manda um 'Salve' pra galera do computador?\nR.: CTRL+S"
p46 = "Como o Pai de Santo acessa a Internet?\nR.: Com Umbanda larga."
p47 = "Qual a diferença entre Hardware e Software?\nR.: O Hardware você chuta, o Software você xinga"
p48 = "Na frase 'Fulano foi mal em todas as provas', onde está o sujeito?\nR.: Na internet."
p49 = "Por que hoje em dia não se encontra mais CD virgem?\nR.: Todos viraram CD de Programa"
p50 = "Qual é a gata que entra e já sai do chat?\nR.: A Hello, Quit"
p51 = "Por que os sites de emprego não informam nada?\nR.: Porque lá as informações são vagas."
p52 = "Quantos programadores são necessários para trocar uma lâmpada?\nR.: Nenhum, isso é problema de Hardware."
p53 = "Qual linguagem de programação o Han Solo detesta?\nR.: JabbaScript"
p54 = "int x=10; int y=10; return x+y; // Qual o nome do filme?\n R.: O Código dá Vinte."
p55 = "Qual a música preferida do Sérgio Reis?\nR.: Toda vez que eu via Java pela estrada de Ouro Fino..." \
      "(Essa só por Deus...)"
p56 = "E como ele testa a rede?\nR.: Ping ni mim, Ping ni mim...(kkkkkkk)"
p57 = "Que música Raul Seixas cantava quando pediam para ele programar em Java?\nR.: Eu prefiro C...(Jamais!)"
p58 = "Qual cidade brasileira não tem táxi?\nR.: Uberlândia."
p59 = "Por que o pão não entende a batata?\nR.: Porque o pão é francês e a batata inglesa."
p60 = "Por que os elétrons nunca são convidados para festas?\nR.: Porque eles são muito negativos."

piadas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20,
          p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40,
          p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60]


@bot.command
@lightbulb.command('piada', 'Receba uma piada!')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx):
    n = random.randint(1, 60)
    await ctx.respond(f"*{piadas[n]}*")


# Calculadora

@bot.command
@lightbulb.command('calculadora', 'Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calculator(ctx):
    pass


@calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sum(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond("*O resultado é **{}***".format(r))


@calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtração', 'Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sub(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond("*O resultado é **{}***".format(r))


@calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicação', 'Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def mult(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond("*O resultado é **{}***".format(r))


@calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisão', 'Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def div(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond("*O resultado é **{}***".format(r))


# Temperatura

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("tokens/api_weather_key.txt", "r").read()


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


@bot.command
@lightbulb.option("país", "País", type=str)
@lightbulb.option("cidade", "Cidade", type=str)
@lightbulb.command("temperatura", "Informe uma cidade e seu país para saber as condições climáticas atuais.")
@lightbulb.implements(lightbulb.SlashCommand)
async def temp(ctx):
    country = ctx.options.país
    CITY = string.capwords(ctx.options.cidade) + "," + country[0:2].lower()
    url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']

    temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))

    await ctx.respond(f"A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius} ºC\n"
                      f"Umidade do ar: {umidade}%\nVento: {vento} m/s")


bot.run()

from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Lista de objetivos a exibir nos checkboxes
OBJETIVOS_LISTA = [
    "Mais praticidade no dia a dia",
    "Segurança para minha casa",
    "Controle de energia elétrica",
    "Conforto e experiência",
    "Automatizar por curiosidade ou por gostar de tecnologia"
]


EQUIPAMENTOS_LISTA = [
    "Lâmpadas inteligentes",
    "Tomadas inteligentes",
    "Câmeras Wi-Fi",
    "Fechadura digital",
    "Ar-condicionado smart (ou com controle remoto)",
    "Robô aspirador",
    "Interruptores inteligentes",
    "Irrigador inteligente",
    "Caixa de som",
    "Chuveiro inteligente",
    "Campainha inteligente",
    "Smart Hub",
    "Abridor de garagem",
    "Lâmpada inteligente",
    "Robô doméstico",
    "Sensor de porta/janela",
    "Sensor de presença",
    "Sensor de temperatura",
    "Sensor de humidade",
    "Sensor de movimento",
    "Sensor de qualidade do ar",
    "Ventilador Smart"
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome                = request.form['nome']
        email               = request.form['email']
        alexas              = request.form.getlist('alexas')
        dispositivos        = request.form['dispositivos']
        comodos             = request.form['comodos']
        desejo_automacao    = request.form['desejo_automacao']
        pref_marca          = request.form['pref_marca'] 
        rotina              = request.form['rotina']
        imovel_tipo         = request.form['imovel_tipo']
        imovel_proprio      = request.form['imovel_proprio']
        famtec              = request.form['famtec']
        orcamento           = request.form['orcamento']
       
        # Equipamentos
        equipamentos = request.form.getlist('equipamentos')
       
        # Objetivos
        objetivos = request.form.getlist('objetivos')

        outros_objetivos = request.form.get('outros_objetivos')
       
       
        if outros_objetivos:
            objetivos.append(f"Outros: {outros_objetivos}")
        
  
        # Envia email para você
        send_email(
            nome, 
            email, 
            alexas,
            dispositivos, 
            comodos, 
            desejo_automacao,
            pref_marca,
            rotina,
            imovel_tipo,
            imovel_proprio,
            famtec,
            objetivos, 
            equipamentos,
            orcamento
        )

        return redirect('/obrigado')

    return render_template('index.html', objetivos=OBJETIVOS_LISTA, equipamentos=EQUIPAMENTOS_LISTA)

@app.route('/obrigado')
def obrigado():
    return "<h1>Obrigado por preencher o formulário!</h1></br><h3>Já pode fechar esta página.</h3>"

def send_email(nome,email,alexas,dispositivos,comodos,desejo_automacao,pref_marca,rotina,imovel_tipo,imovel_proprio,famtec,objetivos,equipamentos,orcamento):
    msg = EmailMessage()
    msg['Subject'] = 'Diagnóstico Cliente'
    msg['From'] = 'arthurjacomite1@gmail.com'
    msg['To'] = 'arthurjacomite1@gmail.com'

    body = f"""
    Novo formulário preenchido:

    Nome:                           {nome}
    E-mail:                         {email}
    Alexas:                         {', '.join(alexas)}
    Qtde. Dispositivos:             {dispositivos}
    Cômodos:                        {comodos}
    Equipamentos:                   {', '.join(equipamentos)}
    Desejo de Automação:            {desejo_automacao}
    Preferência de Marcas:          {pref_marca}
    Rotina:                         {rotina}
    Objetivos:                      {', '.join(objetivos)}
    Tipo de Imóvel:                 {imovel_tipo}
    Propriedade Imóvel:             {imovel_proprio}
    Familiaridade com Tecnologia:   {famtec}
    Orçamento Estimado:             {orcamento}

    """
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('arthurjacomite1@gmail.com', 'fmnp lvtg argw xpox')
        smtp.send_message(msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


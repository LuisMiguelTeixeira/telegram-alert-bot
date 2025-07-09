from dotenv import load_dotenv
import os
import requests
from keep_alive import manter_vivo

manter_vivo()  # manter o servidor vivo

load_dotenv()
TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    print(f"Resposta: {response.status_code}, {response.text}")

if __name__ == "__main__":
    enviar_alerta("?? *Alerta de Teste Tex*\nServidor no Render está online e pronto para sinais!")

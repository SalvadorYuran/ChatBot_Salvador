from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS
import traceback # para imprimir erros no terminal (DEBUG sem saber o que esta errado? Vibe coding dele tbm n é assim jovem!!!)

# Apenas a chave em si, não o endpoint inteiro
GOOGLE_API_KEY = "AIzaSyDFBEcvAmLCXfC9lICDCkD2FVzICVu0npw"
genai.configure(api_key=GOOGLE_API_KEY)

# Use o modelo que está disponível na sua conta (ex: gemini-pro)
# Já agora, o jovem tem certeza de que esse modelo está disponivel na tua conta?
model = genai.GenerativeModel('gemini-pro')

# Informações da sua bio
bio = """
Eu me chamo Salvador Yuran Mário, 21 anos, nascido no dia 10
de Abril de 2004, estatura alta, magro de pele escura e olhos escuros.
Natural de Moçambique, Provincia de Sofala, Cidade da Beira,
actualmente sou estudante da Universidade Catolica de Mocambique, FEG, no curso
de Tecnologias de Informacao. Gosto de ver filmes em sua grande maioria de acção,
vejo séries e animes, mas meu hobby principal são realmente os videojogos,
gosto de sair para falar com meus amigos também nos tempos vagos, não sou muito
proeficiente nos esportes mas meus esportes favoritos são o futebol, basquetebol
e corridas da F1.
Meus top 3 filmes favoritos são o Batman Cavaleiro das Trevas,
Fight Club e HARD TARGET, músicas eu não tenho uma favorita em especifico mas
sim um género que é o Phonk, não sou muito chegado a livros então não tenho
favoritos, mas gosto bastante de Light novels, da pra assemelhar a um livro,
lugares que já visitei são Inhambane, Maputo, Gorongoza, distrito do Buzi, mas
nada supera a praia de Tofo.
Comidas favoritas tenho como Pizza, Shawarmas e Burguers
Sonhos? Viajar mundo fora,   tem alguns países que eu gostaria de visitar,
honrar o investimento que meus pais depositaram em mim e ter uma vida estável,
na qual estaria bem acompanhado.
Tenho alguns objectivos como começar meu próprio negócio,
terminar a faculdade e entrar no ramo de trabalho.
"""

app = Flask(__name__)
CORS(app) # Para permitir requisições de diferentes origens (seu HTML)

@app.route('/pergunta', methods=['POST'])
def fazer_pergunta():
    data = request.get_json()
    pergunta = data.get('pergunta')
    if not pergunta:
        return jsonify({'erro': 'Nenhuma pergunta fornecida'}), 400

    prompt = f"Com base nas seguintes informações sobre Salvador: '{bio}', responda à seguinte pergunta: '{pergunta}'"
    try:
        response = model.generate_content([prompt])  # Colocar o prompt como lista de mensagens
        resposta_texto = response.text
        return jsonify({'resposta': resposta_texto})
    except Exception as e:
        print(traceback.format_exc())  # Mostra erro completo no terminal
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

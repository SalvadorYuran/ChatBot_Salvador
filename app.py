from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

# Sua chave de API do Gemini
GOOGLE_API_KEY = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)
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
        response = model.generate_content(prompt)
        resposta_texto = response.text
        return jsonify({'resposta': resposta_texto})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
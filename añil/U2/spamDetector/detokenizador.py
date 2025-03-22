import json,unicodedata

punctuation = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
    ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"
    ]
articulos = {"el", "la", "los", "las", "un", "una", "unos", "unas"}
preposiciones = {
    "a", "ante", "bajo", "con", "contra", "de", "desde", "en", "entre", 
    "hacia", "hasta", "para", "por", "según", "sin", "sobre", "tras"
}
conjunciones = {"y", "e", "o", "u", "pero", "sino", "aunque", "porque", "si"}

filtered_words = articulos | preposiciones | conjunciones


def clean_text(texto):
    #quita acentos
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    #quita signos de puntuación
    texto = texto.translate(str.maketrans('', '', "".join(punctuation)))
    return texto.lower().strip()

def filter_mail(text):
    return " ".join([word for word in text.split(" ") if word not in filtered_words])

def tokenizador(tokens, correos, categorias):
    n_coreos = len(correos)
    tokens_probabilidad = {}
    for token in tokens:
        ntotal = 0
        nSpam = 0
        for i in range(n_coreos):
            correo_x = correos[i]
            if token in correo_x:
                ntotal += 1
                if categorias[i]:
                    nSpam += 1
        if ntotal > 0:
            tokens_probabilidad[token] = nSpam / ntotal
        else:
            tokens_probabilidad[token] = 0  
    return tokens_probabilidad

if __name__ == "__main__":
    with open("clasified_messages.json", 'r', encoding="utf-8") as file:

        correos = []
        correos_limpios = []
        correos_detokenizados = []
        tokens = []

        data = json.load(file)
        correos = data["messages"]
        # print(correos)
        # print()

        correos_limpios = [[clean_text(correo["correo"])] for correo in correos]
        correos_dtoken = [[filter_mail(correo[0])] for correo in correos_limpios]
        # print(correos_detokenizados)

        # correos_detokenizados = map(lambda x: list(set(x[0].split(" "))), correos_dtoken)
        correos_detokenizados = list(map(lambda x: x[0].split(" "), correos_dtoken))
        # print(list(correos_detokenizados))

        all_tokens = set()
        for correo in correos_detokenizados: 
            all_tokens = all_tokens | set(correo)
        print(all_tokens)


        categorias = [1 if correo["categoria"] == "spam" else 0 for correo in correos]
        # print(categorias)

        tokens_probabilidad = tokenizador(all_tokens,correos_detokenizados,categorias)
        print(tokens_probabilidad)

        with open("tokens_probabilidad.json", 'w', encoding="utf-8") as file:
            json.dump(tokens_probabilidad, file, ensure_ascii=False, indent=4)
        







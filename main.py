from flask import Flask, request, jsonify


#i 4 metodi più comuni per inviare richieste ai server e sono: Get, Post, Put e Delete
#Get: quando voglio recueperare dati 
#Post: quando voglio creare qualcosa di nuovo
#Put: modificare i dati
#Delete: cancellare i dati


app = Flask(__name__)

#@app("/") gli sto dando come route quella di default

@app.route("/get/user/<user_id>")
#dopo /user gli sto passando qualche parametro nello specifico, che è lo stesso parametro che io ho in get_user
#nello specifico ciò che viene dopo get-user/9014 è il numero di id dello user che ad esempio voglio recuperare

#per ritornare su schermo dei valori, bisogna fare un return jsonify. 200 è lo stato del server che vuol dire "ok"
#quindi brevemente.. ci sarà l'url composto dall'address + /get/user/numid . In questo modo restituirà i valori di get_user che sono nome e cognome
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "nome": "billy",
        "cognome": "chocolate"
    }
    if get_user:
        return jsonify (user_data),200

@app.route("/create-user", methods=["POST"])
def create_user():
    #if request.method == "POST"
    data = request.get_json()
    return jsonify(data),201

#per testare il post basta andare su postman, creare una nuova sessione (il +), mettere l'address+la route e impostare il metodo POST
#http://127.0.0.1:5000/create-user
#dopodiché body, raw, JSON e all'interno delle graffe mettere un nuovo valore
#{"nome": "dario"}
#come risposta che si visualizza di sotto, si vedrà ciò che si è appena passato. Se non funziona allora c'è qualche errore

if __name__ == "__main__":
    app.run(debug=True)
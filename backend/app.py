## Importation des modules Flask pour créer le serveur web, afficher des pages HTML, lire les données envoyées, et renvoyer du JSON.
from flask import Flask,render_template,request,jsonify

# Importation pour se connecter à MongoDB.
from pymongo import MongoClient

# Pour manipuler l’ID spécial MongoDB (pas utilisé dans ce code, mais utile pour récupérer ou modifier un document par ID).
from bson.objectid import ObjectId

# Pour autoriser les requêtes venant d’autres domaines (ex: React frontend).
from flask_cors import CORS

# Création de l’application Flask.
app = Flask(__name__)

# Connexion à la base MongoDB locale.
client = MongoClient('mongodb://localhost:27017')

 # Choix de la base de données nommée 'flaskreactfullstack'.
db = client['flaskreactfullstack']

# Active CORS sur toute l’application pour accepter les requêtes cross-origin.(CORS assure l'echange entre frontend et le backend)
CORS(app)

# Récupère les données envoyées au format JSON.
#Route racine '/' qui renvoie la page index.html (dans dossier templates)
@app.route('/')
def index():
    return render_template( 'index.html')

# Récupère les données envoyées au format JSON.
@app.route('/users' ,methods=['POST' , 'GET'])
def data():

    if request.method == 'POST' :
        body= request.json # Tu récupères les données envoyées en JSON depuis le frontend

# Extrait les champs du JSON.

        firstName = body['firstName']
        lastName = body['lastName']
        emailId = body['emailId']

# Insère un nouveau document dans la collection 'users' de MongoDB.

        db['users'].insert_one({
            "firstName":firstName,
            "lastName" :lastName,
            "emailId" :emailId
        })

# Renvoie une confirmation avec les données reçues.

        return jsonify({      #jsonify(...) : transforme un dictionnaire Python en réponse JSON qu’on peut renvoyer au frontend
            'status':'Data is posted to Mongodb',
            'firstName':firstName,
            'lastName' :lastName,
            'emailId' :emailId
        })
    #show all the users
    if request.method == 'GET' :
        allData = db['users'].find()
        dataJson = []
        for data in allData:
            id = data['id']
            firstName = data['firstName']
            lastName = data['lastName']
            emailId = data['emailId']

            dataDict = {
                "id":str(id),
                "firsName":firstName,
                "emailId":emailId,
            }
              
              
# Lance le serveur Flask en mode debug (redémarrage automatique si tu modifies le code).
if __name__=='__main__':
    app.debug = True
    app.run()
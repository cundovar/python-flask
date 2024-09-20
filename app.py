from flask import Flask, render_template, request
from function import check_number, devineNombre,calculer_moyenne
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result_check = ""
    result_voyelle = ""
    result_calc = "" 
    
    if request.method == 'POST':
        # Détecte quel formulaire a été soumis
        form_type = request.form.get('form_type')
        
        if form_type == 'check_number':
            try:
                N = int(request.form.get('number'))
                result_check = check_number(N)
            except ValueError:
                result_check = "Veuillez entrer un nombre valide."
        
        if form_type == 'count_vowels':
            chaine = request.form.get('chaine', "")
            result_voyelle = devineNombre(chaine)
        

        if form_type == 'calculator':
             notes_str = request.form.get('calc')
             try:
                # Convertir la chaîne en une liste de float
                notes = [float(note) for note in notes_str.split(',')]
                result_calc = calculer_moyenne(notes)
             except ValueError:
                result_calc = "Veuillez entrer des notes valides, séparées par des virgules."
    
    return render_template("base.html", result_check=result_check, result_voyelle=result_voyelle, result_calc=result_calc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
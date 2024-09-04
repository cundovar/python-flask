
def check_number(N):
    if 1 <= N <= 3:
        return "Correct"
    else:
        return "Saisie erronée. Le nombre doit être entre 1 et 3."
    
def devineNombre(chaine):
    voyelles = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    compteur_voyelles = sum(1 for char in chaine if char in voyelles)
    return f"Le nombre total de voyelles est : {compteur_voyelles}"

def calculer_moyenne(notes):
    if len(notes)==0 :
        return 0
    #calcule moyenne : somme des notes et longueur de notes
    return sum(notes)/len(notes)



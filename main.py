import re

def demander_nombre():
    while True:
        entree_utilisateur = input("Entrez un nombre : ")
        if re.match(r'^-?\d+(\.\d+)?$', entree_utilisateur):
            return float(entree_utilisateur)
        else:
            print("Veuillez entrer un nombre valide")

def demander_operateur():
    operateurs_valides = ['+', '-', '*', '/']
    while True:
        operateur = input("Entrez un opérateur (+, -, *, /) : ")
        if operateur in operateurs_valides:
            return operateur
        else:
            print("Opérateur invalide. Veuillez choisir parmi '+', '-', '*', '/'")

def evaluer_expression(nombre1, operateur, nombre2):
    if operateur == '+':
        return nombre1 + nombre2
    elif operateur == '-':
        return nombre1 - nombre2
    elif operateur == '*':
        return nombre1 * nombre2
    elif operateur == '/':
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            print("La division par zéro n'est pas définie en mathématique")
            return None

def calculatrice():
    while True:
        nombre1 = demander_nombre()
        operateur = demander_operateur()
        nombre2 = demander_nombre()

        resultat = evaluer_expression(nombre1, operateur, nombre2)

        if resultat is not None:
            print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

        continuer = input("Voulez-vous effectuer une autre opération ? (oui/non) : ").lower()
        if continuer != 'oui':
            break

if __name__ == "__main__":
    calculatrice()

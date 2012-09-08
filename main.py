#coder par GHOSTnew
print("1-homme")
print("2-femme")
choix = input("votre choix : ")
if choix == 1:
    print("homme")
    taille = input("saisisser la taille (en cm) : ")
    resultat = taille - 100 - (taille - 150)/4 
    print("le poid ideal est de:",resultat,"kg")
elif choix == 2:
    print("femme")
    taille = input("saisisser la taille (en cm) : ")
    resultat = taille - 100 - (taille - 150)/2.5 
    print("le poid ideal est de:", resultat, "kg")
else:
    print("ERREUR 404 Not Found")
#Team Mondial Production
#http://team-mondial.fr.nf/

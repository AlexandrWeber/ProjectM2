import csv
"""
Ce programme transforme le fichier csv en xml
fichier input=API_MS.MIL.XPND.CD_DS2_en_csv_v2_317481.csv
fichier output=military4.xml (le tableau commence à partir de la ligne 5)
"""

line_count=0

# ouvre le fichier output et écrit l'entête et le début du root
with open ('military.xml', 'w') as res:
	res.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>\n\n\n')
	res.write('<data>\n\n')
	

#ouvre le fichier input, lit les lignes 
with open('API_MS.MIL.XPND.CD_DS2_en_csv_v2_317481.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	
	for row in csv_reader:
		line_count=line_count+1
		
# la ligne 5 sera le nom des les balises, le programme prend la ligne 5 et la concerve dans une variable listee qui est une list	
		if line_count==5:
			listee=row[:-1] # on enlève la dernière valeur qui est vide
			for i in listee:  # on corrige les espaces dans les noms car les balises xml ne peuvent pas contenir d'espaces. s'il y a une espace on la remplace avec _ et join
				if listee.index(i)==0 or listee.index(i)==1: # pour les deux premiers: Country name, Country code
					ll=list(i)
				for e in ll:
					if e==' ':
						ll[ll.index(e)]='_'
						listee[listee.index(i)]="".join(ll)		
	
# à partir de la 5 ligne on fait la même procédure pour tous les données
# à partir de la ligne 5 on prend l'élément de la ligne 5 et son équivalent en ligne d'après et on les met dans les balises (listee) ou comme texte	entre les balises(les autres lignes)									
		if line_count>5:  # on cherche les occurences de & et les remplace avec "and"
			roww=row
			row0=list(roww[0])
			print(row0)
			for e in row0:
				if e=='&':
					row0[row0.index(e)]="and"
					roww[0]="".join(row0)
		
			with open ('military.xml', 'a') as res: # on ouvre le fichier et pour chaque element de la liste balises et la liste de la ligne courante on rajoute les balises xml et l'info
				res.write("\t<country>\n")
				for i,e in zip(listee, roww):
					if listee.index(i)==0 or listee.index(i)==1:
						print("<{}>{}</{}>".format(i,e,i))
						res.write("\t\t<{}>{}</{}>\n".format(i,e,i))
						

#					if listee.index(i)==2 or listee.index(i)==3: # ces deux éléments , on en a pas besoin
#						continue
					
					if listee.index(i)>3:   # à partir d'index 3 commencent les dates et les chiffres. on les met entre les balises annee et number comme enfants de donnees
						if e=='':
							nr="non renseigné" # on remplace les vides avec non renseigné
							res.write("\t\t<donnees>\n")
							res.write("\t\t\t<annee>{}</annee>\n".format(i))
							res.write("\t\t\t<number>{}</number>\n".format(nr))
							res.write("\t\t</donnees>\n")
						else:
							res.write("\t\t<donnees>\n")
							res.write("\t\t\t<annee>{}</annee>\n".format(i))
							res.write("\t\t\t<number>{}</number>\n".format(e))
							res.write("\t\t</donnees>\n")
					
				res.write("\t</country>\n\n")

# on écrit la balise root fermante				
with open ('military.xml', 'a') as res:
	res.write('</data>')

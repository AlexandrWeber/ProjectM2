import csv
"""
Ce programme transforme le fichier csv en xml
fichier input=API_MS.MIL.XPND.CD_DS2_en_csv_v2_317481.csv
fichier output=military4.xml (le tableau commence à partir de la ligne 5)
"""
economy=["High income", "Low and middle income", "Low income", "Lower middle income", "Middle income", "Upper middle income", "Heavily indebted poor countries (HIPC)", "OECD members"] 
region=["World", "Arab World", "Caribbean small states", "Central Europe and the Baltics", "East Asia and Pacific", "Euro area", "Europe and Central Asia", "European Union", "Latin America and Caribbean", "Middle East and North Africa", "North America", "East Asia and Pacific (excluding high income)", "Europe and Central Asia (excluding high income)", "Latin America and Caribbean (excluding high income)", "Sub-Saharan Africa (excluding high income)", "Sub-Saharan Africa", "Latin America and the Caribbean (IDA and IBRD countries)", "Middle East and North Africa (IDA and IBRD countries)", "South Asia (IDA and IBRD)", "Sub-Saharan Africa (IDA and IBRD countries)", "Middle East and North Africa (excluding high income)", "Pacific island small states", "South Asia", "East Asia and Pacific (IDA and IBRD countries)", "Europe and Central Asia (IDA and IBRD countries)"]
other=["Early-demographic dividend", "Fragile and conflict affected situations", "IBRD only", "IDA and IBRD total", "IDA total", "IDA blend", "IDA only", "Not classified", "Late-demographic dividend", "Pre-demographic dividend", "Post-demographic dividend"]


line_count=0

# ouvre le fichier output et écrit l'entête et le début du root
with open ('military_new.xml', 'w') as res:
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
			listee[0]="entity_name"
			listee[1]="entity_code"
			print(listee)
		
	
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
		
			with open ('military_new.xml', 'a') as res: # on ouvre le fichier et pour chaque element de la liste balises et la liste de la ligne courante on rajoute les balises xml et l'info
				res.write("\t<entity>\n")
				for i,e in zip(listee, roww):
					if listee.index(i)==0 or listee.index(i)==1:
#						print("<{}>{}</{}>".format(i,e,i))
						res.write("\t\t<{}>{}</{}>\n".format(i,e,i))
					

					if listee.index(i)==2: # ces deux éléments , on en a pas besoin
						if roww[0] in economy:
							res.write("\t\t<{}>{}</{}>\n".format("type","economy","type"))
						elif roww[0] in region:
							res.write("\t\t<{}>{}</{}>\n".format("type","region","type"))
						elif roww[0] in other:
							res.write("\t\t<{}>{}</{}>\n".format("type","other","type"))
						else:
							res.write("\t\t<{}>{}</{}>\n".format("type","country","type"))
#						print("<{}>{}</{}>\n".format("type","country","type"))

					
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
					
				res.write("\t</entity>\n\n")

# on écrit la balise root fermante				
with open ('military_new.xml', 'a') as res:
	res.write('</data>')



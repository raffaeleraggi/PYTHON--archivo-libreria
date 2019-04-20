archivio= {}
condizione = True

print('''\tMENU
Comando 0 = Esci
Comando 1 = Visualizza Menu
Comando 2 = Aggiungi Autore
Comando 3 = Aggiungi Libro
Comando 4 = Visualizza archivio
Comando 5 = Visualizza autori
''')

while condizione == True:


    com = input('Scegli comando:\n')

    if com == "esci":
        condizione == False
        print('ARCHIVIO CHIUSO')
        break


    if int(com) == 1:
        print('''\tMENU
        Comando 0 = Esci
        Comando 1 = Visualizza Menu
        Comando 2 = Aggiungi Autore
        Comando 3 = Aggiungi Libro
        Comando 4 = Visualizza archivio
        Comando 5 = Visualizza autori
     ''')

    elif int(com) == 2:#add autore
         autore = input('Aggiungi un nuovo autore  :\n')
         archivio[autore]=[]

    elif int(com) == 3:#add libro

        lista_autori = []
        i = 0
        for el in archivio.keys():
            print('AUTORE: '+ str(el)+" ID: "+str(i))
            lista_autori.append(el)
            i += 1

        id_autore = input("Scrivi l'ID dell'autore: \n")
        autore = lista_autori[int(id_autore)]

        libro = input('Scrivi il titolo del libro: \n')
        archivio[autore].append(libro)

    elif int(com) == 4:#stampa archivio
        print('\n Il nostro archivio è: \n')
        for k,v in archivio.items():
            print('AUTORI: '+str(k))
            print('\tLIBRI: ')
            for el in v:
                print('\t\t'+str(el))

    elif int(com) == 5: # stampa autori
        print('Elenco autori')
        for el in archivio.keys():
            print('\t'+ str(el))

import csv 

num = 0


try:
    exemplo_arquivo = open('Projeto_4_Missao_SINARM\OCORRENCIAS_2025.csv')
    exemplo_leitor = csv.reader(exemplo_arquivo,
                                delimiter=';',
                                dialect='excel')

        
    for arma in exemplo_arquivo:
        if "Espingarda" in arma:
            num += 1

            

        else:
            ("não encontrado nessa linha")
        
    
    exemplo_arquivo.close()

    print("o arquivo contém ", num, "registros de espingardas")

except FileNotFoundError:
    print('Arquivo não encontrado')
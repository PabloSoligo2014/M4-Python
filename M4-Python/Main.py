#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''


if __name__ == '__main__':
    
    #->Asignacion con = 
    midpoint = 5
    
    #->Instancio dos listas vacias ==> lower = list()
    #->Con ; salto la necesidad de nueva linea para terminar sentencia (No recomendado)
    lower = []; upper = [];
    
    #->separo los numeros en "altos" y "bajos"
    #->Iteracion definida, observar que la tabulacion define el bloque!!
    for i in range(10):
        #->Condicional
        if (i<midpoint):
            #->Agrego a la lista
            lower.append(i)
        else:
            #->Agrego a la lista
            upper.append(i)
            
    print("Lower:", lower)
    print("Upper:", upper)
    
    
    #->Iteraciones sobre listas, se crea la lista utilizando nombre clase
    word_list = list()
    
    word_list.extend(["Hola", "Mundo", "!"])
    
    for word in word_list:
        print(word)
        
    
    
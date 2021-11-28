
# Problem

#* A Shashank le gustan las cadenas donde los caracteres consecutivos son diferentes. Por ejemplo, le gusta ABABA, mientras que ABAA no le gusta. Dada una cadena que solamente contiene caracteres A y B, él quiere cambiarla a una cadena que le guste. Para hacerlo, solo se le permite borrar los caracteres en la cadena.
# Tu tarea es encontrar la mínima cantidad requerida de borrados.
# Formato de Entrada La primera linea contiene un enter T que quiere decir el número de casos de prueba. Luego siguen T lineas, con una cadena en cada linea.
# Formato de Salida Imprimie la mínima cantidad requerida de pasos en cada caso de prueba.#

def minimumDeletions(s):
    deletions = 0
    
    spotIndex = 0
    while (spotIndex < (len(s) - 1)):
        for i in range(spotIndex + 1, len(s)):
            if s[i] != s[spotIndex]:
                spotIndex = i
                break
            else:
                deletions += 1
                if i == (len(s) - 1):
                    spotIndex = len(s)
    return deletions
    
    
    # Example: string1 = 'ABAABBB'; string2 = 'ABABAB'. 
    # spotIndex at position 0 so 'A'; len(string1) = 7
    # i will look in 'BAABBB'
    # 'B' is different from 'A' so spotIndex will be 1. And we start again.
    # 1 < 7, so for loop, s[2] != s[1], so spotIndex = 2, and we start again.
    # 2 < 7, so for loop, s[3] == s[2], so we need to add 1 to deletion and look if next letter is also A
    # at this point deletions is 1, i = 4, spotIndex = 2.
    # 2 < 7, so for loop, s[4] != s[2], so spotIndex = 4, and we start again.
    # 4 < 7, so for loop, s[5] == s[4], so deletions = 2, and we look for next letter
    # 4 < 7, so for loop, s[6] == s[4], so deletions = 3, and we need to stop now i = 6 == len(s), so spotIndex = 7
    # 7 = 7, so we finish.
    # Rest to now how to stop.
    # 
    # 
    # Now, with stop implemented
    # spotIndex at position 0 so 'A'; len(string2) = 6
    # i will start looking to 'BABAB'
    # 0 < 6, so for loop, s[1] != s[0], so spotIndex = 1, and we start again.
    # 1 < 6, so for loop, s[2] != s[1], so spotIndex = 2, and we start again.
    # 2 < 6, so for loop, s[3] != s[2], so spotIndex = 3, and we start again.
    # 3 < 6, so for loop, s[4] != s[2], so spotIndex = 4, and we start again.
    # 4 < 6, so for loop, s[5] != s[6], so spotIndex = 5, and we start again.
    # 5 < 6, so for loop, s[6] != s[5], so spotIndex = 6, and we start again.
    # 6 = 6, so we finish!!!#
    
    
def main():
    string1 = "ABABAB"
    deletions = minimumDeletions(string1)
    
    print(deletions)
    
main()
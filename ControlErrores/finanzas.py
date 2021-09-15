import numpy as np
import pandas as pd
import statistics


class Error(Exception):
    pass

class NoAnyoCompleto(Error):
    pass

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))


while(True):
    try:

        csv = pd.read_csv('finanzas2020.csv',sep='\t',header=0, decimal=',')

        if(csv.shape[1]!=12):
            raise NoAnyoCompleto
        else:
            suma = []
                                               
            for i in range(csv.shape[0]):
                for j in range(csv.shape[1]):
                    if (type(csv.iloc[i,j])==str):
                        n = only_numerics(csv.iloc[i,j])
                        if (n==''): 
                            n=0
                        csv.iloc[i,j]=int(n)

            for col in csv:
                n=csv[col].sum()
                suma.append(n)
            
            print(suma)
            
            maximo= max(suma)
            minimo= min(suma)
            media= statistics.mean(suma)
            total= sum(suma)

            print("El maximo ahorrado en un mes es\n", maximo ,"\n")
            print("El maximo gastado en un mes es\n", minimo ,"\n")
            print("La media de gasto es\n", media ,"\n")
            print("El total gastado es\n", total ,"\n")

            break

    except IOError:
        print("El archivo indicado no existe\n")
        break
    except NoAnyoCompleto:
        print("El archivo no corresponde a los datos de un año completo\n")
        break

    
import psycopg2 as pg
import pandas as pd

class Posta:
    def __init__(self):
        self.upit=""
        self.posiljke=None

    def kreiraj_upit(self,upit):
        self.upit=upit
    
    def get_sql(self):
        con=pg.connect(
                database='POSTA',
                user='postgres',
                port='5432',
                host='localhost',
                password='itoip'
        )
        self.posiljke=pd.read_sql('SELECT * FROM POSILJKE',con)
        con.close()
        return 'Dataframe created'
        
    def export_excel(self):
        if self.posiljke.size!=0:
            self.posiljke.to_excel('Posiljke.xlsx',index=False)
            return 'Excel exported'
        else:
            return 'An error ocurred'
    def export_csv(self):
        if self.posiljke.size!=0:
            self.posiljke.to_csv('Posiljke.csv',index=False)
            return 'CSV exported'
        else:
            return 'An error ocurred'
        
    
    def dodaj_posiljku(self,posiljalac,primalac,status='poslato'):
        try:
            con=pg.connect(
                database='POSTA',
                user='postgres',
                host='localhost',
                port='5432',
                password='itoip'
            )
            cursor=con.cursor()
            com='''INSERT INTO POSILJKE (POSILJALAC,PRIMALAC,STATUS)VALUES ('{}','{}','{}');'''.format(posiljalac,primalac,status)
            cursor.execute(com)
            con.commit()
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
            cursor.close()
P=Posta()
P.get_sql()


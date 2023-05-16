import psycopg2 as pg
import openpyxl as op
import pandas as pd

class Posiljke:
    def __init__(self):
        pass
    def dodaj_posiljku(self,posiljalac,primalac):
        try:
            con=pg.connect(
                database='POSTA',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('SELECT * FROM POSILJKE',con=con)
            cursor=con.cursor()
            l='''INSERT INTO POSILJKE VALUES ({},'{}','{}','poslato');'''.format(len(df)+1,posiljalac,primalac)
            cursor.execute(l)
            con.commit()
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
            cursor.close()
    def export_excel(self):
        try:
            con=pg.connect(
                database='POSTA',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('SELECT * FROM POSILJKE',con=con)
            df.to_excel('Excel.xlsx', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
    def export_csv(self):
        try:
            con=pg.connect(
                database='POSTA',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('SELECT * FROM POSILJKE',con=con)
            df.to_csv('CSV.csv', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
    def promeni_status(self,status):
        try:
            con=pg.connect(
                database='POSTA',
                user='postgres',
                port='5432',
                password='itoip',
                host='localhost'
            )
            cursor=con.cursor()

            com='''
            UPDATE POSILJKE
            SET STATUS='{}'
            '''.format(status)
            cursor.execute(com)
            print("Table updated successfully")
            con.commit()

        except (Exception,pg.Error) as e:
            print("Error:",e)

        finally:
            cursor.close()
            con.close()
    # def listbox(self):
    #     try:
    #         con=pg.connect(
    #             database='POSTA',
    #             port='5432',
    #             host='localhost',
    #             user='postgres',
    #             password='itoip'
    #         )
    #         df=pd.read_sql('SELECT * FROM POSILJKE',con=con)
    #         return df
    #     except(Exception,pg.Error) as e:
    #         print('Error: ',e)
    #     finally:
    #         con.close()

p=Posiljke()
# p.export_excel()
# p.export_csv()
# p.dodaj_posiljku('Petar Petrovic','Marko Markovic')
# print(p.listbox())
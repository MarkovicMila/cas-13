import openpyxl as op
import psycopg2 as pg
import pandas as pd


class Posiljke:
    def __init__(self):
        self.upit=''
        self.sql_result=None

    def kreiraj_upit(self,upit):
        self.upit=upit

    def get_sql(self):
        try:
            con=pg.connect(
                database='POSTA',
                user='postgres',
                host='localport',
                port='5432',
                password='itoip'
            )
            cursor=con.cursor()
            cursor.execute(self.upit)
            self.sql_result=cursor.fetchall()
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
            cursor.close()
    
    def export(self,gde):
        if gde=='excel':
            wb=op.Workbook()
            ws=wb.active()
            
            ws['A1']='posiljalac'
            ws['B1']='primalac'
            ws['C1']='status'

            for i in range(2,len(self.sql_result)+2):
                ws.cell(row=i,column=1).value=self.sql_result[i-2][0]
                ws.cell(row=i,column=2).value=self.sql_result[i-2][1]
                ws.cell(row=i,column=3).value=self.sql_result[i-2][2]

            wb.save(filename='Export excel.xlsx')
            wb.close()
            return 'Excel file created successfully!'
        elif gde=='csv':
            dt=pd.DataFrame(self.sql_result)
            dt.to_csv('Export csv',index=False)
            return 'CSV file created successfully!'
        else:
            return 'Fail! No file created!'
        
    def dodaj_posiljku(self,posiljalac,primalac,status):
        try:
            con=pg.connect(
                database='POSTA',
                user='postgres',
                host='localport',
                port='5432',
                password='itoip'
            )
            cursor=con.cursor()
            com="INSERT INTO POSILJKE VALUES ('{}','{}','{}')".format(posiljalac,primalac,status)
            cursor.execute(com)
            con.commit()
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
            cursor.close()

    def promeni_status(self):
        pass


P=Posiljke()
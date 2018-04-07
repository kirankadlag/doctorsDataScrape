
import bs4 as bs
import urllib.request
import xlwt
import pandas as pd


wb = xlwt.Workbook()
ws = wb.add_sheet("State_Doctors")
record = []

for ii in range(399,400):
    linky = 'https://www.drdata.in/list-doctors.php?search=Doctor&page='+str(ii)
    link1 = urllib.request.urlopen(linky)
    soup = bs.BeautifulSoup(link1, 'lxml')
    
    
    table = soup.table
    #print(table)
    table_row = table.find_all('a')
    for tr in table_row:
        link = tr.get('href')
        print(link)
        
        linkx = 'https://www.drdata.in/'
        link2 = linkx + str(link)
        link3 = urllib.request.urlopen(link2)
#        link5 = link2 + '#' 
        
#        print(link)
        
        if linkx == link2:
            continue
        elif link == '#':
            continue
        else:    
            
            soup3 = bs.BeautifulSoup(link3, 'lxml')
            
            table1 = soup3.find('table')
            table1_row = table1.find_all('tr') 
            for tr in table1_row:
                td = tr.find_all('td')
                row = [i.text for i in td]
        #        print(row)
        
            dfs = pd.read_html(link2)
            name = 'NA'
            spec = 'NA'
            degree = 'NA'
            practice = 'NA'
            address = 'NA'
            state = 'NA'
            district = 'NA'
            ph='NA'  
            clinic = 'NA'
            
            for df in dfs:
                
                for i in range(len(df)):
        #            print(i)
                    if df[0][i] == 'Name':
                        name = [df[1][i]] 
                    if df[0][i] == 'Specialization':   
                        spec = [df[1][i]] 
                    if df[0][i] == 'Degree':   
                        degree = [df[1][i]] 
                    if df[0][i] == 'Area of Practice':   
                        practice = [df[1][i]] 
                    if df[0][i] == 'Address':   
                        address = [df[1][i]] 
                    if df[0][i] == 'State':   
                        state = [df[1][i]] 
                    if df[0][i] == 'District':   
                        district = [df[1][i]] 
                    if df[0][i] == 'Phone Number':   
                        ph = [df[1][i]] 
                    if df[0][i] == 'Clinic/ Hospital Name':   
                        clinic = [df[1][i]] 
                        
                record.append([name, spec, degree, practice, address, state, district, ph, clinic])
    print(ii)

for i in range(len(record)):
    for j in range(9):
        ws.write(i, j, record[i][j])
 
wb.save("IndianDoctorsData_399.xls")    
      

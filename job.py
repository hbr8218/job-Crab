import requests
from bs4 import BeautifulSoup
import csv
import os
from tqdm import tqdm


####################### user input section ###########################
w = str(input("enter skill: "))
l = str(input("enter location for job: "))

url_base = os.environ.get('BASE_URI')
uri_init = url_base+'?q='+w+'&l='+l

file_name = w+l+'.csv'
file = open(file_name,'w')
writer = csv.writer(file)
file = writer.writerow(["Job title","Company name","Job Location","Wage","Ratings"])

####### Extrating from First Page ##################

uri = uri_init
source = requests.get(uri).text
soup = BeautifulSoup(source,'html.parser')
for job in soup.findAll('div',class_='sjcl'):
    emp_list = []
    job_data = job.parent
    try:
        job_title = job_data.find('div',class_="title").text
        emp_list.append(str(job_title))
    except:
        emp_list.append(None)
        
    try:
        com_name = job_data.find('div',class_='sjcl').find('span',class_="company").text
        emp_list.append(str(com_name))
    except:
        emp_list.append(None)

    try:
        job_loc = job_data.find('div',class_="location accessible-contrast-color-location").text
        emp_list.append(str(job_loc))
    except:
        emp_list.append(None)

    try:
        sal = job_data.find('div',class_="salarySnippet salarySnippetDemphasizeholisticSalary").find('span',class_="salaryText").text
        emp_list.append(str(sal))
    except:
        emp_list.append(None)

    try:
        rate = job_data.find('div',class_='sjcl').find('span',class_="ratingsDisplay").a.text
        emp_list.append(str(rate))
    except:
        emp_list.append(None)

    writer.writerow(emp_list)
    

##################### Extracting from other pages #############
page_count = 1
for page_no in tqdm(range(10,600,10)):
    try:
        uri = uri_init+'&start={}'.format(page_no)
        source = requests.get(uri).text
        soup = BeautifulSoup(source,'html.parser')

        for job in soup.findAll('div',class_='sjcl'):
            data_list = []
            job_data = job.parent
            try:
                job_title = job_data.find('div',class_="title").text
                data_list.append(str(job_title))
            except:
                data_list.append(None)
                
            try:
                com_name = job_data.find('div',class_='sjcl').find('span',class_="company").text
                data_list.append(str(com_name))
            except:
                data_list.append(None)
            
            try:
                job_loc = job_data.find('div',class_="location accessible-contrast-color-location").text
                data_list.append(str(job_loc))
            except:
                data_list.append(None)

            try:
                sal = job_data.find('div',class_="salarySnippet salarySnippetDemphasizeholisticSalary").find('span',class_="salaryText").text
                data_list.append(str(sal))
            except:
                data_list.append(None)

            try:
                rate = job_data.find('div',class_='sjcl').find('span',class_="ratingsDisplay").a.text
                data_list.append(str(rate))
            except:
                data_list.append(None)
            
            writer.writerow(data_list)
    except:
        print(404)
    page_count = page_count+1



print(page_count)

# for each_div in soup.findAll('div',class_="title"):
#     print(each_div.a.text)
#     print('\n')
'''
data =  soup.find('div',class_='sjcl')
item = data.find('span',class_="company").parent.parent.parent
######## one comany name and one title name and one job_location #########3
job_title = item.find('div',class_='title').text
print(job_title)

# c_name = item.findAll('div',class_="sjcl")
# print(len(c_name))
# job_loc = item.find('div',class_="location accessible-contrast-color-location").text
# print(c_name,len(c_name))
# print(job_title.strip(' '))
# print(job_loc)



################### working code for finding all job titles ###########
# count = 0
data = soup.find('table',{'id':'pageContent'}).find('tr',{'valign':'top'}).find('td',{'id':'resultsCol'})
# for each_div in data.findAll('div',class_="title"):
#     print(each_div.a.text)
#     print('\n')
#     count = count+1

############### code for all company names ########################3
# for i in data.findAll('div',class_='sjcl'):
#     print(i.find('div').find('span',class_="company").text)

    
# print(count)

##################### code for location ##############
# for i in data.findAll('div',class_="location accessible-contrast-color-location"):
#     print(i.text)

'''
'''
count = 0

    
'''    



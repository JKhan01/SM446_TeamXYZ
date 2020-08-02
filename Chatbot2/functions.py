
from atlassian import Confluence
from pprint import pprint
import json

cf = Confluence(
    url='https://shritej112.atlassian.net/',
    username='patilshritej112@gmail.com',
    password='c59BywMlA8hy4mFsWW3U53D2'
    )

# Define all the Confluence functions here
# Then reference these functions to the code of assistant after intent identification
# Based on the intent, call a particular function
# Take input, and give appropriate output

# 1. Users




# 2. Spaces
def create_space(key, name):
    #key = input(print("Enter the space key:"))
    #name = input(print("Enter the name of the space:"))
    cf.create_space(key, name)
    print("Space Created")
    return (json.dumps("Space Created"))
    #return (print(json.dumps("Space Created")))


def get_all_spaces():
    a = cf.get_all_spaces()
    
    e = []
    for i in range(len(a)):
        d = {}
        d['id'] = a[i]['id']
        d['key'] = a[i]['key']
        d['name'] = a[i]['name']
        d['status'] = a[i]['status']
        d['type'] = a[i]['type']

        e.append(d)
    #return(print(json.dumps(e, indent = 2)))
    return(json.dumps(e, indent = 2))


def get_info_space(key):
    #key = int(input("Enter the space key:"))
    a = cf.get_space(key, expand='description.plain,homepage')
    d = {}
    d['id'] = a['id']
    d['key'] = a['key']
    d['name'] = a['name']
    d['status'] = a['status']
    d['type'] = a['type']
    d['homepage_id'] = a['homepage']['id']
    d['homepage_title'] = a['homepage']['title']
    #e.append(d)
    return(json.dumps(d, indent = 2))

            

def get_pages_in_a_space(name):
    #name = input(print("Enter the name of the space"))
    
    a = cf.get_all_pages_from_space(name, start=0, limit=50, status=None, expand=None, content_type='page')
    e = []
    for i in range(len(a)):
        d = {}
        d['id'] = a[i]['id']
        d['status'] = a[i]['status']
        d['title'] = a[i]['title']
        d['type'] = a[i]['type']
        e.append(d)

    return(json.dumps(e, indent = 2))


# 3. Pages
def create_page(space, title, body):

    cf.create_page(space, title, body)
    #print("Page Created")
    return (json.dumps("Page Created"))
    #return (print(json.dumps("Page Created")))

def delete_page(id):
    #id = int(input(print("Enter the ID of the page:")))
    cf.remove_page(id, status=None, recursive=False)
    #print("Page Deleted")
    #return(print(json.dumps("Page Deleted")))
    return(json.dumps("Page Deleted"))

def check_page_exists(space, title):
    #space = input(print("Enter the name of the space to be checked:"))
    #title = input(print("Enter the title of the page that has to be checked:"))
    
    return (json.dumps(cf.page_exists(space, title)))

def get_page_id(space, title):
    #space = input(print("Enter the space name:"))
    #title = input(print("Enter the title of the page:"))
    
    return (json.dumps(cf.get_page_id(space, title)))
    #return (print(json.dumps(cf.get_page_id(space, title))))
    
def get_page_space(id):
    #id = int(input(print("Enter the page ID:")))
    
    return (json.dumps(cf.get_page_space(id)))

# Page Info using title
def page_info_by_title(space, title):
    a = cf.get_page_by_title(space, title, start=None, limit=None)
    d = {}
    d['id'] = a['id']
    d['status'] = a['status']
    d['title'] = a['title']
    d['type'] = a['type']
    
    return(json.dumps(d, indent = 2))

# Page info using ID
def page_info_by_id(id):
    a = cf.get_page_by_id(id, expand=None, status=None, version=None)
    d = {}
    d['id'] = a['id']
    d['status'] = a['status']
    d['title'] = a['title']
    d['type'] = a['type']
    d['space_name'] = a['space']['name']
    d['space_key'] = a['space']['key']
    d['space_id'] = a['space']['id']
    d['creator_email'] = a['history']['createdBy']['email']
    d['creator_displayName'] = a['history']['createdBy']['displayName']
    d['created_date'] = a['history']['createdDate']
    return(json.dumps(d, indent = 2))
   

# Export Page as PDF
def export_page_as_pdf(id, name):
    #id = int(input(print("Enter the page ID:")))
    #name = input(print("Enter the name of the pdf file to be created:"))
    a = cf.export_page(id)
    
    def save_file(content):
        file_pdf = open(name, 'wb')
        file_pdf.write(content)
        file_pdf.close()
        print("Completed")
    
    save_file(content=a)
    #print(a)
    print("Page Exported")
    return (json.dumps("Page Exported"))
    #return (print(json.dumps("Page Exported")))
    # Deadline : 6:00 pm
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
    pprint(cf.get_all_spaces())
    #return(cf.get_all_spaces())
    #return (json.dumps(cf.get_all_spaces(), indent = 4))
    return (pprint(json.dumps(cf.get_all_spaces(), indent = 4)))


def get_info_space(key):
    #key = int(input("Enter the space key:"))
    pprint(cf.get_space(key, expand='description.plain,homepage'))
    return (json.dumps(cf.get_space(key, expand='description.plain,homepage'), indent = 4))
    #return (pprint(json.dumps(cf.get_space(key, expand='description.plain,homepage'), indent = 4)))

            

def get_pages_in_a_space(name):
    #name = input(print("Enter the name of the space"))
    pprint(cf.get_all_pages_from_space(name, start=0, limit=50, status=None, expand=None, content_type='page'))
    #return (pprint(json.dumps(cf.get_all_pages_from_space(name, start=0, limit=50, status=None, expand=None, content_type='page'), indent = 4)))
    return (json.dumps(cf.get_all_pages_from_space(name, start=0, limit=50, status=None, expand=None, content_type='page'), indent = 4))


# 3. Pages
def create_page(space, title, body):
    #space = input(print("Enter the name of the space in which the page is to be created:"))
    #name = raw_input(print("Enter the name of the page to be created:"))
    #title = input(print("Enter the title of the page:"))
    #body = input(print("Enter the body of the page:"))
    cf.create_page(space, title, body)
    print("Page Created")
    return (json.dumps("Page Created"))
    #return (print(json.dumps("Page Created")))

def delete_page(id):
    #id = int(input(print("Enter the ID of the page:")))
    cf.remove_page(id, status=None, recursive=False)
    print("Page Deleted")
    #return(print(json.dumps("Page Deleted")))
    return(json.dumps("Page Deleted"))

def check_page_exists(space, title):
    #space = input(print("Enter the name of the space to be checked:"))
    #title = input(print("Enter the title of the page that has to be checked:"))
    pprint(cf.page_exists(space, title))
    #return (pprint(json.dumps(cf.page_exists(space, title))))
    return (json.dumps(cf.page_exists(space, title)))

def get_page_id(space, title):
    #space = input(print("Enter the space name:"))
    #title = input(print("Enter the title of the page:"))
    print(cf.get_page_id(space, title))
    return (json.dumps(cf.get_page_id(space, title)))
    #return (print(json.dumps(cf.get_page_id(space, title))))
    
def get_page_space(id):
    #id = int(input(print("Enter the page ID:")))
    print(cf.get_page_space(id))
    return (json.dumps(cf.get_page_space(id)))

# Page Info using title
def page_info_by_title(space, title):
    #space = input(print("Enter the space name:"))
    #title = input(print("Enter the title of the page:"))
    pprint(cf.get_page_by_title(space, title, start=None, limit=None))
    #return (pprint(json.dumps(cf.get_page_by_title(space, title, start=None, limit=None), indent = 4)))
    return (json.dumps(cf.get_page_by_title(space, title, start=None, limit=None), indent = 4))

# Page info using ID
def page_info_by_id(id):
    #id = int(input(print("Enter the page ID:")))
    pprint(cf.get_page_by_id(id, expand=None, status=None, version=None))
    #return (pprint(json.dumps(cf.get_page_by_id(id, expand=None, status=None, version=None), indent = 4)))
    return (json.dumps(cf.get_page_by_id(id, expand=None, status=None, version=None), indent = 4))
   

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
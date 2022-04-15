#Inserting content into base template

def content_replace(template, content_file, title):
    combined_file = template.replace("{{content}}", content_file)
    combined_file = combined_file.replace("{{title}}", title)
    return combined_file

#Working on function to display the active tab by changing the css it recieves

# def navbar_status(combined_file, title):
#         combined_file = combined_file.replace("{{nav_status_",title"}}", "class = 'nav-active-tab'")
#     else:
#         combined_file = combined_file.replace("{{nav_status",['']}}, "class = 'nav-item")


#Outputing finished files
def main(pages):
    template = open("./templates/base.html").read()
    #for loop to generate each content page from filepaths specified outside of function
    for page in pages:
        content_file = open(page['filename']).read()
        title = page['title']
        output_file = page['output']
        combined_file = content_replace(template, content_file, title)
        
        # combined_file = combined_file.replace({{title}}, 'nav-active-tab')
        open(output_file, 'w+').write(combined_file)



pages = [
    {
    "filename": "./content/index.html",
    "output": "./docs/index.html",
    "title": "About",
    },
    {
    "filename": "./content/projects.html",
    "output": "./docs/projects.html",
    "title": "Projects",
    },

    {
    "filename": "./content/resume.html",
    "output": "./docs/resume.html",
    "title": "Resume",

    }

]
    
main(pages)
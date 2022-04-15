#Constant across pages
def main(pages):
    template = open("./templates/base.html").read()
    #for loop to generate each content page from filepaths specified outside of function
    for page in pages:
        content_file = open(page['filename']).read()
        output_file = page['output']
        template.replace("{{content}}", content_file)

        combined_file = template.replace("{{content}}", content_file)
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
    "title": "My Projects",
    },

    {
    "filename": "./content/resume.html",
    "output": "./docs/resume.html",
    "title": "My Resume",

    }

]
    
main(pages)
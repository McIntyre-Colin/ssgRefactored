#Constant across pages
def main(pages):
    header = open('./templates/header.html').read()
    footer = open('./templates/footer.html').read()

    #for loop to generate each content page from filepaths specified outside of function
    for page in pages:
        content_file = open(page['filename']).read()
        output_file = page['output']
        
        combined_file = header + content_file + footer
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
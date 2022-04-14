#Constant across pages
def main(pages):
    header = open('./templates/header.html').read()
    footer = open('./templates/footer.html').read()

    for page in pages:
        content_file = page['filename']
        output_file = page['output']
        open(output_file, 'w+').write(header,content_file, footer)

    #Crwating webpages
    open('./docs/index.html', 'w+').write(index)
    open('./docs/projects.html', 'w+').write(projects)
    open('./docs/resume.html', 'w+').write(resume)




pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "About",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "My Projects",
    },

    {
    "filename": "content/resume.html",
    "output": "docs/resume.html",
    "title": "My Resume",

    }

]
    
main()
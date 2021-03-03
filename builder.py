from distutils.util import strtobool
import os
import pathlib
import re
import sys
import unicodedata


DIRS = [
    '{project_slug}/',
    '{project_slug}/static/',
    '{project_slug}/static/img/',
    '{project_slug}/static/js/',
    '{project_slug}/static/css/',
    '{project_slug}/templates/',
]

FILES = {
    '{project_slug}/requirements.txt': 'requirements.txt.template',
    '{project_slug}/app.py': 'app.py.template',
    '{project_slug}/static/css/{project_slug}.css': 'project.css.template',
    '{project_slug}/static/js/{project_slug}.js': 'project.js.template', 
    '{project_slug}/templates/index.html': 'index.html.template'
}

def create_dirs(root, slug):
    try:
        os.makedirs(root)
    except OSError:
        print("Could not create the project root at {}.".format(root))
        sys.exit()
        # stops executing program
    else:
        for dir in DIRS:
            try:
                os.makedirs(os.path.join(root, dir.format(project_slug=slug)))
            except FileExistsError:
                print("Could not create the project root at {}.".format(root))
                sys.exit()

def slugify(string):
    string = unicodedata.normalize('NFKC', string)
    string = re.sub(r'[\w\s]', '', string).strip().lower()
    # only accepts unicode characters, strips anything that is not a word character or a space, sets to lowercase 
    return re.sub(r'[_\-\s]+', '_', string)
    # replaces any instance of one or more space, hyphen or underscore with a single underscore, and return the resulting string

def get_root():
    root = pathlib.PurePath(
        input("What is the full path where you would like your project?  ")
    )
    if not root.is_absolute():
        return get_root()
        # resets the function to get the user to do what we asked
    return root

def check_delete_root(root):
    if os.path.exists(root): 
        # checks to see if path exists
        print("Path already exists")
        try:
            delete = strtobool(input("Delete existing files/directories? [y/n]  ").lower())
            # asks if the user wants us to delete the existing path
        except ValueError:
            return check_delete_root(root)
        else:
            if delete:
                try:
                    os.removedirs(root)
                    # if boolean is true, we'll try to delete. if we can't delete, we give a message for the user to delete
                except OSError:
                    print("Could not remove {}. Please remove manually.".format(root))
                else:
                    print("{} removed successfully!".format(root))

def main():
    """Entry point"""
    project_root = get_root()
    check_delete_root(project_root)
    # check for root before asking for name so we dont ask for a name if we dont have to
    project_name = None
    while not project_name:
        project_name = input("What is the full name of your project?  ").strip().lower()
        # asks for the name of the project
    project_slug = slugify(project_name)

    create_dirs(project_root, project_slug)
    
    print("Creating {} in {}".format(project_name, project_root))
    # confirms the name and location where the project was created

if __name__ == '__main__':
    main()

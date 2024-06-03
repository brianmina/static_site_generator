import os
import shutil

from copystatic import copy_files_recursive
from html_generator import generate_page

dir_path_static = 'github.com/brianmina/static_site_generator/static'
dir_path_public = "github.com/brianmina/static_site_generator/public"
dir_path_content = "github.com/brianmina/static_site_generator/content"
template_path = "github.com/brianmina/static_site_generator/template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
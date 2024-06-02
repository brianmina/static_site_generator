from textnode import TextNode
import os
import shutil

def copy_static(source, destination):
    # Check if the source directory exists
    if not os.path.exists(source):
        print(f"Current working directory: {os.getcwd()}")
        print(f"The source directory {source} does not exist.")
        return
    
    # Ensure the destination directory exists or create it
    if not os.path.exists(destination):
        os.mkdir(destination)
        print(f"Created the destination directory {destination}")

    # List the contents of the source directory
    items = os.listdir(source)
    print(f"Items to copy from {source}: {items}")

    # Process each item in the source directory
    for item in items:
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)

        if os.path.isfile(source_item):
            print(f"Copying file: {source_item} to {destination_item}")
            shutil.copy(source_item, destination_item)
        elif os.path.isdir(source_item):
            print(f"Entering directory: {source_item}")
            copy_static(source_item, destination_item)


if __name__ == "__main__":
    copy_static('static', 'public')

from pathlib import Path 
 
SAFE_FOLDERS = ["Apresentações", "Áudio e Músicas", "Compactados", "Documentos", "GIFs", "Imagens", "Livros", "Outros", "Planilhas", "Programas", "Textos", "Vídeos"]

def main():
    """
    Coordinates the organization of 'Downloads' folder and its main sub-directories, guaranteeing that loose files and directories are moved to categories
    
    """
    p = Path.home() / "Downloads" # creates a path object to "Downloads" directory concatenating the Path.home() object, i.e "C:\Users\Asus" with "Downloads" folder
    organize_folders(p, p)
    outros = p / "Outros"
    if outros.exists():
        organize_folders(outros, p)

def organize_folders(target_path, root_path):
    """
    Iterates over a specific folder (target_path) amd moves its files to the correct directories inside the root_path 
    
    :param target_path: represents the current path (folder) being 'scanned'
    :type target_path: Path class object (pathlib.Path)
    :param root_path: represents the fixed path where all category folders are (i.e, 'Downloads')
    :type root_path: Path class object (pathlib.Path)
    :return: None. The function operates files directly
    """
    
    for child in target_path.iterdir(): # child means file or directory; iterdir iterates over each child of the directory 
        if child.is_file(): 
            file_extension = child.suffix.lower() # the extension is the suffix attribute in lowercase to avoid errors
            destination_name = get_category(file_extension) # calls get_category function on the file_extension variable to return the folder; this variable is just a string
            target_dir = root_path / destination_name  # a new path object using the root_path argument and the destination folder name (string)
            target_dir.mkdir(exist_ok=True) # actually creates the new directory. "exist_ok" parameter means that if the dir already exists, nothing happens; if it doesn't, it creates a new one.
            try:
                child.rename(target_dir / child.name) # renaming is like realocating: it puts each child inside its respective target_dir inside the Downloads file
                print(f"Movido: {child.name}")
            except PermissionError:
                print(f"Erro: não pude mover {child.name}. O arquivo pode estar aberto.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
        elif child.is_dir() and child.name not in SAFE_FOLDERS: # handles random folders inside root_path that are not one of the folders created by this program
            target_dir = root_path / "Outros" # their place will be in the "Outros" folder
            target_dir.mkdir(exist_ok=True)
            try:
                child.rename(target_dir / child.name)
                print(f"Movido: {child.name}")
            except PermissionError:
                print(f"Erro: não pude mover {child.name}. A pasta pode estar sendo usada.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")    

def get_category(extension):
    """
    Returns the name of the destination folder based on the file extension 
    
    :param extension: represents file extension (i.e, '.pdf') 
    :type extension: str
    :return: A string with the respective destination folder name; 'Outros' if the extension is not mapped
    """
    
    categories = {
        ".webp": "Imagens",
        ".jpg": "Imagens",
        ".jpeg": "Imagens",
        ".jpg_large": "Imagens",
        ".png": "Imagens",
        ".ico": "Imagens",
        ".jfif": "Imagens",
        ".tif": "Imagens",
        ".pdf": "Documentos",
        ".docx": "Documentos",
        ".odt": "Documentos",
        ".xlsx": "Planilhas",
        ".pptx": "Apresentações",
        ".epub": "Livros",
        ".zip": "Compactados",
        ".rar": "Compactados",
        ".mp4": "Vídeos",
        ".webm": "Vídeos",
        ".mp3": "Áudio e Músicas",
        ".ogg": "Áudio e Músicas",
        ".exe": "Programas",
        ".msi": "Programas",
        ".gif": "GIFs",
        ".txt": "Textos",
    }
    return categories.get(extension, "Outros") 


if __name__ == "__main__":
    main()


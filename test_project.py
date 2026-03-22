import pytest #type: ignore
from project import get_category

def test_get_category_images():
    extensions = [".webp", ".jpg", ".jpeg", ".jpg_large", ".png", ".ico", ".jfif", ".tif"]
    for ext in extensions:
        assert get_category(ext) == "Imagens"

def test_get_category_documents():
    assert get_category(".pdf") == "Documentos"
    assert get_category(".docx") == "Documentos"
    assert get_category(".odt") == "Documentos"

def test_get_category_media():
    # Vídeos
    assert get_category(".mp4") == "Vídeos"
    assert get_category(".webm") == "Vídeos"
    # Áudio
    assert get_category(".mp3") == "Áudio e Músicas"
    assert get_category(".ogg") == "Áudio e Músicas"
    # GIFs
    assert get_category(".gif") == "GIFs"

def test_get_category_office_and_books():
    assert get_category(".xlsx") == "Planilhas"
    assert get_category(".pptx") == "Apresentações"
    assert get_category(".epub") == "Livros"
    assert get_category(".txt") == "Textos"

def test_get_category_system_and_archive():
    # Programas
    assert get_category(".exe") == "Programas"
    assert get_category(".msi") == "Programas"
    # Compactados
    assert get_category(".zip") == "Compactados"
    assert get_category(".rar") == "Compactados"

def test_get_category_fallback():
    # Teste para extensões não mapeadas ou vazias
    assert get_category(".xyz") == "Outros"
    assert get_category("") == "Outros"
    assert get_category(".unknown") == "Outros"
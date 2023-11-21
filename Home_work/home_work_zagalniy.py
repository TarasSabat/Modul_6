import re

CYRILLIC_SYMBOLS = 'абвгдежзйклмнопрстуфхцчшщюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "j", "z", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "yu", "ja", "je", 'i', "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_name = name.split('.')
    translate_name[0] = re.sub(r'\W', '_', translate_name[0].translate(TRANS))
    my_name = ('.'.join(translate_name))
    return my_name

'''
Сортування файлів за розширенням 
'''
import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENT = []
DOCX_DOCUMENT = []
TXT_DOCUMENT = []
PDF_DOCUMENT = []
XLSX_DOCUMENT = []
PPTX_DOCUMENT = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENT,
    'DOCX': DOCX_DOCUMENT,
    'TXT': TXT_DOCUMENT,
    'PDF': PDF_DOCUMENT,
    'XLSX': XLSX_DOCUMENT,
    'PPTX': PPTX_DOCUMENT,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES, 
    'TAR': TAR_ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  
            if item.name not in ('archives', 'videos', 'audios', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  
        full_name = folder / item.name  
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1] 
    scan(Path(folder_process))
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Videos avi: {AVI_VIDEO}')
    print(f'Videos mp4: {MP4_VIDEO}')
    print(f'Videos mov: {MOV_VIDEO}')
    print(f'Videos mkv: {MKV_VIDEO}')
    print(f'Documents doc: {DOC_DOCUMENT}')
    print(f'Documents docx: {DOCX_DOCUMENT}')
    print(f'Documents txt: {TXT_DOCUMENT}')
    print(f'Documents pdf: {PDF_DOCUMENT}')
    print(f'Documents xlsx: {XLSX_DOCUMENT}')
    print(f'Documents pptx: {PPTX_DOCUMENT}')
    print(f'Audios mp3: {OGG_AUDIO}')
    print(f'Audios wav: {WAV_AUDIO}') 
    print(f'Audios amr: {AMR_AUDIO}') 
    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')
    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
    print(f'FOLDERS: {FOLDERS}')
    print(f'MY_OTHER: {MY_OTHER}')


'''
--------------------------------
'''

from pathlib import Path
import shutil
import sys
import file_parser
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))
   
def handle_document(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_other(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    file_parser.scan(folder)
    for file in file_parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in file_parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in file_parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in file_parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in file_parser.AVI_VIDEO:
        handle_media(file, folder / 'videos' / 'AVI')
    for file in file_parser.MP4_VIDEO:
        handle_media(file, folder / 'videos' / 'MP4')
    for file in file_parser.MOV_VIDEO:
        handle_media(file, folder / 'videos' / 'MOV')   
    for file in file_parser.MKV_VIDEO:
        handle_media(file, folder / 'videos' / 'MKV')   
    for file in file_parser.MP3_AUDIO:
        handle_media(file, folder / 'audios' / 'MP3')
    for file in file_parser. OGG_AUDIO:
        handle_media(file, folder / 'audios' / 'OGG')
    for file in file_parser. WAV_AUDIO:
        handle_media(file, folder / 'audios' / 'WAV')
    for file in file_parser. AMR_AUDIO:
        handle_media(file, folder / 'audios' / 'AMR')
    
    for file in file_parser.DOC_DOCUMENT:
        handle_document(file, folder / 'documents' / 'DOC')  
    for file in file_parser.DOCX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'DOCX')
    for file in file_parser.TXT_DOCUMENT:
        handle_document(file, folder / 'documents' / 'TXT')
    for file in file_parser.PDF_DOCUMENT:
        handle_document(file, folder / 'documents' / 'PDF')
    for file in file_parser.XLSX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'XLSX')
    for file in file_parser.PPTX_DOCUMENT:
        handle_document(file, folder / 'documents' / 'PPTX')

    for file in file_parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    
    for file in file_parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in file_parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in file_parser.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'TAR')
       
    for folder in file_parser.FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')


if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())




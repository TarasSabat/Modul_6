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


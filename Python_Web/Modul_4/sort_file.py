import re
import pathlib
import shutil
from threading import Thread

IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
ARCHIVES = []
FOLDERS = []
REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'PDF': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


CYRILlIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєії'
TRANSLATION = ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
               'f', 'h', 'ts', 'ch', 'sh', 'sch', '', 'y', 'e', 'u', 'ja', 'e', 'i', 'i')


TRANS = {}


for cs, trl in zip(CYRILlIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str) -> str:
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r'\W', '_', trl_name)
    return trl_name


def scan(folder: pathlib.Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('images', 'videos', 'documents', 'archives'):
                FOLDERS.append(item)
                scan(item)
        name, extension = item.stem, item.suffix
        new_name = normalize(name)
        new_item = folder / ''.join([new_name, extension])
        item.rename(new_item)
        if extension.upper().strip('.') in REGISTERED_EXTENSIONS:
            container = REGISTERED_EXTENSIONS[extension.upper().strip('.')]
            container.append(new_item)


def handle_image(path: pathlib.Path, root_folder: pathlib.Path):
    print(f'handle_image - {path}')
    target_folder = root_folder / 'images'
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_audio(path: pathlib.Path, root_folder: pathlib.Path):
    print(f'handle_audio - {path}')
    target_folder = root_folder / 'audio'
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_video(path: pathlib.Path, root_folder: pathlib.Path):
    print(f'handle_video - {path}')
    target_folder = root_folder / 'video'
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/path.name)


def handle_archive(path: pathlib.Path, root_folder: pathlib.Path):
    print(f'handel_archive - {path}')
    target_folder = root_folder / 'archive'
    name = path.stem
    target_folder.mkdir(exist_ok=True)
    archive_folder = target_folder / name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.absolute()), str(archive_folder.absolute()))
    except Exception:
        archive_folder.rmdir()
        return


def handle_documents(path: pathlib.Path, root_folder: pathlib.Path):
    print(f'handle_documents - {path}')
    target_folder = root_folder / 'documents'
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / path.name)


def handle_folder(path: pathlib.Path):
    print(f'handle_folder - {path}')
    try:
        path.rmdir()
    except OSError:
        pass


def sort_folder(path):
    folder = pathlib.Path(path)
    print(f'Start in folder: "{folder}"')
    print('-----' * 20)
    scan(folder)
    threads = []
    for file in IMAGES:
        threads.append(Thread(target=handle_image, args=(file, folder)))

    for file in AUDIO:
        threads.append(Thread(target=handle_audio, args=(file, folder)))

    for file in VIDEO:
        threads.append(Thread(target=handle_video, args=(file, folder)))

    for file in DOCUMENTS:
        threads.append(Thread(target=handle_documents, args=(file, folder)))

    for file in ARCHIVES:
        threads.append(Thread(target=handle_archive, args=(file, folder)))

    for f in FOLDERS:
        threads.append(Thread(target=handle_folder, args=(f,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('-----' * 20)



if __name__ == '__main__':
    path = input('Введите путь для сортировки.\n>>> ')
    try:
        sort_folder(path)
    except TypeError:
        print(f'Вы не передали путь при вызове скрипта. Попробуйте еще раз.')
    else:
        print('Сортировка окончена')
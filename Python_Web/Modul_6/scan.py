from aiopath import AsyncPath

IMAGE = []
VIDEO = []
DOC = []
AUDIO = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "IMAGE": IMAGE,
    "VIDEO": VIDEO,
    "DOC": DOC,
    "AUDIO": AUDIO,
    "ARCH": ARCH,
    "OTHER": OTHER,
}


def get_extension(file_name):
    return AsyncPath(file_name).suffix[1:].upper()


async def scan(folder):
    async for item in folder.iterdir():
        is_folder = await item.is_dir()
        if is_folder:
            if item.name not in ("images", "video", "audio", "documents", "other", "archives"):
                FOLDERS.append(item)
                await scan(item)
            continue
        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            if extension in ("JPEG", "JPG", "SVG", "PNG"):
                current_container = REGISTERED_EXTENSIONS.get("IMAGE")
                EXTENSION.add(extension)
                current_container.append(new_name)
            elif extension in ("MP4", "MPEG", "WMV", "MOV", "MKV", "3gp", "AVI"):
                current_container = REGISTERED_EXTENSIONS.get("VIDEO")
                EXTENSION.add(extension)
                current_container.append(new_name)
            elif extension in ("MP3",):
                current_container = REGISTERED_EXTENSIONS.get("AUDIO")
                EXTENSION.add(extension)
                current_container.append(new_name)
            elif extension in ("DOC", "DOCX", "TXT", "PDF"):
                current_container = REGISTERED_EXTENSIONS.get("DOC")
                EXTENSION.add(extension)
                current_container.append(new_name)
            elif extension in ("ZIP", "RAR"):
                current_container = REGISTERED_EXTENSIONS.get("ARCH")
                EXTENSION.add(extension)
                current_container.append(new_name)
            else:
                UNKNOWN.add(extension)
                OTHER.append(new_name)
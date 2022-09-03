import sys
import shutil
import asyncio
from aiopath import AsyncPath

import scan
from normalize import normalize


async def handle_files(root_folder, folder_for_sort, dist: str):
    for file in folder_for_sort:
        target_folder = root_folder / dist
        async_folder = AsyncPath(target_folder)
        await async_folder.mkdir(exist_ok=True)
        ext = AsyncPath(file).suffix
        new_name = normalize(file.name.replace(ext, "")) + ext

        if dist != 'archives':
            await file.replace(target_folder / new_name)
        else:
            archive_folder = target_folder / new_name
            async_folder = AsyncPath(archive_folder)
            await async_folder.mkdir(exist_ok=True)
            try:
                async_file = AsyncPath(file)
                shutil.unpack_archive(str(async_file), str(async_folder))
            except shutil.ReadError:
                archive_folder.rmdir()
                return
            await file.unlink()


async def handle_folder(folder):
    try:
        await folder.rmdir()
    except OSError:
        pass


async def main(folder):
    async_path = AsyncPath(folder)
    await scan.scan(async_path)

    await handle_files(folder, scan.IMAGE, 'images')
    await handle_files(folder, scan.VIDEO, 'video')
    await handle_files(folder, scan.AUDIO, 'audio')
    await handle_files(folder, scan.DOC, 'documents')
    await handle_files(folder, scan.OTHER, 'other')
    await handle_files(folder, scan.ARCH, 'archives')

    for item in scan.FOLDERS:
        await handle_folder(item)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = AsyncPath(scan_path)
    asyncio.run(main(sort_folder))
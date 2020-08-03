import os


def rename():
    paths = os.getenv('SUBTITLE_RENAME_DIR', '/rename').lower()
    suffix = os.getenv('SUBTITLE_SUFFIX', '.pt').lower()
    ext = os.getenv('SUBTITLE_EXT', '.srt').lower()

    for path in paths.split(";"):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                file_ext = os.path.splitext(file)
                if file_ext[1].lower() == ext and not file_ext[0].lower().endswith(suffix):
                    files.append(os.path.join(r, file))

        for f in files:
            file_ext = os.path.splitext(f)
            new_name = f'{file_ext[0]}{suffix}{file_ext[1]}'
            print(f'renamed: {f} -> {new_name}')
            os.rename(f, new_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename()

import os


def rename():
    paths = os.getenv('SUBTITLE_RENAME_DIR', './test')
    suffix = os.getenv('SUBTITLE_SUFFIX', '.pt').lower()
    ext = os.getenv('SUBTITLE_EXT', '.srt').lower()

    for path in paths.split(";"):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                file_ext = os.path.splitext(file)
                name = file_ext[0].lower()
                if file_ext[1].lower() == ext and not (name.endswith(suffix) or name.endswith(f'{suffix}.forced')):
                    files.append(os.path.join(r, file))

        for f in files:
            file_ext = os.path.splitext(f)
            if file_ext[0].endswith('.forced'):
                new_name = f'{file_ext[0][:-7]}{suffix}.forced{file_ext[1]}'
            else:
                new_name = f'{file_ext[0]}{suffix}{file_ext[1]}'
            print(f'renamed: {f} -> {new_name}')
            os.rename(f, new_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename()

import os


def support_file_path(filename):
    return os.path.join('test/support/files/', filename)


def support_file_contents(filename):
    with open(support_file_path(filename), 'rb') as f:
        return f.read()

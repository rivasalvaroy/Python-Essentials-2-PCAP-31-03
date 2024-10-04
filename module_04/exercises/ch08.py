import os


class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:  # No procesa un archivo que no es un directorio.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)
            os.chdir("../")


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")

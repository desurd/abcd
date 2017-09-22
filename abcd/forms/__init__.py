#print (self.currentPath)

# temporary remove for debugging purpose
#


# fileList = os.listdir(self.currentPath)
# print (fileList)
# listclass0 = []
# listclass = []
# for element in fileList:
#     if not fnmatch.fnmatch(element, '*.py'):
#         continue
#     # remove .py for the file which are py
#     modulename = element[:-3]
#     listclass0.append(modulename)
#     pkg = __import__(__name__, globals(), locals(), [modulename])
#     listclass.append(pkg)
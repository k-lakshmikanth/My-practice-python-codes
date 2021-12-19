# **************************
# Utility to count the number of files in and size of a directory
# **************************

def computeFileStats(path):
  bytes = 0
  count = 0

  files = dbutils.fs.ls(path)
  
  while (len(files) > 0):
    fileInfo = files.pop(0)
    if (fileInfo.isDir() == False):               # isDir() is a method on the fileInfo object
      count += 1
      bytes += fileInfo.size                      # size is a parameter on the fileInfo object
    else:
      files.extend(dbutils.fs.ls(fileInfo.path))  # append multiple object to files
      
  return (count, bytes)
  
from browser_history import *

def writeHistory(list):
    file1 = open("history.txt", "w")

    for i in range(len(list)):
        file1.write(list[i][1] + "\n")

    file1.close()

def writeBookmarks(list):
    file2 = open("bookmarks.txt", "w")

    for i in range(len(list)):
        file2.write(list[i][1] + "\n")

    file2.close()

outputs = get_history()
bookmarks = get_bookmarks()

history = outputs.histories
bookmarks = bookmarks.bookmarks

writeHistory(history)
writeBookmarks(bookmarks)
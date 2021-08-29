import webbrowser

link = 'https://www.youtube.com/watch?v='

for i in range(1,4):
    filename = "solution/" + str(i) + ".txt"
    try:
        link += open(filename).read()
    except FileNotFoundError:
        link = 'https://www.youtube.com/watch?v=' # resetting link
        print(filename + " cannot be found.")

try:
    webbrowser.open(link) 
except:
    print("ERROR: Unable to open link. Make sure that the video id is correct.")

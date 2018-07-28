import osproc
import os
import strutils as str

#Default bits for files...
echo "Setup default frontend, or flask?"
let choice: string = readLine(stdin)
let naming: string = "Name the project..."

let defaultHTML: string = "<!DOCTYPE html><html> <head> </head><body></body> </html>" 
let defaultCSS: string = "body {font-family: 'Ubuntu', sans-serif; color: #333333; background-color: #f6f9fc; }"
let defaultFlask: string = "from flask import Flask, render_template"
let READMENAME = "README.md"
#Write your README...
proc readmeMD(s: string) = 
    echo "Write the README.md for the project"
    let text: string = readLine(stdin)
    writeFile(s, text)

#Frontend setup...
proc frontEndTemp(s: string) =
    echo "Setting up Front-End Files"
    if not existsDir(s):
        createDir(s)
        setCurrentDir(s) #Is this correct? Enter new dirct...
        writeFile("main.html", defaultHTML)
        writeFile("style.css", defaultCSS)
        writeFile("index.js", "")
        readmeMD(READMENAME)

#Flasksetup..
proc flaskSetup(s: string) = 
    echo "Setting up files for Flask"
    if not existsDir(s):
        createDir(s)
        setCurrentDir(s)
        writeFile("app.py", defaultFlask)
        writeFile("style.css", defaultCSS) 
        createDir("static")
        createDir("templates")
        readmeMD(READMENAME) 
        setCurrentDir("templates")
        writeFile("main.html", defaultHTML)
        


#Decision tree...
if choice == "frontend":
    echo naming
    let name: string = readLine(stdin)
    frontEndTemp(name)
elif choice == "flask":
    echo naming
    let name: string = readLine(stdin)
    flaskSetup(name)
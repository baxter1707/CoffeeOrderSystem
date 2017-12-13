let body = document.getElementById("main")
let blueBox = document.getElementById("headerBar")
let title = document.createElement("h1")
title.innerHTML="HighOnCoding"
blueBox.appendChild(title)

let homeDiv = document.createElement("div")
let homeLink = document.createElement("a")
homeLink.innerHTML="Home"
homeLink.href = "index.html"
homeDiv.appendChild(homeLink)
blueBox.appendChild(homeDiv)


let catDiv = document.createElement("div")
let categoriesLink =document.createElement("a")
categoriesLink.innerHTML="Categories"
categoriesLink.href = "categories.html"
catDiv.appendChild(categoriesLink)
blueBox.appendChild(catDiv)

let grayBox = document.createElement("div")
grayBox.className="gray-box"
body.appendChild(grayBox)

let smallTitle = document.createElement("h2")
smallTitle.innerHTML="Curse of the Current Reviews"
grayBox.appendChild(smallTitle)

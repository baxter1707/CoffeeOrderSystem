
console.log(document.getElementById("email"))

// access the button
let emailButton = document.getElementById("displayEmailButton")
// attach the onclick event on the button
// anonymous function
emailButton.addEventListener('click',function() {
  console.log("button is clicked")
})

emailButton.addEventListener('mouseover',function(){
  console.log("Mouse over the button")
})


let div1 = document.getElementById("div1")

div1.addEventListener("mouseover",function(){
  let body = document.body
  body.style.backgroundColor = "yellow"
})

div1.addEventListener("mouseout",function(){
  let body = document.body
  body.style.backgroundColor = "blue"
})



function displayEmail() {
  console.log("You clicked the button")
}

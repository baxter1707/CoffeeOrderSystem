//let adBanner = document.getElementById("adDiv")
//elem.src = "images/ad.jpg";

//adBanner.addEventListener("load",function(){
//  let adImage= document.createElement("img");
  //adImage.setAttribute ("src", "images/ad.jpg")
  //adBanner.appendChild(adImage)
  //img.src= "images/ad.jpg"
  //adBanner.appendChild(img)
//})


let adBanner = document.getElementById("adDiv")
//adBanner.innerHTML="<img src='images/ad.jpg' />";
let adImage= document.createElement("img")  // <img></img>
adImage.className= "adImageClass" //<img class "adImageClass />"
adImage.src = "images/ad.jpg"; // <img class ="adImageClass" src='images/ad.jpg' />)
adBanner.appendChild(adImage)

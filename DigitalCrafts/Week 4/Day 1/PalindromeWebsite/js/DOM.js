let palinButton = document.getElementById("displayPalinButton")

palinButton.addEventListener("click", function() {
  let userInput = document.getElementById("palin").value;
  //document.write(userInput)

  let rev_word = "";

//please explain line 10
  for(index = userInput.length -1; index>= 0; index--){
    rev_word += userInput[index]
    console.log(rev_word)
  }

  if(userInput.toLowerCase() == rev_word.toLowerCase()){
  console.log("Palindrome!")
  window.alert("You entered a Palindrome!")
  document.getElementById("result").innerHTML = "You entered a Palindrome!"}

  else {
  console.log("Not Palindrome")
  window.alert("You did not enter a Palindrome")
  document.getElementById("result").innerHTML = "You did not enter a Palindrome!"
  }
})


  //for(let  index = 0; index<userInput.length; index++){
  //console.log(userInput[index])}


  //for(let index = userInput.length, rev_word = ""; index >= 0; rev_word +=[index--])
  //console.log(rev_word)
  //console.log(userInput)

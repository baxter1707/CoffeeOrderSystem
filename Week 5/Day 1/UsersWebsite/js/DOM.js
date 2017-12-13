let userSection = document.getElementById("user-list")

function getUserInfo(){
  for(let index=0; index<users.length; index++){


    let userList= `<div class="customerInfo">
    <label> Name </label>
    <li> ${users[index].name}</li>
    <label>Address</label>
    <li> ${users[index].address.street},  ${users[index].address.suite},  ${users[index].address.city}, <br> ${users[index].address.zipcode}</li>
    <label>Phone Number</label>
    <li> ${users[index].phone} </li>
    </div>`


    userSection.innerHTML += userList
  }
}


getUserInfo()

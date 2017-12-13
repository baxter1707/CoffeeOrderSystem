
let taskTextBox = $("#taskTextBox")
let pendingTasks = []
let completedTasks = []

$("#btnAddTask").click(function(){

  // create an array which contains the task elements
  let task = new Object()
  task.title = taskTextBox.val()
  pendingTasks.push(task)

  // create a parent div
  let taskItem = $("<div>",{ style :'display:flex' }).append($("<input>",{ type :'checkbox' }).click(function(){

    if($(this).is(':checked')) {
        // get the index of element checked
        let index = $(this).parent().index()
        // remove the item from the tree
        $(this).parent().remove()
        // add to the completed tasks
        completedTasks.push(pendingTasks[index])

        updateCompletedTasks()
    }

  })).append($("<li>").html(taskTextBox.val()))

  $("#pendingTaskList").append(taskItem)

})

function updateCompletedTasks() {
  console.log("update completed tasks")
}

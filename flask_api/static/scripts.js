document.addEventListener('DOMContentLoaded', function () {
    // Handle form submission for the todo form
    const todoForm = document.getElementById('todoForm');
    todoForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form from submitting the traditional way

        const taskInput = document.getElementById('task');
        const task = taskInput.value;

        // Add the task to the todo list
        const todoList = document.getElementById('todoList');
        const newTodoItem = document.createElement('li');
        newTodoItem.textContent = task;
        todoList.appendChild(newTodoItem);

        // Clear the input field
        taskInput.value = '';

        // Optionally, send the data to the server via AJAX
        // fetch('/add', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ task: task })
        // });
    });
});


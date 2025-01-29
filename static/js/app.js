document.addEventListener('DOMContentLoaded', function() {
    focusTaskInput();

    setupEditTaskLinks();

    confirmClearCompleted();

    autoDismissMessages();
});

function focusTaskInput() {
    const taskInput = document.querySelector('input[name="task_title"]');
    const addButton = document.getElementById('button-addon2');
    const todoForm = document.getElementById('todo-form');

    // Focus input on page load
    taskInput.focus();

    // Focus input when add button is clicked
    addButton.addEventListener('click', function() {
        taskInput.focus();
    });

    // Focus input when Enter key is pressed inside the form
    todoForm.addEventListener('submit', function(event) {
        setTimeout(() => {
            taskInput.focus();
        }, 10);  // Delay to ensure form submission happens first
    });
}


function setupEditTaskLinks() {
    document.querySelectorAll('.edit-task').forEach(function(editLink) {
        editLink.addEventListener('click', function(event) {
            event.preventDefault();
            let editUrl = this.getAttribute('data-url');
            let currentTask = this.closest('.todo-item').querySelector('span').textContent;

            let newTask = prompt('Edit your task:', currentTask);
            if (newTask && newTask.trim() !== '') {
                let form = document.createElement('form');
                form.method = 'POST';
                form.action = editUrl;

                let csrfInput = document.createElement('input');
                csrfInput.type = 'hidden';
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = '{{ csrf_token }}';

                let taskInput = document.createElement('input');
                taskInput.type = 'hidden';
                taskInput.name = 'new_task_title';
                taskInput.value = newTask;

                form.appendChild(csrfInput);
                form.appendChild(taskInput);
                document.body.appendChild(form);
                form.submit();
            } else {
                // Focus back to the add task input if prompt is canceled or empty
                taskInput.focus();
            } 
        });
    });
}


function confirmClearCompleted() {
    const clearCompletedForm = document.getElementById('clear-completed-form');
    clearCompletedForm.addEventListener('click', function(event) {
        const confirmation = confirm("Are you sure you want to clear all completed tasks?");
        if (!confirmation) {
            event.preventDefault(); // Prevent form action
        }
    });
}


function autoDismissMessages(timeout = 5000) {
    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = "opacity 0.5s ease, visibility 0.5s ease";
            alert.style.opacity = "0";
            alert.style.visibility = "hidden"; // Ensures it's visually removed

            setTimeout(function () {
                alert.remove();
            }, 500);
        }, timeout);
    });
}

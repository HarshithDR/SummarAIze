// interests.js

document.getElementById("interestForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get the entered interest
    var interest = document.getElementById("interest").value;
    
    // Add the interest to the display area
    var interestsList = document.getElementById("interestsList");
    var interestElement = document.createElement("div");
    interestElement.className = "interest";
    interestElement.innerHTML = interest;
    
    // Create a delete button
    var deleteButton = document.createElement("button");
    deleteButton.className = "delete-button";
    deleteButton.innerHTML = "x";
    
    // Add click event listener to delete button
    deleteButton.addEventListener("click", function() {
        interestElement.remove();
    });
    
    // Append interest and delete button to the display area
    interestElement.appendChild(deleteButton);
    interestsList.appendChild(interestElement);
    
    // Clear the input field
    document.getElementById("interest").value = "";
});

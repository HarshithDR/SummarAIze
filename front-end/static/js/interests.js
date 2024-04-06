// Define a global array to store all interests
var allInterests = [];

document.getElementById("interestForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    var interest = document.getElementById("interest").value.trim(); // Get the entered interest, trimmed of whitespace

    if (interest) {
        // Add the interest to the allInterests array if it's not empty
        allInterests.push(interest);

        // Update the UI to show the interest
        var interestsList = document.getElementById("interestsList");
        var interestElement = document.createElement("div");
        interestElement.className = "interest";
        interestElement.textContent = interest; // Set text content to escape HTML (safety reasons)

        // Create a delete button
        var deleteButton = document.createElement("button");
        deleteButton.className = "delete-button";
        deleteButton.textContent = "x";

        // Add click event listener to delete button for removal
        deleteButton.addEventListener("click", function() {
            var index = allInterests.indexOf(interest);
            if (index > -1) {
                allInterests.splice(index, 1); // Remove from array
            }
            interestElement.remove(); // Remove from UI
        });

        // Append interest and delete button to the display area
        interestElement.appendChild(deleteButton);
        interestsList.appendChild(interestElement);
        
        // Clear the input field
        document.getElementById("interest").value = "";
    }

    console.log("Current interests:", allInterests); // Debugging to see current state of interests
});

// Function to submit interests
function submitInterests() {
    console.log('Interests submitted:', allInterests);
    // Potentially send this data to a server or process it as needed
    // Example: POST request to a server endpoint
}

// Ensure the submit button or method is properly set up to call submitInterests when needed

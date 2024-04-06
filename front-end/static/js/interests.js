// This code should replace your existing JavaScript handling for adding and submitting interests.

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
    // Get the interests list container
    var interestsList = document.getElementById('interestsList');
  
    // Get all the interests elements
    var interestsElements = interestsList.getElementsByClassName('interest');
  
    // Initialize an empty array to store interests
    var interestsArray = [];
  
    // Loop through the interests elements and push their text content into the array
    for (var i = 0; i < interestsElements.length; i++) {
      interestsArray.push(interestsElements[i].innerText.trim());
    }
  
    // Convert the array of interests into a single string separated by commas
    var interestsString = interestsArray.join(', ');
  
    // Log the interests string to the console (you can remove this line if you don't need it)
    console.log('Interests submitted:', interestsString);
  
    // Here you can do whatever you want with the interests string, such as sending it to the server
  }
  

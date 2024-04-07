// Initialize allInterests array outside of the event listener
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
  
    // Make an HTTP POST request to the server running on port 5001
    //Run the below command in mac terminal for CORS error
    // open -na "Google Chrome" --args --disable-web-security --user-data-dir=/tmp/chrome_dev
    fetch('http://localhost:5001/interests', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin'   : 'http://localhost:5001'
        },
        body: JSON.stringify({ user_interest: interestsString, useremail: 'testuser123@gmail.com' })
    })
    .then(response => {
        console.log('its response')
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        console.log('Response from server:', data);
        // Handle the response from the server if needed
        recordId = JSON.parse(data).record_id;
        console.log('recordId',recordId)
        get_newsfeed(recordId);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}


function get_newsfeed(userId) {
    console.log('Here it is coming')
    // Make an HTTP GET request to the server running on port 5001
    fetch('http://localhost:5001/newsfeed?user_id='+userId, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:5001'
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
        });
    } 

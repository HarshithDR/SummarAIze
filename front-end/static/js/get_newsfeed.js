function get_newsfeed(userId) {
    // Make an HTTP GET request to the server running on port 5001
    fetch('http://localhost:5001/newsfeed'+userId, {
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
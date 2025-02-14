{/* <script> */}
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let query = document.getElementById("queryInput").value;

    fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })  // Send JSON instead of form-data
    })
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        if (data.results) {
            data.results.forEach(result => {
                let div = document.createElement("div");
                div.classList.add("result");
                div.innerHTML = `<a href="${result.link}" target="_blank">${result.title}</a>
                                 <p>${result.snippet}</p>`;
                resultsDiv.appendChild(div);
            });
        } else {
            resultsDiv.innerHTML = "<p>No results found.</p>";
        }
    })
    .catch(error => console.error("Error:", error));
});
// </script>

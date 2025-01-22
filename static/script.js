function getPrediction() {
    let experience = document.getElementById("experience").value;

    if (!experience) {
        alert("Please enter years of experience.");
        return;
    }

    fetch(`/predict?experience=${experience}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText =
                `Predicted Salary: $${data.predicted_salary}`;
        })
        .catch(error => console.error("Error:", error));
}
const analyzeButton = document.getElementById("analyzeButton");

analyzeButton.addEventListener("click", async () => {
    const text = document.getElementById("textInput").value;

    const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    const result = await response.json();

    document.getElementById("wordCount").textContent = result.word_count;
    document.getElementById("characterCount").textContent = result.character_count;
});
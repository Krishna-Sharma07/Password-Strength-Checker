const generateBtn = document.querySelector("button");
const lengthInput = document.getElementById("length");
const passwordField = document.getElementById("generated-password");
const copyBtn = document.getElementById("copy-btn");

generateBtn.addEventListener("click", async () => {
    const length = lengthInput.value;

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ length })
    });

    const data = await response.json();
    passwordField.value = data.password || "Error generating password";
});

copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(passwordField.value);
    alert("Password copied to clipboard!");
});

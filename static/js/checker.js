const passwordInput = document.getElementById("password");
const strengthLabel = document.getElementById("strength-label");

const rules = {
    length: document.getElementById("length"),
    uppercase: document.getElementById("uppercase"),
    lowercase: document.getElementById("lowercase"),
    digit: document.getElementById("digit"),
    symbol: document.getElementById("symbol")
};

passwordInput.addEventListener("input", async (e) => {
    const password = e.target.value;

    const response = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    for (let rule in data.rules) {
        if (data.rules[rule]) {
            rules[rule].classList.add("valid");
        } else {
            rules[rule].classList.remove("valid");
        }
    }

    strengthLabel.textContent = data.strength;
});

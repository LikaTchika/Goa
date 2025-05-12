let password = "Group 41 is best";
let attempts = 3;

function guessPassword() {
    while (attempts > 0) {
        let userInput = prompt("Enter the password:");
        
        if (userInput === password) {
            alert("Your entered password is correct.");
            break;
        } else {
            attempts--;
            if (attempts === 0) {
                alert("You have run out of attempts.");
            } else {
                alert("Incorrect password. You have " + attempts + " attempts left.");
            }
        }
    }
}

guessPassword();

function calculateFactorial(N) {
    let factorial = 1;
    for (let i = 1; i <= N; i++) {
        factorial *= i;
    }
    console.log("The factorial of " + N + " is: " + factorial);
}

calculateFactorial(5); // Example: N = 5

function countdown() {
    for (let i = 100; i >= 0; i--) {
        console.log("Remaining " + i + " seconds");
    }
}

countdown();
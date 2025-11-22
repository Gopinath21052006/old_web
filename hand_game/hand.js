const choices = ["rock", "paper", "scissor"];
const playerDisplay = document.getElementById("playerDisplay");
const computerDisplay = document.getElementById("computerDisplay");
const resultDisplay = document.getElementById("resultDisplay");
const PlayerScroreDisplay = document.getElementById("PlayerScroreDisplay");
const ComputerScroreDisplay = document.getElementById("ComputerScroreDisplay")
let PlayerScrore = 0
let ComputerScrore = 0

function playergame(playerchoice) {

    const computerchoice = choices[Math.floor(Math.random() * 3)];
    let result = "";
    if (playerchoice === computerchoice) {
        result = "IT'S A TIE!";
    } else {
        switch (playerchoice) {
            case 'rock':
                result = (computerchoice === "scissor") ? "YOU WIN" : "YOU LOSE!";
                break;
            case 'paper':
                result = (computerchoice === "rock") ? "YOU WIN" : "YOU LOSE!";
                break;
            case 'scissor':
                result = (computerchoice === "paper") ? "YOU WIN" : "YOU LOSE!";
                break;

        }
    }
    playerDisplay.textContent = `PLAYER: ${playerchoice}`;
    computerDisplay.textContent = `COMPUTER: ${computerchoice}`;
    resultDisplay.textContent = result;
    resultDisplay.classList.remove("greentext", "redtext")
    switch (result) {
        case "YOU WIN":
            resultDisplay.classList.add("greentext")
            PlayerScrore++;
            PlayerScroreDisplay.textContent = PlayerScrore
            break;
        case "YOU LOSE!":
            resultDisplay.classList.add("redtext")
            ComputerScrore++;
            ComputerScroreDisplay.textContent = ComputerScrore
            break;
    }
}
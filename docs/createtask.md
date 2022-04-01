{% include navigation.html %}

## Create Task Code Run-Time:

[Brian's Create Task](https://github.com/RohanG326/supporting_cast/wiki/Brian-Tang-Create-Task-Write-Up-and-Video)

[Runtime Video](https://www.loom.com/share/39ac2521c2224812976c08c03384f3f2)

[Code](https://github.com/RohanG326/supporting_cast/blob/main/createtask/templates/brian_divya_create_task.html)

```
function checkGameStatus() {
//if wrongGuess is 6 or higher, put "You lose" in gameResultText, display the selection div, hide the game div, and return
if (wrongGuess>=6){
    document.getElementById("gameResultText").innerText = "Game Over";
    document.getElementById("game").style.display="none";
    document.getElementById("selection").style.display="block";
    return;
}
//check whether every index of letterCheckArray is true
//if a single one is false, set indexCheck to false and break the loop
let indexCheck = true;
for (let i=0; i<letterCheckArray.length; i++){
    if (letterCheckArray[i]==false){
        indexCheck=false;
        break;
    }
}
//if every index of letterCheckArray is true, put "You win" in gameResultText, display the selection div, hide the game div, and return
if (indexCheck==true){
    document.getElementById("gameResultText").innerText = "You Win";
    document.getElementById("game").style.display="none";
    document.getElementById("selection").style.display="block";
    return;
}
}
```
```
function startGame (difficulty) {
document.getElementById("message").innerText = "";
//choose the array to select from based on difficulty
let arrayToChooseFrom;
if (difficulty==0){
    arrayToChooseFrom=fiveLetter;
}
else if (difficulty==1){
    arrayToChooseFrom=sevenLetter;
}
else if (difficulty==2){
    arrayToChooseFrom=nineLetter;
}
//select a word
word = arrayToChooseFrom[Math.floor(Math.random() * arrayToChooseFrom.length)];
//reset checkedLetters and wrongGuess
checkedLetters = [];
wrongGuess = 0;
//set letterCheckArray to an array length = word length filled with false, except spaces are true
letterCheckArray = [];
for (let i=0; i<word.length; i++){
    letterCheckArray.push(false);
}
//hide difficulty selection elements
document.getElementById("selection").style.display="none";
//show game elements
document.getElementById("game").style.display="block";
//if hard mode, reduce lives by 1
if (difficulty==2){
    guess(7);
}
//update display
displayWord();
}
```

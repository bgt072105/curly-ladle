{% include navigation.html %}

## Create Task Code Run-Time:

[Brian's Create Task](https://github.com/RohanG326/supporting_cast/wiki/Brian-Tang-Create-Task-Write-Up-and-Video)

[Runtime Video](https://www.loom.com/share/39ac2521c2224812976c08c03384f3f2)

[Code](https://github.com/RohanG326/supporting_cast/blob/main/createtask/templates/brian_divya_create_task.html)

## Questions

3a.

i. The purpose of this program is to act as a game where a user is meant to guess a random word. The user will guess one letter at a time until they either run out of guesses and lose the game or successfully complete the word and win the game.

ii. The video shows that there are three different difficulty levels for the user to choose from, with each difficulty level having words of varying lengths that correspond to the difficulty level. The video also shows the process of trying to guess a word along with what happens when you guess all the letters of the word successfully or when you run out of guesses.

iii. The input shown in the video are the letters that the user guesses in the game. The outputs shown in the video are the results of either guessing all the letters of a word successfully or running out of guesses.

3b.

i.

<img width="563" alt="Screen Shot 2022-02-27 at 11 48 07 PM" src="https://user-images.githubusercontent.com/89488588/155944409-13037825-0aa5-48eb-b7b6-995b72a62e1a.png">

ii.

<img width="861" alt="Screen Shot 2022-02-27 at 11 49 56 PM" src="https://user-images.githubusercontent.com/89488588/155944595-61d1ff93-3ce8-474f-98c2-5db7cd7159a1.png">

iii. The names of my lists are fiveLetter, sevenLetter, and nineLetter.

iv. The data contained in the lists represents words that the program can randomly choose to have the user guess in the hangman game. Each list stores a different set of words based on the length of the word. This allows the user to select three distinct difficulty levels to play on, each with their own unique word length.

v. The selected lists allow you to select a specific random piece of data out of a set of data. Without the use of lists, you could only select a nonrandom item, which defeats the purpose of the hangman game, which is to guess the letters in a random word. This allows us to manage complexity because it makes it easier to access one random piece of data. This way we do not have to hardcode all of the possible words into the program.

3c.

i. 

<img width="904" alt="Screen Shot 2022-02-27 at 11 51 42 PM" src="https://user-images.githubusercontent.com/89488588/155944849-c83d8182-6852-4b74-aa08-2bb6c3c4111c.png">

ii.

<img width="710" alt="Screen Shot 2022-02-27 at 11 52 28 PM" src="https://user-images.githubusercontent.com/89488588/155944940-4ab0b709-0b2c-4219-902d-b4f83c433fcc.png">

iii. The identified procedure, guess, checks whether or not the letter that the user guessed is a part of the word. If the letter is not a part of the word, the hangman has a limb added to it and the user is informed that the letter they guessed is not in the word. If the letter is a part of the word, all instances of that letter in the word are filled into the template for the word. This contributes to the overall functionality of the program because without this procedure, there would be no way to check whether or not a letter that the user has guessed appears in the word that they are meant to be guessing.

iv. The first step of the procedure is to make sure that the input is valid. Nonvalid inputs would be blank inputs, inputs that have already been guessed, and inputs consisting of multiple letters. Then we iterate over the word to mark all instances of the letter. If there are no instances of the letter, increase the wrong guess count. The procedure also adds the guessed letter to the checked letters. Then, the procedure executes the program's next steps of updating the game’s status and display.

3d.

i. The first call is when you click the guess button. This action inputs the user’s guess and allows for the guess to be checked.

The second call is when you start the game on the hard difficulty level. If the user starts the game on the hard difficulty level, the guess function is used to give the user one less life compared to other difficulty levels by automatically guessing something that can’t be a part of the word the user is meant to be guessing.

ii. The first call tests a user’s input and determines whether that input appears in the word that the user is meant to be guessing.

The second call tests an intentionally wrong guess to make sure that it is not in the word, thus artificially lowering the amount of lives the user has in the hard difficulty by one life.

iii. The result of the first call is whether or not the user’s guess appears in the word that they are meant to be guessing.

The result of the second call is artificially lowering the amount of lives the user has in the hard difficulty by one life by forcing an intentionally incorrect guess.


```
function checkGameStatus() 
{
//if wrongGuess is 6 or higher, put "You lose" in gameResultText, display the selection div, hide the game div, and return
if (wrongGuess>=6)
{
    document.getElementById("gameResultText").innerText = "Game Over";
    document.getElementById("game").style.display="none";
    document.getElementById("selection").style.display="block";
    return;
}
//check whether every index of letterCheckArray is true
//if a single one is false, set indexCheck to false and break the loop
let indexCheck = true;
for (let i=0; i<letterCheckArray.length; i++)
{
    if (letterCheckArray[i]==false)
    {
        indexCheck=false;
        break;
    }
}
//if every index of letterCheckArray is true, put "You win" in gameResultText, display the selection div, hide the game div, and return
if (indexCheck==true)
{
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
if (difficulty==0)
{
    arrayToChooseFrom=fiveLetter;
}
else if (difficulty==1)
{
    arrayToChooseFrom=sevenLetter;
}
else if (difficulty==2)
{
    arrayToChooseFrom=nineLetter;
}
//select a word
word = arrayToChooseFrom[Math.floor(Math.random() * arrayToChooseFrom.length)];
//reset checkedLetters and wrongGuess
checkedLetters = [];
wrongGuess = 0;
//set letterCheckArray to an array length = word length filled with false, except spaces are true
letterCheckArray = [];
for (let i=0; i<word.length; i++)
{
    letterCheckArray.push(false);
}
//hide difficulty selection elements
document.getElementById("selection").style.display="none";
//show game elements
document.getElementById("game").style.display="block";
//if hard mode, reduce lives by 1
if (difficulty==2)
{
    guess(7);
}
//update display
displayWord();
}
```

//Parker Lowney
const prompt = require("prompt-sync")(); //For user input

/**
 * Returns true if input is a letter (regex is hard :( )
 */
function isLetter(c){
    let v = c.charCodeAt(); //ASCII value of given character
    if ((65 <= v && v <= 90) || (97 <= v && v <= 122)){
        return true;
    } else {
        return false;
    }
}

/**
 * Encodes a given string
 */
function encode(s){
    vals = s.split(" ");
    const output = [];

    //Loop through all the words
    for (word of vals){

        let w = ""; //Stores the new values for this word
        for (l of word){ //Loops through the letters of each word
            
            if (isLetter(l)){ //Char is ignored if it isn't a letter

                let v = l.charCodeAt(); //Get ASCII value of letter
                v += word.length % 26; //Add the length of word to character mod 26 to account for being more than 26 characters off

                //Check for overruns
                if (!isLetter(String.fromCharCode(v)) || (l == l.toUpperCase() && v >= 90)){ //If isn't letter
                    v -= 26 //- (v - 90 - (32 * Math.floor(v / 100))) //Subract the alphabet (minus one) plus how far over it is
                } 

                w = w + String.fromCharCode(v); //Add our new char to output array
            } else { //If not a letter it just carries over
                w = w + l
            }
        }
        output.push(w)
    }

    return output.join(" ");

}

/**
 * Decodes a given string
 */
 function decode(s){
    vals = s.split(" ");
    const output = [];

    //Loop through all the words
    for (word of vals){

        let w = ""; //Stores the new values for this word
        for (l of word){ //Loops through the letters of each word
            
            if (isLetter(l)){ //Char is ignored if it isn't a letter

                let v = l.charCodeAt(); //Get ASCII value of letter
                v -= word.length % 26; //Add the length of word to character mod 26 to account for being more than 26 characters off

                //Check for overruns
                if (!isLetter(String.fromCharCode(v)) || (l == l.toLowerCase() && v <= 90)){ //If isn't letter
                    v += 26 //- (v - 90 - (32 * Math.floor(v / 100))) //Subract the alphabet (minus one) plus how far over it is
                } 

                w = w + String.fromCharCode(v); //Add our new char to output array
            } else { //If not a letter it just carries over
                w = w + l
            }
        }
        output.push(w)
    }

    return output.join(" ");

}


/**
 * Main function
 */
function main(){
    let welcome = "Welcome to pCypher! Input a phrase to be encrypted, or start it with \"//\" to decode instead.";

    console.log(welcome)

    //Input loop
    while (true){

        console.log("Enter a string:");
        
        //Take user input
        let input = String(prompt())

        if (input == "quit" || input == "stop" || input == "exit"){
            console.log("Exiting..."); //Exit message
            break
        }

        //Chooses which operation to perform
        if (!input.startsWith("//")){
            console.log(encode(input));

        } else {
            
            console.log(decode(input.slice(2, input.length)));
        }
    }
}

main()
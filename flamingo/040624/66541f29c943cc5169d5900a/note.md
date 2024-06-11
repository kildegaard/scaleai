
# Prompt

I'm a beginner in dynamic programming in JavaScript, so I need inline comments for this code.
```
const readlineSync = require('readline-sync');

function max_powered_rooms(M, N, K, F, correct_wirings) {
    let dp = new Array(M + 1);
    for (let i = 0; i <= M; i++) {
        dp[i] = new Array(F + 1);
        for (let j = 0; j <= F; j++) {
            dp[i][j] = new Array(K + 1).fill(0);
        }
    }

    for (let i = 1; i <= M; i++) {
        for (let j = 0; j <= F; j++) {
            for (let k = 0; k <= K; k++) {
                if (k > i || j > i) continue; 
                let activated = correct_wirings[i - 1] + dp[i - 1][j][k];
                let deactivated = (N - correct_wirings[i - 1]) + (k > 0 && j > 0 ? dp[i - 1][j - 1][k - 1] : 0);
                
                dp[i][j][k] = Math.max(activated, deactivated);
            }
        }
    }

    return dp[M][F][K];
}

function getInput() {
    let M = parseInt(readlineSync.question("Enter the number of floors: "));
    let N = parseInt(readlineSync.question("Enter the number of rooms per floor: "));
    let K = parseInt(readlineSync.question("Enter the exact number of master switches to be deactivated: "));
    let F = parseInt(readlineSync.question("Enter the maximum number of floors that can be left without power completely: "));

    let correct_wirings = [];
    for (let i = 0; i < M; i++) {
        let wiring = parseInt(readlineSync.question(`Enter the number of correctly wired rooms on floor ${i + 1}: `));
        correct_wirings.push(wiring);
    }

    return { M, N, K, F, correct_wirings };
}

function main() {
    const { M, N, K, F, correct_wirings } = getInput();
    console.log(max_powered_rooms(M, N, K, F, correct_wirings));
}

main();



```


# justif orig

Both responses provide inline comments explaining the purpose of each part of the code.
Response 2 provides a bit more clarity in terms of the logic within the loops. Therefore, response 2 could be considered slightly better for someone who is a beginner and needs more detailed explanations.
Note: I used this link for testing the code:
https://www.programiz.com/javascript/online-compiler/
and it works on it without error against the model's responses.

# justif modif

Both responses provide inline comments explaining the purpose of each part of the code. They correctly answered the prompt with no issues, and the code ran flawlessly. Response 2 provides a bit more clarity in terms of the logic within the loops. Therefore, response 2 could be considered slightly better for someone who is a beginner and needs more detailed explanations.

# Feedback

Dear Contributor, your task was very good up to the first turn. Your first prompt is fine (could have more non-code details which will increase its quality) and your justification passes the actual guidelines (could also improve in the testing area mentioning how you did it showing examples of that).
However, your second prompt has a major issue because it is like starting right from the beginning. You pasted the initial code without comments, which was the first prompt idea.
You will need to redo this attempt from this point onward, considering that you must engage in a continued conversation with the LLM, you can't cut the conducting line just like that.

I will share with you some insights about prompting and justification writing that may come in handy!

 Prompts need to have a certain structure considering the following:
- Context: giving some environmental information will buff your prompt as the model has information to be more specific and clever.
- Clear objectives: well-explained goals for the code or problem to achieve.
- Use cases: propose uses for the code to be useful within specific situations
- Constraints: adding extra spice to the model is a good way to increase its quality. Think about specific limitations to take into account or restrictions that would make the problem non-trivial.
- Uniqueness: as stated previously, your problem must provide some fresh ideas to the prompt pool. It's expected for you to write problems that are not so easily found on the internet.
- Complexity: Once again, as stated before, the problem must not be trivial. It would be best if you aimed for issues that require some effort for the model, that provide a clear yet not easy way for solving them.

Another topic to engage in is justifications: in the documentation, there's plenty of information to learn some workflow to tackle this. I'll add them at the end for you to later consults.
Your justification also lacks development in it. Some things can be done to improve it further. For example, it is important to show evidence in the responses to support your response selection. You must also claim where's the deviation (in case there is), or analyze why there is not.

Another thing that is of extreme importance is to test your code factually (as stated before). Not only test it, but show some evidence that you did, and share the environment set for this. It's important because if the reviewer can not rut it, or if it's too complicated and time-consuming to set the correct environment, then your task is most probably going to be sent back to you. Please consider this!

Keynote for future justifications: I will show you a systematic way of building excellent-quality justifications.

Comparison between responses + Along which dimension? + Epic quality justification + Evidence for taking the aforementioned decision.
Also, you must explain and demonstrate HOW did you test the code, and how (briefly describe the environment). Extra points if you can define how to fix issues (if any).
If you follow these instructions, you will almost always be rated 4 or 5.


With all this, I truly believe you can develop perfect stellar prompts that would make the model thrive to create astonishing responses.

Thanks a lot for reading till the end! I wish you the best on this, I know you have what is needed for the project!

* Documentation:

* Flamingo Crash Course:
https://docs.google.com/document/d/1djY7NcldjU21bRYCX6hoFHrrQSPQ5C_o0d_XDJnNUmY/edit#heading=h.3ibr2go7c4fs

* Dimension Priorities:
https://docs.google.com/document/d/1XtlJbL3WuvMBqKvqSmRHVCujy_fvDrluiKOzR5I0qO4/edit

# Nota
2
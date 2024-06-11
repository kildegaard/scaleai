# Prompt

Can you code a basic Javascript to-do list application where users can add and remove tasks? I want a bulleted list feature in this application, where there are checkboxes next to each to-do list item, and when a box is checked, the corresponding item gets crossed out. Implement a search feature to find tasks. I also want to be able to set a due date for each task, and add a filter feature to the application to filter by soonest due date to find the highest priority tasks.

# justif original

Response 1 and Response 2 have identical code functionality, so in function they are identical. In terms of explanation, Response 1 offers an explanation in the second to last paragraph of how to use the application, which makes the code easier to follow than Response 2 if the user is not as technically familiar with Javascript.
Response 1 and Response 2 both offer a separation of the HTML and Javascript code blocks, which allows for ease of readability. Response 2 offers greater detail in the list of bullet points that explain features of the application - for example, it says "Users can add tasks with due dates using the form" as opposed to the first bullet point of Response 1 just saying "Add tasks with due dates", which is more ambiguous and harder to understand.
Both responses lack an explanation of how to run the code, which should be added. Overall, Response 1 might have a few better features including syntax highlighting of code blocks, and better explanations, but overall it is not much stronger than Response 2.
In terms of testing, neither Responses contain code blocks that compile and run, as it does not work for the Nodejs workspace IDE.

# Justif modif

Response 1 and Response 2 have identical code functionality, so in function they are identical. In terms of explanation, Response 1 offers an explanation in the second to last paragraph of how to use the application, which makes the code easier to follow than Response 2 if the user is not as technically familiar with Javascript.
Response 1 and Response 2 both offer a separation of the HTML and Javascript code blocks, which allows for ease of readability. Response 2 offers greater detail in the list of bullet points that explain features of the application - for example, it says "Users can add tasks with due dates using the form" as opposed to the first bullet point of Response 1 just saying "Add tasks with due dates", which is more ambiguous and harder to understand.
Both responses lack an explanation of how to run the code, which should be added. Overall, Response 1 might have a few better features including syntax highlighting of code blocks, and better explanations, but overall it is not much stronger than Response 2.
In terms of testing, both responses work fine without issues. For this, I used a Visual Studio Code environment and created two files, one for each part of the code: index.html and script.js.
After that, I used the Live Server extension to create a local server and test it on Google Chrome. Both codes ran smoothly and provided no errors whatsoever.


# Feedback

Dear Contributor, very good task! Both your prompt and your justification are great in terms of actual guidelines. They excel above the mean tasks in both good content and correct structure.
Minor things can be done to increase even further both ranks. I will share with you some good practices in prompting and justification writing.

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
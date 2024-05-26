# Prompt 1

I am  working for a company that receives disorganized product id with disorganized product names and SKUs (Stock Keeping Units). I need you to create a Python code that matches each product name with its corresponding SKU.
generate  python code to make the following :

**Normalize product names and SKUs by:

- Removing extra spaces.
- Converting all characters to lowercase.

** Generate possible SKUs for each product name based on different patterns:
- Using the first three letters of the product name if the name contains one word, followed by the sum of the product ID digits.
- Using the first letter of each word in the product name if the name contains two words, followed by the multiplication of the product ID digits.

** For products with a three-word name, also consider:
Use the first letter of the first word, the first letter of the second word, and the full last word, followed by the product ID.


# Justif 1 original

Both responses give correct answers, I have tested the two codes locally on VS code, but response 2 in line 1, defines separated functions for the normalization process, which makes the code easier to read, in line 7 response 2, the generating SKUs process is in a separated function, which makes the process for adding another SKUs pattern easier, all we need is to modify the function only, no need to change all the part s of the response.


%%%%%%%%%%%%%%%


# Feedback

Hello, dear Tasker. Thanks a lot for your commitment to the actual project.
I reviewed your work and wanted to share my thoughts.

I liked your prompts very much! First prompt hit almost every intended spot for it to be outstanding. Your second prompt was good enough considering it a follow-up one, but lacked some important things. I'll share below some key lines to consider for further prompts that will come In handy!

* Prompts
Prompts need to have a certain structure considering the following:
- Context: giving some environmental information will buff your prompt as the model has information to be more specific and clever.
- Clear objectives: well-explained goals for the code or problem to achieve.
- Use cases: propose uses for the code to be useful within specific situations
- Constraints: adding extra spice to the model is a good way to increase its quality. Think about specific limitations to take into account or restrictions that would make the problem non-trivial.
- Uniqueness: as stated previously, your problem must provide some fresh ideas to the prompt pool. It's expected for you to write problems that are not so easily found on the internet.
- Complexity: Once again, as stated before, the problem must not be trivial. It would be best if you aimed for issues that require some effort for the model, that provide a clear yet not easy way for solving them.

* Justifications
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
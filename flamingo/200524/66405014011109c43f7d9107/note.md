# Prompts

Can you create a Python function that will accept a URL for a CSV file that will do the following:
1. Validate the format by checking the headings against a predefined list of headings, they also have to be in a fixed order
2. There are certain fields that should be non-null, these are also available as a global constant
3. The function then needs to check for duplicate entries, here duplicate means that two rows will have the same values
4. If there are duplicate entries, they must be added to a separate pandas object as a single entry with a new column called "duplicate_count" that will have the number of times said entry was in the original CSV file.
5. If checks for 1, 2 and 3 are passed then return a tuple with the first item as "PASSED" and the second item should be a pandas object of the initial file. If it fails due to 1, return a tuple where the first item is "Malformed File" and the second item is null. If it fails due to 2, return a tuple where the first item is "Null Constraint not met" and the second is null. If it fails due to 3, return a tuple where the first item is "Duplicates exist" and the second item is the pandas object created in 4.


We need to modify the function so that instead of a URL it will accept the CSV as it would come in a REST API as form data. Can you also show an example of how we would pass that data from a POST request to the function in flask?


I need you to write data from the checked pandas object to a DB. The function needs to:
1. Validate the rows for SQL injection attacks and other security concerns. 
2. Restrict it to a single update query to the database to reduce the writes to the DB.
3. When writing the query leave the table name with a template that I can fill in later.
4. The columns for the values are the headings in the csv file in camel case


# Justificacion 1 original

Response 2 is better than Response 1. Response 2 was styled and formatted better than Response 1, as it had comments all along the code explaining what each section is. Response 1 also had comments but they were limited to only the conditions described in the prompt, while Response 2 explained the solution it used. Response 1 had an overall error wrapper that would catch any error in the code but it would only give a general error while Response 2 provided a more specific error handling mechanism around the web fetch.


# Feedback

Dear tasker, your attempt is very good! However, in the first prompt justification you chose the wrong response along an incorrect dimension. Your choice was of formatting, whereas the main problem was that the code did not compile due to a ValueError (in the duplicate_count method).
Your justifications were good but can be improved to upgrade the quality of the task.

I will give you some pieces of advice about these subjects and also provide you with the official documentation that may come in handy.

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

* Flamingo Crash Course [ONLY OFFICIAL DOCUMENTATION]:
https://docs.google.com/document/d/1djY7NcldjU21bRYCX6hoFHrrQSPQ5C_o0d_XDJnNUmY/edit#heading=h.3ibr2go7c4fs

* Dimension Priorities:
https://docs.google.com/document/d/1XtlJbL3WuvMBqKvqSmRHVCujy_fvDrluiKOzR5I0qO4/edit
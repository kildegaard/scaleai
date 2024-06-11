Attempter: 

# Prompt

I have users' data in my database consisting of names, email, country, and phone numbers and I want to assign phone codes. Write a function that takes a country name as an argument and returns the phone number code (For example, for India as input, 91 should be output). Please throw an error for invalid inputs. You can use any library like 'phonenumbers' to support and fetch outputs.

# justif original

Response 1 is clearly better than Response 2 in terms of functionality and performance. Response 1 returns a correct response mentioning the phone code for the given Country using 'phonenumbers' library. Whereas, Response 2 failed to utilize the library and threw an error as it incorrectly used a function that doesn't exist (UnknownRegionErros). Response 2 failed to give a correct output and also failed to throw an error appropriately. Response 1 adheres to the prompt completely matches the requirements and also handles errors efficiently.


# justif modif

Response 1 is better than response 2 along the Functionality & Performance dimension.

Response 1 returns a correct response mentioning the phone code for the given Country using `phonenumbers` library. The thing with this response is that the country must be hardcoded into a dictionary for it to work correctly.

On the other hand, Response 2 failed to utilize the library and threw an error as it incorrectly used a method that doesn't exist (UnknownRegionError). Because of this 
Response 2 failed to give a correct output and also failed to throw an error appropriately. This error can be solved using other libraries known in the Python ecosystem.

Response 1 adheres to the prompt completely, matches the requirements, and also handles errors efficiently.

Both codes were tested using Visual Studio Code in a local environment.
The codes could improve a lot by using the `pycountry` library. It associates a country's name with its nomenclature. When used along with `phonenumbers`, you can create a full-fledged application with all the country names already loaded.


# Feedback

Dear Attempter, Your task was good despite some issues that I will now discuss.
Your prompt is a bit too simple. It barely reaches the minimum required level of aproveness. I would suggest increasing its complexity by adding some constraints or by creating a use case with more context.
On the other hand, your justification is good too but lacked some structure that would make it improve its quality. I will share some insights for this as well as the documentation for future tasks. Good work!

Prompts need to have a certain structure considering the following:
- Context: giving some environmental information will buff your prompt as the model has information to be more specific and clever.
- Clear objectives: well-explained goals for the code or problem to achieve.
- Use cases: propose uses for the code to be useful within specific situations
- Constraints: adding extra spice to the model is a good way to increase its quality. Think about specific limitations to take into account or restrictions that would make the problem non-trivial.
- Uniqueness: as stated previously, your problem must provide some fresh ideas to the prompt pool. It's expected for you to write problems that are not so easily found on the internet.
- Complexity: Once again, as stated before, the problem must not be trivial. It would be best if you aimed for issues that require some effort for the model, that provide a clear yet not easy way for solving them.

Another topic to engage in is justifications: in the documentation, there's plenty of information to learn some workflow to tackle this. I'll add them at the end for you to later consults.

Yet another thing that is of extreme importance is to test your code factually (as stated before). Not only test it, but show some evidence that you did, and share the environment set for this. It's important because if the reviewer can not rut it, or if it's too complicated and time-consuming to set the correct environment, then your task is most probably going to be sent back to you. Please consider this!

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
# Prompt 1

I am building a project in JavaScript for a school to connect teachers with parents. I need a function for adding a new student to a teacher. The function should take a student object, a teacher name, and the array of teachers. The student object should consist of first name, last name, age, and parent name. The teacher object should be first name, last name, room number, and students array which will consist of student objects. It should add the student to the teachers student array.

# Justif 1 original

PUNTUACION: 7

Response 2 is better than Response 1 -

Style & Formatting:
- Response 1's code blocks are not in the proper JavaScript markdown, which makes it harder to read. In contrast, Response 2's code blocks are in the correct markdown.
- Response 1 also uses multiple code snippets, having the example usage in a separate code snippet. In contrast, Response 2 includes the example usage in the same code snippet as the function, making it easier to test before using.

# Justif 1 modificada

In this case, response 1 and response 2 are very similar. They both fully adapt to the prompt's requirements, so no deviation is found.
Despite this, they are a bit different in structure. Response 2 creates all things needed in just one code block whereas response 1 separates them into three. In my personal opinion, I prefer the first option due to its testability: it's easier to test just one block of code. Also, it's labeled as a "JavaScript" markdown whereas response 1 is plain text.
For this, response 2 is just a little bit better than response 1. I have tested the codes using Node in my Windows Terminal.

# Prompt 2

Modify the function to ensure the student and teacherName parameters are the correct datatype. Also, ensure the student object has the appropriate properties.

# Justif 2 original
Response 1 is better than Response 2 because the error handling in Response 2 does not fully ensure that the student parameter is an object.

Functionality & Performance:
Response 2 only checks if the type of the student parameter is object. However, arrays also return a type of object. In contrast, Response 1 checks the type, but also includes a check if it is an array.

# Justif 2 modificada
Response 1 is hardly better than response 2 because, despite having different codes they do almost the same. Response 1 has a bit more stylistic code but essentially is the same as response 2's code.
I have tested both codes in Visual Studio Code.

# Feedback

Hello dear Tasker! Nice job with this task. I have made a few minor modifications to the justification, mainly grammar issues. The overall performance is very good!

I'll leave some considerations so you can better improve future attempts.

# Prompts
Prompts need to have a certain structure considering the following:
- Context: giving some environmental information will buff your prompt as the model has information to be more specific and clever.
- Clear objectives: well-explained goals for the code or problem to achieve.
- Use cases: propose uses for the code to be useful within specific situations
- Constraints: adding extra spice to the model is a good way to increase its quality. Think about specific limitations to take into account or restrictions that would make the problem non-trivial.
- Uniqueness: as stated previously, your problem must provide some fresh ideas to the prompt pool. It's expected for you to write problems that are not so easily found on the internet.
- Complexity: Once again, as stated before, the problem must not be trivial. It would be best if you aimed for issues that require some effort for the model, that provide a clear yet not easy way for solving them.

# Justifications
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
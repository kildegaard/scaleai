# Prompt 1

I have an inventory of multiply items, and I have a lot of inventory managers that keep track of what goes in the inventory and out of the inventory. Thus making it difficult to keep track of the changes in the inventory.

I want you to build me a Python backend to solve this issue. The code must implement the following:

1. Exposes an endpoint to register an item, the user should send the name of the item, the quantity of the item, and the name of the user making the change.

2. Exposes an endpoint to take items out of the inventory, the user should send the name of the item, how many items the user wants to take out, and the name of the user making the change.

3. Exposes an endpoint that will return the entire list of changes for a specific user.

You should take the following constraints into consideration:

1. If a user is trying to add an item to the inventory that already exists, the count should increase; if a user is trying to take an item that doesn't exist in the inventory or is trying to take more than the available count, the operation should be rejected; otherwise, the count will be decreased.

2. All the data saving should be done in memory.

3. A record file of all the operations should be created and updated when any successful operation is done.

4. When the system starts, it should read the record file and restore the state of the system before shutting down.

5. The data in the record file should contain the name of the item, the count, the operation adding to the inventory or taking out of the inventory, and the name of the user who did the operation.

# Justif original


Response 1 and 2 share a lot of similarities in the code explanation and formatting except the following where response 1 is better than response 2:

1. Response 1 used a JSON file to store the record which is better than a normal text file because it's easier to do operations on and it provides the ability to easy integrate the data with a database.

2. Response 1 has a better formatting sense the code is colored.


To test the code I recommend running the code in your local environment, just run the Python code and use any API testing program like Postman and test each endpoint.

I have tested the code in my local environment and the code fully works with all the correct functionalities present. This apply for both of the responses.


# Justificacion modificada

Response 1 is slightly better than response 2, despite no deviation being found.

Responses 1 and 2 share a lot of similarities in the code explanation and formatting.
In spite of their similarities, Response 1 used a JSON file to store the record which is better than a normal text file because it's easier to do operations on and it provides the ability to easily integrate the data with a database. 

To test the code I recommend running the code in your local environment, just run the Python code and use any API testing program like Postman and test each endpoint.

I have tested the code in my local environment and the code fully works with all the correct functionalities present. This applies to both of the responses.


# Feedback

Hi dear tasker, good job on your attempt!
Your prompts were very good, as well as your justifications. There are some things that can be improved in order to increase its quality to the next level.

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
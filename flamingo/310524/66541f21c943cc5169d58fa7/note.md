# Prompts
I have confused the global variables and the local ones. Please help me to debug the following code by clarifying their difference:

import numpy as np

def complex_data_analysis(data):
    global total_data
    total_data = {'total_sum': 0, 'counts': []}
    
    for x in range(len(data)):
        local_sum = 0
        total_intermediate_sum = 0
        for y in range(len(data[x])):
            intermediate_sum = 0
            for z in range(data[x][y]):
                local_sum += data[x][y]
                intermediate_sum += data[x][y]
                for _ in range(data[x][y]):
                    if x % 2 == 0:
                        total_data['total_sum'] += intermediate_sum * z
                    else:
                        total_data['total_sum'] -= intermediate_sum * z
                    total_data['counts'].append(intermediate_sum)
       
            total_intermediate_sum += intermediate_sum
            local_sum -= intermediate_sum  # Confusing update to local_sum

        total_data['total_sum'] += total_intermediate_sum
        total_data['counts'].extend([total_intermediate_sum] * (x + 1))
    
    return total_data['total_sum']


Use the debugging tip 1 to start debugging the code step-by-step. Meanwhile, remove the "local_sum -= intermediate_sum" statement since it is a confusing update to local_sum.


Perform the third debugging tip by breaking the code into smaller functions, making it easier to debug.


# Justifs
Response 2 is better than Response 1 because it offers debugging tips about the prompt and addresses the clarification about the global and local variables in the bugged code. In contrast, response 1 provides the "corrected" code by refactoring the code, but it simplifies the logic in the prompts and removes the nested loops. 

Response 1's refactored version is tested but does not match the output of the original function, while Response 1 offers tips about how to debug the given code.

Overall, response 2 is better than response 1, given that it addresses all the requirements in the prompt. 



Both responses all meet the prompt requirements and print out the values for debugging as suggested in tip 1. 



Response 1 is slightly better than Response 2 because it divides the code into more granular functions by including the process_outer_loop (line 24). However, both responses do not generate identical results to the original code in turn 2 using the same test case.


# Feedback
Dear Contributor, thanks for your contributions. However, your prompt does not align with the actual Guidelines. Its nature is too simple and the code to debug seems forced. The idea is to use real-life code with organic bugs or issues. This way, the Model has good material to work with and increases its capabilities.
On the other hand, your justifications are a bit too vague, you need to expand your claims about the differences found between both responses and support them with evidence.
I will share with you some insights about both prompts and justifications that will come in handy, as well as the official updated documentation.

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
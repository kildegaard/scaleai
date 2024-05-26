# Prompt 1

I am developing a Python application that needs to manage multiple network connections concurrently. 
1. I need a function that accepts a list of URLs and downloads the content of each of them using the 'asyncio' and 'aiohttp' modules. 
2. The function should handle exceptions appropriately and return a dictionary where the keys are the URLs and the values are the downloaded content or the error if the download failed. 
3. Additionally, the time for each request must be 10 seconds. Make sure the feature does not download content from URLs that contain the word "forbidden" in their domain.
4. Provide the following test scenarios:
- A list of valid and accessible URLs.
- A list of URLs that include a mix of valid URLs and URLs with domains containing the word "forbidden".
- A list of URLs where some take more than 10 seconds to respond.
- An empty list of URLs.
Provide well-documented code and explain each step of the process, including the implementation of the test cases and expected results.

# Justif 1 original

Response 2 is slightly better than Response 1.  Although both responses address all aspects of the task and cover all required testing scenarios, Response 2 uses 'asyncio.run' and voids the unnecessary use of 'asyncio.coroutine' in Response 1 (line 15), which reduces complexity and improves the readability of the code by making it clearer and using modern techniques. 
Both responses failed to detail the necessary installation of the 'aiohttps' modeule.

# Justif 1 modif

Response 2 is slightly better than Response 1.  Although both responses address all aspects of the task and cover all required testing scenarios, Response 2 uses 'asyncio.run' and voids the unnecessary use of 'asyncio.coroutine' in Response 1 (line 15), which reduces complexity and improves the readability of the code by making it clearer and using modern techniques.
Also, both responses hallucinate some URLs (there is not an example.com/ website online)
There's not an explicit deviation in this case, and both codes were locally tested within a VSCode environment using venv.


# Prompt 2

Now let's add new conditions:
1. The function must allow a maximum number of simultaneous connections configured through a parameter.
2. Implement an option to save downloaded content as individual files in a specific folder, where each file must be named according to the domain of the URL.
3. Provide test cases that verify these new functionalities, including the following:
- A list of valid and accessible URLs with the simultaneous connection limit set to 2.
- Verification that content is saved correctly in files with appropriate names.
- Exception handling when the specified directory does not exist.

Make sure to include the installation of all necessary modules.


# Justif 2 orig

Le puso 8 de ranking

Response 2 is much better than Response 1 in terms of Functionality & Performance. Response 2 uses 'aiohttp.TCPConnector' (line 28) to limit simultaneous connections more efficiently and directly than using 'asyncio.Semaphore' (line20) in Response 1. Also, Response 2 uses 'pathlib' (line17) to manage files path, which improves the modernity of the code compared to the use of 'aiofiles' (line 29) in Response 1. 
Therefore, Response 2 demonstrates a superior use of modern programming techniques and best practices.

# Justif 2 modif

Se lo bajo a 6

Despite being response 2 better in terms of modern programming than response 1, I consider there is not a deviation in this situation.
R2 uses 'aiohttp.TCPConnector' in line 28 to limit the simultaneous connections in a more efficient way than R1, that uses 'asyncio.Semaphore (line 20).
Also, R2 uses 'pathlib' (line 17) to manage file paths which improves the quality and readability of the code, rather than 'aiofiles' (line 29) in R1.


# Prompt 3

Now, we are going to add a new function that should allow you to filter the URLs to download only those contents that contain certain words specified by the user.
1. Provide test cases that verify these new features, including the following:
- Verification that only the contents of URLs that contain the words specified in their HTML are downloaded.
- Handling cases where none of the URLs contain the specified words.
- Confirmation that leaked content is correctly saved in files with appropriate names.

# Justif 3 original

Response 1 is better than Response 2 in terms of Functionality & Performance. Response 1 implements word filtering more directly and efficiently line 14 checks that all words are present in the content before saving, reducing unnecessary processing. In Response 2, filtering is done after downloading in the main task block, which may result in additional and less clear processing.

# Justif 3 modif

Se lo cambio a 3

Response 1 is slightly better than response 2. Despite no deviation in this step, the difference between both responses would be along the Functionality & Performance dimension.
R1 implements word filtering more directly and efficiently than R2. In line 14, it checks that all the words are present in the content before saving. On the other hand, R2 does this after download is complete, resulting in additional processing.


# Feedback

You rated turn 2 with an 8 and turn 3 with a 2, in both cases along the Functionality & Performance dimension. I disagree with this decision because, according to actual guidelines, the difference between them (hence, the deviation) must be concerning the prompts: it is only considered a deviation when one response does not provide what was asked in the prompt. If it executes it less efficiently, you can rank it accordingly but not submit it as a deviation.

Apart from that, your prompts were very good! Keep up the good work.

To continue improving your prompts and justifications, I would suggest rereading the documentation that has been updated. I'll leave the URLs below.

* Documentation:

* Flamingo Crash Course:
https://docs.google.com/document/d/1djY7NcldjU21bRYCX6hoFHrrQSPQ5C_o0d_XDJnNUmY/edit#heading=h.3ibr2go7c4fs

* Dimension Priorities:
https://docs.google.com/document/d/1XtlJbL3WuvMBqKvqSmRHVCujy_fvDrluiKOzR5I0qO4/edit
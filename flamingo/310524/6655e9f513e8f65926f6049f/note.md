Attempter:

# Prompt 1

You are tasked to fix a bug in JavaScript code which takes a dataset of fruits and their quantities, and calculates the mean, median and standard deviation of the entire quantity column. Return the code with the fixed bug so the summary statistics mentioned above can be returned.

Code:

// Data structure with fruits and their quantities
const fruitData = [
    { fruit: "Apple", quantity: 10 },
    { fruit: "Banana", quantity: 15 },
    { fruit: "Cherry", quantity: 8 },
    { fruit: "Date", quantity: 12 },
    { fruit: "Elderberry", quantity: 7 }
  ];
  
  // Function to calculate the mean
  function calculateMean(data) {
    const sum = data.reduce(acc, curr => acc + curr.quantity, 0);
    return sum / data.length;
  }
  
  // Function to calculate the median
  function calculateMedian(data) {
    const quantities = data.map(item => item.quantity).sort((a, b) => a - b);
    const mid = Math.floor(quantities.length / 2);
    return quantities.length % 2 !== 0 ? quantities[mid] : (quantities[mid - 1] + quantities[mid]) / 2;
  }
  
  // Function to calculate the standard deviation
  function calculateStd(data) {
    const mean = calculateMean(data);
    const variance = data.reduce((acc, curr) => acc + Math.pow(curr.quantity - mean, 2), 0) / data.length;
    return Math.sqrt(variance);
  }
  
  // Aggregating the statistics
  const mean = calculateMean(fruitData);
  const median = calculateMedian(fruitData);
  const std = calculateStd(fruitData);
  
  console.log(`Mean: ${mean}`);
  console.log(`Median: ${median}`);
  console.log(`Standard Deviation: ${std}`);
  


# Justif 1 orig

Response 2 is slightly better than Response 1 because it provides the explanation of the bug as a friendly introduction to the user before providing the code with the fixed bug. Response 1 on the other hand provides the corrected code however without the introduction of what is actually changed. Introducing to the user the issue of the code before providing it as evidenced in response 2 is fulfills the prompt in a better way because it directly provides the bug location and how it is solved and allows for less time to be spent on debugging from the user perspective.

# Justif 1 modif

Response 2 is slightly better than Response 1 because it provides an explanation of the bug as a friendly introduction to the user before providing the code with the fixed bug.
Response 1 on the other hand provides the corrected code but without the introduction of what is actually changed. Introducing to the user the issue of the code before providing it as evidenced in response 2 fulfills the prompt in a better way because it directly provides the bug location and how it is solved and allows for less time to be spent on debugging from the user perspective.
Codes were locally tested in Google Chrome's console (devTools).


# Prompt 2

Now that the bugs are fixed, add additional summary statistics such as mode, min, max, and print out the values using console.log, similar to the other statistics. In addition, make sure these statistics are aggregated and grouped by the fruit type so the result should give us 5 summary statistics for each fruit type in the dataset.


# Justif 2 orig

Response 1 is better than response 2 because it is more performant and optimal since it uses 'Object.keys' in line 64 to aggregate the summary statistics. Response 1 is a more consistent approach compared to the 'for...in' loop in line 74 in response 2 which is faster in JS engines because it finds all modes and joins them in case of multiple modes. While response 2 is calculating the maximum frequency and mode during each iteration, which is more redundant. Response 1 also includes better error handling for mode calculation joining multiple modes in a string making it more accurate, where as creates incremental values which is more computational if the dataset increases in size. The code in response 1 was ran successfully and faster than the code in response 2 by .02 seconds, however both responses provide the correct output. Response 1 is more performant therefore better using 'Object.keys' for efficient aggregation and includes better error handling, whereas response 2 is redundant and not as efficient. There were no bugs in response 1 or response 2.


# Justif 2 modif

le bajé a 4 la puntuación

Response 1 and Response 2 are basically the same except for the way the mode is calculated. Response 1 calculates all the modes in the case that multiple values share the same highest frequency. On the other hand, Response 2 only returns a single mode (the first one encountered).
However, because the prompt said nothing about how the mode should be calculated, this difference does not generate any kind of deviation.
Because of this, response 1 is hardly better than response 2.
I ran both codes in Google Chrome's devTools and both ran successfully, no issues were found.


# Feedback

Hello dear Contributor, I want to thank you for your time and effort in this project.
Your attempt is very good, but there are some things that I want to discuss.

Your prompts are fine. Their complexity level is not so high, but just enough to be OK. I would (in future tasks) try to increase this by adding more constraints, this will improve the overall quality of your work. Particularly speaking about debugging tasks, it is highly encouraged to use more complex codes, with errors that are not so evident. In this case (and for me) it's fine and enough, but consider that for the future.

I disagreed with your justifications: you marked that there were deviations where there were not. In both cases, you based your decision on differences in performance or "better code" but that's not what "Functionality & Performance" really is about. According to actual guidelines, it answers to the following questions:

- Does the code compile and run without errors and exceptions?
- Does the code compile and run and generate the expected results or outputs?

So, basically, this dimension arises when the response tries to run what the prompt said but fails to do so. Here that was not the case. So, I corrected the rankings and the justification accordingly.

Try these things in future tasks and you will probably get qualifications of 4 or 5 with no problems!

I will leave the documentation for a quick lecture!

* Documentation:

* Flamingo Crash Course:
https://docs.google.com/document/d/1djY7NcldjU21bRYCX6hoFHrrQSPQ5C_o0d_XDJnNUmY/edit#heading=h.3ibr2go7c4fs

* Dimension Priorities:
https://docs.google.com/document/d/1XtlJbL3WuvMBqKvqSmRHVCujy_fvDrluiKOzR5I0qO4/edit
# Data Analysis With Python 2021
a MOOC (Massive Open Online Course) course organized by Open University of Helsinki. More information found from [MOOC learning environment](https://dap-21.mooc.fi/).

> ## Let's analyze some data
> ### Data analysis with Python is a practical introduction to data analysis using a large number of programming exercises. 
> The course takes a practical approach to different phases of data analysis pipeline. After the course you can select subsets, transform, reshape and combine data. You learn to visualize data as simple plots or histograms. And finally, you'll be able to apply basic data analysis skills to a simple project.</br></br>
> Do you have good programming skills? Do you know the basics of probability calculus and linear algebra? Are you ready to work hard? If yes, let's start analyzing some data!

-----
### Task list:

- [ ] Exam
- [ ] Peer-reviewed project work

<b>TMC-exercises:</b>
- [x] Week 1 - 100 % completed
- [x] Week 2 - 100 % completed
- [ ] Week 3
- [ ] Week 4
- [ ] Week 5
- [ ] Week 6

-----

## Week 1 - Summary

 *   Python's code blocks are denoted by consistent indenting, with spaces or tabs, unlike in many other languages
 *   Python's for loops goes through all the elements of a container without the need of worrying about the positions (indices) of the elements in the container
 *   More generally, an iterable is an object whose elements can be gone through one by one using a for loop. Such as range(1,7)
 *   Python has dynamic typing: the type of a name is known only when we run the program. The type might not be fixed, that is, if a name is created, for example, in a loop, then its type might change at each iteration.
 *   Visibility of a name: a name that refers to a variable can disappear in the middle of a code block, if a del statement is issued!
 *   Python is good at string handling, but remember that if you want to concatenate large number of strings, use the join method. Concatenating by the + operator multiple times is very inefficient
  *  Several useful tools exist to process sequences: map, reduce, filter, zip, enumerate, and range. The unnamed lambda function can be helpful with these tools. Note that these tools (except the reduce) don't return lists, but iterables, for efficiency reasons: Most often we don't want to store the result from these tools to a container (such as a list), we may only want to iterate through the result!

## Week 2 - Summary

*    We have learned how regular expressions can be used to specify regular sets of strings
    *   We know how to find out if a string matches a regular expression
    *   We know how to extract pieces of text that match a RE
    *   We can replace matches to a RE with another string
    
*    We can read (and write) a text file either line by line or whole file at the same time
*    We also know how to specify the encoding of the file. The utf-8 encoding is a very common and can represent nearly every character or symbol of any (natural) language
*    Program's parameters are in the array sys.argv, and we can return a value from the program with the function sys.exit
*    The file streams sys.stdin, sys.stdout, and sys.stderr allow basic textual input and output to and from the program
*    Every value in Python is an object
    -    Classes are user defined data types, they tell how to construct instances (objects) of that type
    -    Relationship between objects and classes: isinstance
    -    Relationship between classes: issubclass
*    Exceptions signal exceptional situations, not necessarily errors
*    The efficiency of NumPy is based on the fact that the same operations can be performed on elements fast, if all the elements have the same type. These are called vectorized operations
*    We know how to create, reshape, perform basic access, combine, split, and aggregate arrays

# ExamTopics Scraper & Quiz Creator
## Steps
1. Go to the exam page
2. CTRL+s to save the page
3. Save in a directory named `res`
4. Repeat for all pages in the exam like a monkey because payment page isn't available
5. ???
6. Profit

## Types of questions
I am aware that there is at least one question with multiple answers. This quiz
does **NOT YET** have support for these types of questions. I am unaware if it is
even present in the list of questions as it may have a different tag.

## Notes
The implementation is quite poorly tought. It doesn't uses the fact the every card 
actually has its div. After 2 hours of coding, this actually led to some nasty bug
where on page 1 there are returned more correct answers (5 instead of 4) and on page
there are returned less (3 instead of 4). 

The bug on page 10 is due to a community progress bar not existing, but I did not find
the cause on page 1.

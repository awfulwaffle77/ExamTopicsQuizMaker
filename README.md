# ExamTopics Scraper & Quiz Creator

## What is this?
This is a Python-built CLI quiz for quizzes from ExamTopics. 
It gets questions from pages (saved locally as HTML at the moment),
shuffles them, you pick answers and then you are shown a 
final score and then questions you got wrong are 
written in a `.txt` file. Correct answers are taken from the
discussions.

It looks like this (example from the Google ACE exam, obviously
without the red markings):

![how_it_looks](https://i.imgur.com/7VED0g3.png)

## ⚠️ READ BEORE YOU START
This was initially tested on Windows and seems to work alright on this OS.

⚠️ As tested, saving a page with CTRL+s in ChromeOS does not save it
in HTML by default, as needed by the application. In the dropdown 
menu, you have to select "Webpage, HTML Only".

![html_only](https://i.imgur.com/87YOG3U.png)


## How do I get it working?
*Note: If you want the quiz for **Google Associate Cloud Engineer**, you can get the res directory
in the proper HTML format [here](https://www.udrop.com/6AuX/res.zip). Just unzip the archive
in the ExamTopicsQuizMaker directory AFTER you clone it and skip step 2.
At the moment it does **not** contain questions that are only available
to those with Contributor Access.*

1. Clone the repository with `git clone https://github.com/awfulwaffle77/ExamTopicsQuizMaker.git`
or by going in the upper part of the page, clicking Code > Download ZIP (and unzip the archive)
2. Create a new directory in the directory of the repository(inside ExamTopicsQuizMaker), 
named `res` 
3. Go to the exam page that you want 
(ex. https://www.examtopics.com/exams/google/associate-cloud-engineer/view/)
4. CTRL+s to save the page. It has to be HTML. Save it in the `res` directory
5. Repeat for all pages in the exam

The structure of the folder should now be:

📁ExamTopicsQuizMaker \
&ensp;|-> 📄 main.py \
&ensp;|-> 📄 requirements \
&ensp;|-> 📄 quiz.py \
&ensp;|-> 📄 _classes.py \
&ensp;|-> 📁 res \
&emsp;|-> 📄 all pages needed, in HTML format 

6. Install requirements with `pip install -r requirements`
7. Run `main.py` with `python main.py` or however your python3
command is called
8. Choose how many questions you want per run. This is if you want to
have a set of only n question before finishing and checking for wrong
questions, where n is the number you choose
9. Choose if you want the correct answer shown immediately after 
giving an answer or choose "no" if you want  to only check the file 
at the end of the quiz (a file is generated anyway)
10. Answer the questions
11. Review the .txt file that has been created when you have started
the quiz

## Steps with images
Create the `res` directory after cloning the repository

![step1](https://i.imgur.com/78xsRjX.png)

Go to the exam page and save it 

![step2](https://i.imgur.com/4hOW8c0.png)

How the `res` directory should look after saving all the needed pages

![step3](https://i.imgur.com/mEATsMZ.png)

Run `main.py` & get your quizzes done!

![step4](https://i.imgur.com/qpZ2r3N.png)

## Can't you automate these steps?
Yes and no. Due to the fact that ExamTopics uses a *lot* of captchas, 
this automation process would be accessible to people with contributor
access, as that disables captchas.

## Status
At this moment (5th of May 2022):
- scraping is done correctly from the HTML of ExamTopics pages.
- quizzes seem to be looking fine

## Bug reports
If you encounter any type a bug, please let me know by creating an 
[issue](https://github.com/awfulwaffle77/ExamTopicsQuizMaker/issues/new).

## Types of questions
I am aware that there is at least one question with multiple answers. To
answer those questions you have to write both answers concatenated, 
without space. For example, if the correct answers are `B` and `E`, you
have to write `BE`. 
# noqa: W291
file_diff = """
You are an expert programmer, and you are trying to su
mmarize a git diff.
Reminders about the git diff format:
For every file, there are a few metadata lines, like (
for example):
```
diff --git a/lib/index.js b/lib/index.js
index aadf691..bfef603 100644
--- a/lib/index.js
+++ b/lib/index.js
```
This means that `lib/index.js` was modified in this co
mmit. Note that this is only an example.
Then there is a specifier of the lines that were modif
ied.
A line starting with `+` means it was added.
A line that starting with `-` means that line was dele
ted.
A line that starts with neither `+` nor `-` is code gi
ven for context and better understanding.
It is not part of the diff.
After the git diff of the first file, there will be an
 empty line, and then the git diff of the next file.  

Do not include the file name as another part of the co
mment.
Do not use the characters `[` or `]` in the summary.  
Write every summary comment in a new line.
Comments should be in a bullet point list, each line s
tarting with a `-`.
The summary should not include comments copied from th
e code.
The output should be easily readable. When in doubt, w
rite less comments and not more. Do not output comment
s that simply repeat the contents of the file.        
Readability is top priority. Write only the most impor
tant comments about the diff.

EXAMPLE SUMMARY COMMENTS:
```
- Raise the amount of returned recordings from `10` to
 `100`
- Fix a typo in the github action name
- Move the `octokit` initialization to a separate file
- Add an OpenAI API for completions
- Lower numeric tolerance for test files
- Add 2 tests for the inclusive string split function 
```
Most commits will have less comments than this example
s list.
The last comment does not include the file names,     
because there were more than two relevant files in the
 hypothetical commit.
Do not include parts of the example in your summary.  
It is given only as an example of appropriate comments
.


THE GIT DIFF TO BE SUMMARIZED:
```
<FILE_DIFF>
```

THE SUMMARY:

"""
commit_summary = """
You are an expert programmer, and you are trying to su
mmarize a pull request.
You went over every file that was changed in it.      
For some of these files changes where too big and were
 omitted in the files diff summary.
Please summarize the pull request.
Write your response in bullet points, using the impera
tive tense following the pull request style guide.    
Starting each bullet point with a `-`.
Write a high level description. Do not repeat the comm
it summaries or the file summaries.
Write the most important bullet points. The list shoul
d not be more than a few bullet points.

THE FILE SUMMARIES:
```
<SUMMARY_POINTS>
```

Remember to write only the most important points and d
o not write more than a few bullet points.
THE PULL REQUEST SUMMARY:

"""
commit_title = """
You are an expert programmer, and you are trying to ti
tle a pull request.
You went over every file that was changed in it.      
For some of these files changes where too big and were
 omitted in the files diff summary.
Please summarize the pull request into a single specif
ic theme.
Write your response using the imperative tense followi
ng the kernel git commit style guide.
Write a high level title.
Do not repeat the commit summaries or the file summari
es.
Do not list individual changes in the title.

EXAMPLE SUMMARY COMMENTS:
```
Raise the amount of returned recordings
Switch to internal API for completions
Lower numeric tolerance for test files
Schedule all GitHub actions on all OSs
```

THE FILE SUMMARIES:
```
<SUMMARY_POINTS>
```

Remember to write only one line, no more than 50 chara
cters.
THE PULL REQUEST TITLE:

"""

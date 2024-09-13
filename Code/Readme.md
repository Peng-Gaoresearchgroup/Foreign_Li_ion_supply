# AI_summarization_for_organic_electroactive_molecules

### Description
The "AI_summarization_for_organic_electroactive_molecules.py" script is the main program used to summarize molecular and electrochemical reaction information from the references. The ''demo.pdf'' and ''demo.txt'' are input and output file for presentation.

### Operating system
- Windows, Mac , Linux

### Necessary python modules
- DrissionPage (most version should be fine)
- loguru (most version should be fine)
- requests (most version should be fine)

### Demo
- The input file is a pdf file of relevant literature or patent in the field of electrochemical organic synthesis, here ''demo.pdf'' is used as an example, and the input file should be placed under the Code folder.
- After running the ''AI_summarization_for_organic_electroactive_molecules.py'', the output ''demo.txt'' is expected to collect the relevant organic-electroactive chemical reaction information in ''demo.txt'' (following this format: [compound A][CAS number] reacts under [xxx] conditions, product is [compound B][CAS number]).

### Instructions for use
- Put the input file in Code folder, and run ''AI_summarization_for_organic_electroactive_molecules.py''.
- To reproduce the paper, all pdf files of the references and patents mentioned in the ''References_and_patents.md'' under Data folder should be put in the Code floder. Run the ''AI_summarization_for_organic_electroactive_molecules.py''. The summarized content will be saved to ''demo.txt''. Runtime expected to be 20 days (Depends on the frequency of web page visits). After the necessary organization, the 20 redox-active centers' summarization files were obtained in the Data folder.

### Disclaimer
- This code is intended for educational and research purposes only. Please ensure that you comply with relevant laws and regulations as well as the terms of service of the target website when using this code. The author is not responsible for any legal liabilities or other issues arising from the use of this code.
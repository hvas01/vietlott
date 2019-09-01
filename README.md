<h3>How to deploy on Google Cloud App Engine</h3>
<p><em>Prequisite:</em></p>
<p>    You already regiter an Google Cloud account and remember to activate the 300$ free balance.</p>
<p>    Install Google Cloud SDK</p>
<p></p>
<p>Step 1. Clone this repo to your development workstation.</p>
<p></p>
<p>Step 2. Logon to Google Cloud Console and create an empty project. Activate billing for this new project.</p>
<p></p>
<p>Step 3. On your development workstation, open Google Cloud SDK Shell. Then cd to the repo directory.Execute following commands to deploy this application to Google Cloud App Engine</p>
<p>'gcloud config list' -> verify the current active project</p>
<p>'gcloud config set project [your_project_name]' -> set the activate project if neccessary</p>
<p>'gcloud app deploy app.yaml' -> deploy the application to Google Cloud App Engine</p>
<p></p>
<p>You may need to select the region that host your app. The whole process might take a few minutes to complete.Upon completion, execute following commands to browse the new web app</p>
<p>'gcloud app browse'</p>

<hr>

<p>Vietlott 6/55</p>
<p></p>
<p>Play rule:You have to choose 6 different numbers to make a combination. Each number is between 1 to 55. </p>
<p></p>
<p>Problem:You have 1 in 28,989,675 chance of winning the Vietlott Power 6/55. Need a solution to improve the chance of winning. </p>
<p></p>
<p>Solution:Making a program that eliminates rare combinations by setting some rules.</p>
<p></p>
<p>Rules:</p>
<p></p>
<p>    It should generate 6 random numbers from 1-55</p>
<p>    It should generate numbers from Low (1-28) and High (29-55) with this ratios: 3:3 4:2 2:4</p>
<p>    It should generate Odd and Even numbers with the same ratio as above</p>
<p>    It should not generate 6 numbers from all of 5 groups</p>
<p>    The sum of the 6 numbers should be from 104 - 239</p>
<p>    The generated combination should not equal to any previous winning number (not working on this version)</p>
<p></p>
<p>Groups: </p>
<p></p>
<p>    1 -- 1-11 </p>
<p>    2 -- 12-22 </p>
<p>    3 -- 23-33 </p>
<p>    4 -- 34-44 </p>
<p>    5 -- 45-55</p>
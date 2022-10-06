# quantman-angel-auto-login
Daily Cron Job runner that opens browser, do login via your broker credentials and close the browser.
I created this only for Angel Broking
# Setup:

- In the quantman-login respository page. 
- Fork the repo using the fork button. (at the top right area in the page.) 
- In the forked repository page do the below 2 steps. (You should already be in the forked repo, if not Go to the forked repo)
- *Settings* 
  - Click the "Settings" button to go to the settings page.
  - Select Secrets. And within secrets Actions (in the left side panel).

    1. Click New Repository Secret. Add USERNAMES => <value> (fill in your client id's)
    2. Click New Repository Secret. Add PASSWORDS => <value> (fill in your client password's)
    3. Click New Repository Secret. Add TOTP => <value> (fill in your 26 character Secret Key)

- *Actions*
  - Click "Actions" button at the top of the page.
  - Click "I Understand my workflows, go ahead and enable them"
  - Select the "Auto Login Bot" in the left side panel.
  - In the disclaimer warning message in the center of the page, click "Enable Workflow"
- Now daily at 07:30, the enabled action will login in you into QuantMan using the credentials filled in the repository's secret.

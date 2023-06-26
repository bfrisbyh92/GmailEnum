<h1 align='center'>Enumerate Gmail Accounts</h1>

<h2 align='center'>Brendan Frisby</h2>
<h4 align='center'>https://github.com/bfrisbyh92/GmailEnum</h4>

### **A simple Python script to enumerate valid Gmail Accounts**

## How it works...
***If you make a request to the `https://mail.google.com/mail/gxlu?email=` endpoint, appending a valid email address(Any Google Username/Email) then it sets a cookie. If there is no such account, no cookie is set.***

<li>
git clone https://github.com/bfrisbyh92/GmailEnum.git && cd GmailEnum
</li>
<li>
python3 gmailenum.py
</li>
<h3>OR</h3>
<li>
python3 gmailenum.py -e <{UserList}> -o <{OutputFileLocation}>
</li>
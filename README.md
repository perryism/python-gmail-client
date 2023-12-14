# Get app password

App password can be generated here
https://myaccount.google.com/apppasswords

# Send email

<pre>
mail = Mail('test subject', 'perryism@gmail.com', 'perryism@gmail.com')
mail.text("Hello world!")

with Gmail('perryism@gmail.com', os.environ['GMAIL_APP']) as g:
    g.send(mail)"""

</pre>

# Receive email

<pre>

</pre>
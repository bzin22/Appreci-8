# Gild
Initial set-up of Appreciation webpage

## Link to the live website
[Link to the website](http://www.mygild.com)
[Link to same website at heroku link](https://guarded-oasis-19453.herokuapp.com/)

[See the google docs for more info on steps, as well as some screenshots](https://docs.google.com/document/d/1YyIzdYTXTHMGST9i7XrLBGXJBQP2-jouIFonMnoVpaQ/edit)
## 2021.04.23 Update
Deployed to Heroku.

1 Following the instructions, deploy the app to Heroku, it?s free. The general steps are:
- Install git and heroku
- Create a Heroku account (added you as a collaborator to the gild heroku repo).
* Once you have git installed, type the following commands in your webapp folder:
- `git init`
- `git add .`
- `git commit -m 'My first commit?'
* Run the following commands in your webapp folder to deploy to heroku:
- `heroku create`
- `git push heroku master` which will push your webapp to Heroku?s servers.
- `heroku run python manage.py migrate` to create the database
- `heroku ps:scale web=1` which actually assigns compute power to your app
- Run `heroku open` which will open your live website.


*To link with a godaddy domain, 
-in terminal:
heroku domains:add www.mygild.com
heroku domains
This is what the output should look like:

Copy the boiling-orchid-hj1kcg2zfpw8sl38mq7bhvf5.herokudns.com
This is the dns target.
In godaddy, go to dns settings for the domain you purchased. mygild for instance

Paste the dns target into the CName field, overwriting the @ symbol.
Follow the instructions here: https://www.earningbaba.com/redirect-non-www-to-www-in-godaddy/
To forward naked doman to site: mygild.com -> http://www.mygild.com:
Add a subdomain. mygild.com to www.mygild.com. Permanent, forward only 



I also added a venv folder.
Start venv:
source env/bin/activate
and
deactivate:
deactivate

I think django already takes care of package management with the existing requirments.txt

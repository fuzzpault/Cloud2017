from flask import Flask, render_template, request

from google.appengine.api import memcache
from google.appengine.api import users

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def main():
    user = users.get_current_user()
    if user:
      #return str(dir(user))
      curr_users = memcache.get('curr_users')
      if curr_users:
        if user.nickname() not in curr_users:
          curr_users.append(user.nickname())
          memcache.set('curr_users',curr_users)
      else:
        memcache.set('curr_users',[user.nickname()])
      logout_url = users.create_logout_url('/')
      curr_users = memcache.get('curr_users')
      return 'Logged in %s %s <a href="%s">logout</a> %s' % (user.nickname(), user.user_id(), logout_url, curr_users)
    else:
      login_url = users.create_login_url('/')
      return 'Sorry, you are not logged in. <a href="%s">login</a>' % login_url, 200
    return render_template('counter.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
    
    
    
    
    
    
    
    
    

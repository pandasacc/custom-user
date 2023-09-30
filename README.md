## Custom User Model
Custom user model for use in my personal projects. `username` field has been removed and `email` is used as username field. `first_name` and `last_name` replaced by one field called `name`

### How to Install
1. Copy to the project directory. Change `name` in `apps.py` to reflect the app's installed location.
2. In templates, create a folder called `accounts` and add 2 templates `login.html`, `change_password.html`
3. In settings.py, set `LOGOUT_REDIRECT_URL`, `LOGIN_REDIRECT_URL`, `LOGIN_URL`, `AUTH_USER_MODEL`, `SESSION_EXPIRE_AT_BROWSER_CLOSE`, `SESSION_COOKIE_AGE`, `PASSWORD_CHANGE_SUCCESS_URL`


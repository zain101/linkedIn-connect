from linkedin import linkedin
from linkedin import server
import sys

APP_KEY = '75calirpyvhcw9'

APP_SECRET = '1jHkmwpkx84hinRp'

RETURN_URL = 'http://localhost:8000/'
s = sys.argv[1]
print s
try:
    # print(linkedin.PERMISSIONS.enums.values())
    authentication = linkedin.LinkedInAuthentication(
        APP_KEY, APP_SECRET, RETURN_URL)
    #authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    # Pass it in to the app...
    print(authentication.authorization_url)
    application = linkedin.LinkedInApplication(authentication)
    # a='AQWNvW_ILh7iiKpiSQIRA2ColGyDdzu6fH0S9EzUg2sEdL95ABETk7i9CZIvecoeFt7VF2nVr46FFajW2b9XUevH9btw5C5Qhd-6W_Hj-lFcA1InbaGHbDyMcA_d6ux8qw26z4hoPN_Qxe47qqbo3uV3t8l-Mw9mI8BVLXf_duk0TUyNEBo'
    # a='AQUArDgkIawfIl8WNy0fya-sPvaVyKCf7XFByvYbyFHBGf5_Xcgf4xM1Fl81VgIZwdd0pZH0wfvb7Dh97ECDn0aFkruHeJJXd-9n9Gh5lb9WUiSHyKUoDeJN4SA8Azj2tp-gDJpJOCU7lKoHTrrMzMHBf3-YrrX7NNxlrCMhOW6Zbnib5Kk'
    a = 'AQWAC76Tt8zb9Nr1xGEJZqpuQRKQod0tv4NlrWX5hiSNpwxy33dKGnSlzO9ahf-eMHkmEIeHNTgkD1yo0HOKy5UeDiOZEg-rOCuUYL9TQJaup-qXP29O1GxTGfVAfI8LCzPGselTAIT1H-qZmlZKAA_K7bzsa-bxNezFwsqHgMO24xMf-QI'
    # https://api.linkedin.com/v1/people/~/email-address?format=json
    application = linkedin.LinkedInApplication(token=a)
    prof = application.get_profile(selectors=[
                                   'email-address', 'id', 'languages', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
    print(prof)
except ValueError as e:
    print(str(e))

"""
WSGI config for tri_issues project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

#sys.path.insert(0, 'C:/Users/Administrator/AppData/Local/Programs/Python/Python312/Lib/site-packages')
sys.path.append('D:/FTP/TRI_ISSUES')
sys.path.append('D:/FTP/TRI_ISSUES/tri_issues')
#sys.path.insert(0, 'D:/Python/projects/tri_issues')
#sys.path.insert(0, 'D:/Python/projects/tri_issues/tri_issues')

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tri_issues.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "tri_issues.settings"

application = get_wsgi_application()

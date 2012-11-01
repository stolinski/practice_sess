from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test pracitce')
    local('git add -p && git commit') # or local('hg add && hg commit')

from fabric.api import lcd, local

def deploy():
    with lcd('../../Sites/practice/'):

        # With git...
        local('git pull ../../dev/practice/')

        # With both
        local('python manage.py migrate practice_tracking')
        local('python manage.py test practice_tracking')
        local('cd ../../dev/practice/ | python manage.py runserver')
from cactus.template_tags import register

def nbsp(value):
    return value.replace(' ', '&nbsp;')

def preBuild(site):
    register.filter('nbsp', nbsp)

from HowMany import app
import heroku


@app.template_filter('fuzzystamp')
def fuzzystamp(dtobj):
    tstring = dtobj.isoformat("T") + "Z"
    return "<time class='timeago' datetime='%s'></time>" % (tstring,)

# @app.context_processor
# def get_app_name():
#     return dict(app_name=app.config['APP_NAME'])
#
# @app.context_processor
# def get_app_version():
#     cloud = heroku.from_key(app.config['HEROKU_API_KEY'])
#     return dict(app_version=cloud.apps[app.config['APP_NAME']].releases[-1].name)
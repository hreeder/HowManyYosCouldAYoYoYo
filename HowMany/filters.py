from HowMany import app


@app.template_filter('fuzzystamp')
def fuzzystamp(dtobj):
    tstring = dtobj.isoformat("T") + "Z"
    return "<time class='timeago' datetime='%s'></time>" % (tstring,)
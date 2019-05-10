from download import get_url

def test_url():
    URL = 'https://cpb-us-w2.wpmucdn.com/portfolio.newschool.edu/dist/4/3049/files/2015/05/Emoji-Presentation-1wijyji.pdf'
    resp = get_url(URL)
    assert resp == get_url(URL)


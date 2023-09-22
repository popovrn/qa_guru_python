from selene import  be, have, browser

def test_first_less1(browser_setings):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_second_less2(browser_setings):
    browser.element('[name="q"]').should(be.blank).type('988897hfgfytmmjmg76jt76jgkjhjghgf8687tmg86u7gjgf78775tjmgjk').press_enter()
    browser.element('[id="result-stats""]').should(have.text('988897hfgfytmmjmg76jt76jgkjhjghgf8687tmg86u7gjgf78775tjmgjk'))







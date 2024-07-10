from selene import have, browser
import allure


@allure.story("Пользователь ищет issue")
@allure.feature('Тестовая фича')
@allure.link('https://github.com/Kiwenk/QA_GURU_Home_Task_10')
@allure.description('Описание теста')
@allure.label('test_label')
@allure.tag('test_tag')
@allure.severity(allure.severity_level.MINOR)
def test_check_repo_issue():
    with allure.step('Открываем браузер'):
        browser.open('/')

    with allure.step('Открываем репозиторий через поиск'):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
        browser.element('#query-builder-test').type('Kiwenk/QA_GURU_Home_Task_9').press_enter()
        browser.element('[href="/Kiwenk/QA_GURU_Home_Task_9"]').click()

    with allure.step('Открываем issue'):
        browser.element('#issues-tab').click()
        browser.element('#issue_1_link').click()

    with allure.step('Проверяем текст issue'):
        browser.element('.js-issue-title').should(have.text('Тестовый issue'))

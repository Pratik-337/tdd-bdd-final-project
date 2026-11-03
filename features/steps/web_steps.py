@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element_by_id(button_id).click()

@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = 'product_' + element_name.lower().replace(' ', '_')
    found = context.driver.find_element_by_id(element_id).get_attribute('value')
    assert text_string == found

@then('I should not see "{name}" in the results')
def step_impl(context, name):
    element = context.driver.find_element_by_id('search_results')
    assert name not in element.text

@then('I should see the message "{message}"')
def step_impl(context, message):
    found = context.driver.find_element_by_id('flash_message').text
    assert message in found

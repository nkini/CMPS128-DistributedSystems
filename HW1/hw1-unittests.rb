require 'unirest'
require "test/unit"
 
class TestSimpleNumber < Test::Unit::TestCase
 
  def test_everything
    res = Unirest.get('http://localhost:49160/hello')
    assert_equal(res.raw_body, 'Hello world!', 'GET on the hello resource did not execute successfully')

    res = Unirest.get('http://localhost:49160/echo')
    assert_equal(res.raw_body, '', 'GET echo without a msg should have output a blank.')

    res = Unirest.get('http://localhost:49160/echo?msg=AnyColourYouLike')
    assert_equal(res.raw_body, 'AnyColourYouLike', 'GET echo with a message did not execute successfully')

    
    res = Unirest.get('http://localhost:49160/anUnknownMethod')
    assert_equal(res.code, 404, 'GET on random unknown resource should have failed, but did not.')

    res = Unirest.post('http://localhost:49160/hello')
    assert_not_equal(res.code, 200, 'POST on hello should not have worked, but returned successfully.')
    assert_equal(res.code, 405, 'POST should have returned a 405 METHOD NOT ALLOWED.')

  end
 
end

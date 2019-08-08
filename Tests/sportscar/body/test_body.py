from pytest import mark

@mark.smoke
@mark.body
class BodyTests:

    def test_body_function_as_expected(self):
        assert True
    def test_body_color(self):
        assert True
    def test_body_bumper(self):
        assert True
 

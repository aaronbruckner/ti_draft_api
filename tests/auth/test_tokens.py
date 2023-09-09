from jwt import ExpiredSignatureError
import pytest
from datetime import datetime
from freezegun import freeze_time
from ti_draft_api.auth import tokens

@pytest.mark.small
class TestValidateAuthToken:
  def test_raises_exception_if_token_invalid(self):
    with pytest.raises(Exception):
      tokens.validate_auth_token("MyFakeToken.tetfasfasd.fadsfsafs")
  
  def test_raises_exception_if_token_expired(sellf):
    # Given
    original_creation_time = datetime(year=2020, month=1, day=15, hour=12, minute=0)
    almost_expired_time = datetime(year=2020, month=1, day=15, hour=12, minute=29)
    expired_time = datetime(year=2020, month=1, day=15, hour=12, minute=31)
    TTL_30_MINUTES = 60*30

    with freeze_time(original_creation_time) as frozen_time:
      token = tokens.generate_auth_token("user1234", ttl_secs=TTL_30_MINUTES)
      
      frozen_time.move_to(almost_expired_time)
      jwt_state = tokens.validate_auth_token(token)
      assert jwt_state.user_id == "user1234"

      frozen_time.move_to(expired_time)
      with pytest.raises(ExpiredSignatureError):
        # Too much time has passed and now token is expired
        tokens.validate_auth_token(token)

  def test_can_correctly_extract_payload_from_previously_generated_token(self):
    # Given
    token = tokens.generate_auth_token("user1234")

    # When
    jwt_state = tokens.validate_auth_token(token)

    # Then
    assert jwt_state.user_id == "user1234"

  

class JwtState:
  """Represents all the state contained within a JWT."""
  def __init__(self, user_id: str) -> None:
    self.user_id = user_id
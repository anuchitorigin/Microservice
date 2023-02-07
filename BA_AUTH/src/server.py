import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL
from .env import settings


server = Flask(__name__)
mysql = MySQL(server)


@server.route("/login", methods=["POST"])
def login():
  auth = request.authorization
  if not auth:
    return "missing credentials", 401
  # Check username, password
  cur = mysql.connection.cursor()
  res = cur.execute(
    "SELECT email, password FROM user WHERE email = %s", (auth.username)
  )
  if res > 0:
    user_row = cur.fetchone()
    email = user_row[0]
    password = user_row[1]
    if (auth.username != email) or (auth.password != password):
      return "invalid credentials", 401
    else:
      return createJWT(auth.username, settings.OAUTH2_SECRET_KEY, True)
  else:
    return "invalid credentials", 401


@server.route("/validate", method=["POST"])
def validate():
  encoded_jwt = request.headers["Authorization"]
  if not encoded_jwt:
    return "missing credentials", 401
  token = encoded_jwt.split(" ")[1]
  try:
    decode = jwt.decode(
      token,
      settings.OAUTH2_SECRET_KEY,
      algorithm=[settings.OAUTH2_ALGORITHM]
    )
  except:
    return "not authorized", 403
  return decode, 200


def createJWT(username, secert, authz):
  return jwt.encode(
    {
      "username": username,
      "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
      "iat": datetime.datetime.utcnow(),
      "admin": authz
    },
    secert,
    algorithm=settings.OAUTH2_ALGORITHM
  )


if __name__ == "__main__":
  server.run(host="0.0.0.0", port=5000)

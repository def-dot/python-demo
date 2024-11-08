import babyagi


app = babyagi.create_app("/dashboard")
app.run(host='0.0.0.0', port=8080)

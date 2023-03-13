from blog.app import app
import commands

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )

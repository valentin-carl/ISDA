### Database example

To create a database (assuming you're using a unix shell), just run `./init.sh` in your terminal. If you're getting something like `zsh: permission denied: ~/init.sh`, try running `chmod 755 init.sh` and run the script again. If you're on Windows, just running the `create_db.py` should also work; however, I didn't test it.

To play around with the database, run the `db.py` file, which lets you put SQL commands into your console and will print the results.

If you find any bugs (as there will probably be some), please open an issue, shoot me an [e-mail](v.carl@campus.tu-berlin.de), or fix them and start a pull request (preffered option).

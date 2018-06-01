# String Manipulation Utility

The purpose of this CLI is to manipulate text data from files and export into a combine file or two files.

### Development Environment

After forking the project, `cd` to project root and run `pipenv install`. If `pipenv` is not installed on your system, run `pip install pipenv` or whatever package manager you are using on your system such `conda`.

### Combined Format

For building LR models utilizing training data combined into one file, positive and negative sentences in the same file.

```
complaint1, I don't like this bank.
complaint1, Customer service is terrible.
none, Great experience so far.
...
```

For building LR models utilizing training data split in two files, positive and negative sentences are in separate files respectively without labels. The name of the file will determine the label.

```
This is a positive complaint sentence.
And this is another positive complaint sentence.
...
```

```
Negative complaint sentence.
Another negative complaint sentence.
...
```

The ultimate goal would be to pass different flags to let the app know how to export the file, and the directory where the data resides.

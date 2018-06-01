# String Manipulation Utility
<hr>

The purpose of this CLI is to manipulate training text data from files and export files to either trex or p2s `training_data.txt` format.

#### Trex Format

For building LR models utilizing trex, positive and negative sentences are contained in the same file.

```
complaint1, I don't like this bank.
complaint1, Customer service is terrible.
none, Great experience so far.
...
```

For building LR models utilizing p2s, positive and negative sentences are in separate files respectively without labels.

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

The ultimate goal would be to pass a flag  `-trex` or `-p2s` to let the app know how to export the file, and the directory where the data resides.

### Trex Features:

- Abel to pass how many layers and new positive and negative examples. The utility should update existing `training_data.txt` with the new data on each layer with their respective labels.

### P2S Features:

- Abel to pass new positives and negatives examples and the utility should update existing `pos.txt` and `neg.txt` and normalized them.
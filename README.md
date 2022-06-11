# Mandarin Stuff
- Just publicising some of the resources I use to learn mandarin
- Currently I am working on transferring my written notes to the vocab CSV files that will be interpreted by the Python script eventually
- This will allow for testing of translation, as well as presenting random English / Pinyin to be handwritten as characters on paper

## TODO:
- [x] **Example functionality separate to definition**
- [x] Practice En-Zh and Zh-En functionality
- [x] Difficulty filtering
- [ ] Copy over all written notes
- [ ] Speed testing?
- [ ] Number generator - for practicing translating numbers Zh-En
- [ ] Simple sentence generator maybe? (perhaps scraping translation from Google Translate or similar (or using API if there is one))

```
usage: mandarin.py [-h] [-f] [-d DIFFICULTY] [-c] [-p] fileOrFolder

Learn Mandarin

positional arguments:
  fileOrFolder          file or directory of files to test with

options:
  -h, --help            show this help message and exit
  -f, --useFolder       use a directory of csv files -> will test using all files
  -d DIFFICULTY, --difficulty DIFFICULTY
                        min difficuly (from 1 to 5) to test from - to skip easy words
  -c, --characterTest   tests pinyin (no tones) + translation -> character
  -p, --pinyinTest      tests character -> pinyin + tones + translation
```
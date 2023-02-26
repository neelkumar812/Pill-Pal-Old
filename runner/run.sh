#Automating scripts for running the test
tesseract /Users/i584196/biggestBirds/images/demo_test.jpeg sample_output
echo sample_output.txt
python3 main.py
#test_chlor.jpeg
cd ../google_calendar
node index.js
text = "X-DSPAM-Confidence:    0.8475";
a=text.find('0')
print(float(text[a:]))
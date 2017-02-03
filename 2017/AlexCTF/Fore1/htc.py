#!/usr/bin/env python

encoded_flag = 'cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'

# cut first 3 chars and create list
encoded_flag = encoded_flag[3:]

decoded_flag = ''.join([encoded_flag[x]
                        for x in range(0, len(encoded_flag)) if x % 5 == 0])

print decoded_flag

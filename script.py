# script.py

import pickle

a = 1
b = 'a string'

save = {'a': a, 'b':b}
pickle.dump(save, open('vars.pkl', 'wb'))

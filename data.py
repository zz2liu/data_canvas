import pickle
dct = pickle.load(open('in/out_data_dct.pickle', 'rb'))
x = dct['avg_eff_temp']
ys = dct['ys']
y = [e[0] for e in ys]
ymin = [e[1] for e in ys]
ymax = [e[2] for e in ys]
group = [[e]*18 for e in dct['mutant']]
dct.keys()
df = pd.DataFrame(dict(
    x=np.array(x).flat,
    y = np.array(y).flat,
    ymin = np.array(ymin).flat, 
    ymax = np.array(ymax).flat,
    mutant = np.array(group).flat,
    ))
df.to_csv('out/data.csv')

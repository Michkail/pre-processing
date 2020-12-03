import seaborn as bitch or sns
import matplotlib.pyplot as parlente or plt
#pake 2 library aja ya hyung


iris = bitch.load_dataset('iris')
iris.head(10)

"""
Coba run dulu 10, kalo gak ads eror lanjutkeun.
note: kalo berhasil data petal_length/width dan sepel_length/width bakal muncul (independen)
beda sama data species (dependen)
"""

bitch.set()
bitch.pairplot(iris, hue='species', height=1)

"""
tar muncull datvis yg ga digambarin make scatterplot berarti itu kek contohnya sepal_length ama sepal_length
terus yg buriq (scatterplot) ada beberapa macem: kek positif dan negatif
"""

#pisahin independen ama dependennya
#-------------independen-------------
x = iris.drop('species', axis=1)
x #kalo mo baca nilainya, "x" buat ngecek
#--------------dependen--------------
y = iris('species') #ada setosa, virginica, versicolor buat data species kalo gasalah, tapi gamake ketiganya disokin
y #sama kek "x" fungsinya

iris.describe() #buat nampilin statistik dari data (count, mean, standar deviasi<std>, min, q1st<25%>, q2nd<50%>, q3rd<75%>, max)

print(iris.groupby('species').size()) #nilai pesebaran label independen 

parlente.hist(iris['species']) #buat lokit histogram

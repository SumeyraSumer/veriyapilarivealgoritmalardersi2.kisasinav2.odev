import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Excel dosyasını oku
df = pd.read_excel('2D_clustering_data.xlsx')

# Kümeleme için gerekli veri setini seç
X = df.iloc[:, 1:].values

# Aglomeratif hiyerarşik kümeleme yap
Z = linkage(X, method='ward')

# Dendrogramı çiz
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Aglomeratif Hiyerarşik Kümeleme')
plt.xlabel('Gözlem Birimleri')
plt.ylabel('Uzaklık')
plt.show()

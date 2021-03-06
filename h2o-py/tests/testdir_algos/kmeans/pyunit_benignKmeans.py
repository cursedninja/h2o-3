import sys
sys.path.insert(1, "../../../")
import h2o

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import Imputer

def benignKmeans(ip,port):
    # Connect to a pre-existing cluster
    h2o.init(ip,port)  # connect to localhost:54321


    #  Log.info("Importing benign.csv data...\n")
    benign_h2o = h2o.import_frame(path=h2o.locate("smalldata/logreg/benign.csv"))
    #benign_h2o.summary()

    benign_sci = np.genfromtxt(h2o.locate("smalldata/logreg/benign.csv"), delimiter=",")
    # Impute missing values with column mean
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    benign_sci = imp.fit_transform(benign_sci)

    # Log.info(paste("H2O K-Means with ", i, " clusters:\n", sep = ""))
    for i in range(1,7):
        benign_h2o_km = h2o.kmeans(x=benign_h2o, k=i)
        print "H2O centers"
        print benign_h2o_km.centers()

        benign_sci_km = KMeans(n_clusters=i, init='k-means++', n_init=1)
        benign_sci_km.fit(benign_sci)
        print "sckit centers"
        print benign_sci_km.cluster_centers_

if __name__ == "__main__":
  h2o.run_test(sys.argv, benignKmeans)

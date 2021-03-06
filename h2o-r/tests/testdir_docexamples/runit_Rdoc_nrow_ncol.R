setwd(normalizePath(dirname(R.utils::commandArgs(asValues=TRUE)$"f")))
source('../h2o-runit.R')

test.rdoc_nrow_ncol.golden <- function(H2Oserver) {

irisPath <- system.file("extdata", "iris.csv", package="h2o")
iris.hex <- h2o.uploadFile(H2Oserver, path = irisPath, destination_frame = "iris.hex")
nrow(iris.hex)
ncol(iris.hex)

testEnd()
}

doTest("R Doc nrow and ncol", test.rdoc_nrow_ncol.golden)

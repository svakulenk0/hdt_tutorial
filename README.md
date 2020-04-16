# hdt_tutorial
HDT for NLP + ML + KG applications

1. Install [HDT C++](https://github.com/rdfhdt/hdt-cpp)

Tips:

** copy serd/serd.h into src/libhdt folder

** configure path to serd library:
export LD_LIBRARY_PATH=/my_folder/serd-0/build


2. Install [pyHDT](https://github.com/webdata/pyHDT):
```
git clone https://github.com/webdata/pyHDT.git
cd pyHDT/
./install.sh
```

3. Download HDT file and its index (if available) from http://www.rdfhdt.org/datasets/
```
wget http://gaia.infor.uva.es/hdt/freebase-rdf-2013-12-01-00-00.hdt.gz
```

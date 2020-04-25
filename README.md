# hdt_tutorial

1. Install [HDT C++](https://github.com/rdfhdt/hdt-cpp)

Troubleshooting:

** copy serd/serd.h into src/libhdt folder

** configure path to serd library:
```
export LD_LIBRARY_PATH=/my_folder/serd-0/build
make check SERD_LIBS="-L/ivi/ilps/personal/svakule/serd-0/build/ -lserd-0" SERD_CFLAGS="-I/ivi/ilps/personal/svakule/serd-0/serd"
```

2. Install [pyHDT](https://github.com/webdata/pyHDT):
```
git clone https://github.com/webdata/pyHDT.git
cd pyHDT/
./install.sh
```

3. Download and uncompress the HDT file and its index (if available) from http://www.rdfhdt.org/datasets/ e.g.
```
wget http://gaia.infor.uva.es/hdt/wikidata/wikidata20200309.hdt.gz
wget http://gaia.infor.uva.es/hdt/wikidata/wikidata20200309.hdt.index.v1-1.gz
or
wget http://gaia.infor.uva.es/hdt/freebase-rdf-2013-12-01-00-00.hdt.gz
```

4. Dump entity and predicate labels into separate files:
```
  -o Dump also objects

  -u Dump only URIs

  -p <exportPredicateFile> exportPredicateFile (outPred.txt by default)

  -t <exportTermsFile> portTermsFile (outTerms.txt by default)

```
e.g.
```
hdt-cpp/libhdt/tests/dumpDictionary wikidata20200309.hdt -o -u -t wikidata20200309Entities.txt
hdt-cpp/libhdt/tests/dumpDictionary wikidata20200309.hdt -o -t wikidata20200309Terms.txt
hdt-cpp/libhdt/tests/dumpDictionary wikidata20200309.hdt -p wikidata20200309Pred.txt
```

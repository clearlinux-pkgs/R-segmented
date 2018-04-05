#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-segmented
Version  : 0.5.3.0
Release  : 2
URL      : https://cran.r-project.org/src/contrib/segmented_0.5-3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/segmented_0.5-3.0.tar.gz
Summary  : Regression Models with Break-Points / Change-Points Estimation
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n segmented

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521242930

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521242930
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library segmented
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library segmented
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library segmented
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library segmented|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/segmented/CITATION
/usr/lib64/R/library/segmented/DESCRIPTION
/usr/lib64/R/library/segmented/INDEX
/usr/lib64/R/library/segmented/Meta/Rd.rds
/usr/lib64/R/library/segmented/Meta/data.rds
/usr/lib64/R/library/segmented/Meta/features.rds
/usr/lib64/R/library/segmented/Meta/hsearch.rds
/usr/lib64/R/library/segmented/Meta/links.rds
/usr/lib64/R/library/segmented/Meta/nsInfo.rds
/usr/lib64/R/library/segmented/Meta/package.rds
/usr/lib64/R/library/segmented/NAMESPACE
/usr/lib64/R/library/segmented/NEWS
/usr/lib64/R/library/segmented/R/segmented
/usr/lib64/R/library/segmented/R/segmented.rdb
/usr/lib64/R/library/segmented/R/segmented.rdx
/usr/lib64/R/library/segmented/data/down.rda
/usr/lib64/R/library/segmented/data/plant.rda
/usr/lib64/R/library/segmented/data/stagnant.rda
/usr/lib64/R/library/segmented/help/AnIndex
/usr/lib64/R/library/segmented/help/aliases.rds
/usr/lib64/R/library/segmented/help/paths.rds
/usr/lib64/R/library/segmented/help/segmented.rdb
/usr/lib64/R/library/segmented/help/segmented.rdx
/usr/lib64/R/library/segmented/html/00Index.html
/usr/lib64/R/library/segmented/html/R.css

%define major 4
%define oname netcdf
%define sname lib%oname
%define sover 11
%define priority 30
%define hdfdir %_libdir/hdf5-seq

Name: %sname%sover-seq
Version: %major.4.1.1
Release: alt3

Summary: Libraries to use the Unidata network Common Data Form (netCDF)

License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/software/netcdf/

Requires(post,preun): alternatives
Requires: libhdf5-8-seq
Conflicts: %sname-mpi < 4.0.1-alt6 %oname%sover-mpi-tools < 4.0.1-alt6
Conflicts: %sname-mpi-devel-doc
Provides: %sname = %version-%release
Provides: %sname%sover = %version-%release
Conflicts: %sname < %version-%release
Obsoletes: %sname%sover < %version-%release
%ifarch x86_64
Provides: %sname.so.%sover()(64bit)
%else
Provides: %sname.so.%sover
%endif

# https://github.com/Unidata/netcdf-c.git
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: flex gcc-c++ gcc-fortran zlib-devel libhdf5-devel

BuildPreReq: /usr/bin/tex libcurl-devel libexpat-devel doxygen graphviz

%description
NetCDF (network Common Data Form) is an interface for array-oriented
data access and a freely-distributed collection of software libraries
for C, Fortran, C++, and perl that provides an implementation of the
interface.
The netCDF library also defines a machine-independent format for
representing scientific data. Together, the interface, library, and
format support the creation, access, and sharing of scientific data. The
netCDF software was developed at the Unidata Program Center in Boulder,
Colorado.

NetCDF data is:

   o Self-Describing. A netCDF file includes information about the data
     it contains.

   o Network-transparent. A netCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.

   o Direct-access. A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding data.

   o Appendable. Data can be appended to a netCDF dataset along one
     dimension without copying the dataset or redefining its structure.
     The structure of a netCDF dataset can be changed, though this
     sometimes causes the dataset to be copied.

   o Sharable. One writer and multiple readers may simultaneously
     access the same netCDF file.

%description -l ru_RU.UTF-8
NetCDF (network Common Data Form) - это ориентированный на массивы
интерфейс для доступа к данным и, одновременно, свободно
распространяемая коллекция программ и библиотек для C, Fortran, C++,
которые реализуют этот интерфейс. Программы netCDF были
разработаны Гленом Дэвисом (Glenn Davis), Руссом Рью (Russ Rew),
Стивом Еммерсоном (Steve Emmerson), Джоном Кэроном (John Caron) и
Харвей Дэвисом (Harvey Davies) в Unidata Program Center в Боулдере,
Колорадо и расширены вкладами от других пользователей netCDF.
Библиотеки netCDF определяют машиннонезависимый  формат для
представления научных данных. Интерфейс, библиотеки и сам формат
поддерживают создание, доступ и совместное использование научных
данных.

%package -n %sname-devel
Summary: Development tools for the NetCDF library
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF
Group: Development/C
Provides: pkgconfig(%oname) = %EVR
Requires(post,preun): alternatives
Requires: %name = %version-%release
Conflicts: %sname-mpi-devel < 4.0.1-alt6

%description -n %sname-devel
This package contains the netCDF-3 header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF library,
you'll need to install the %sname-devel package.

%description -l ru_RU.UTF-8 -n %sname-devel
Заголовочные файлы и документация для использования библиотеки NetCDF
в приложениях.

Если вы собираетесь разрабатывать приложения, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%sname-devel.

%package doc
Summary: Documentation for NetCDF
Summary(ru_RU.UTF-8): Документация по NetCDF
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description doc
Documentation for NetCDF library.

%description -l ru_RU.UTF-8 doc
Документация по NetCDF.

%prep
%setup
%patch1 -p1

rm -fR udunits/expat

%build
%add_optflags -I%hdfdir/include -fno-strict-aliasing %optflags_shared
%autoreconf
%configure \
	--enable-shared \
	--enable-static=no \
	--bindir=%hdfdir/bin \
	--libdir=%hdfdir/lib \
	--includedir=%hdfdir/include \
	--enable-netcdf-4 \
	--enable-cxx-4 \
	--enable-docs-install \
	--enable-ncgen4 \
	--with-udunits \
	--with-hdf5=%hdfdir \
	--with-zlib=%prefix \
	--enable-doxygen \
	--enable-internal-docs \
	--enable-extra-example-tests \
	--enable-extra-tests \
	--enable-v2 \
	--enable-mmap \
	--disable-dap-remote-tests
%make

%install
%makeinstall_std

install -d %buildroot%hdfdir/include/netcdf
ln -s netcdf %buildroot%hdfdir/include/netcdf-3
install -p -m644 include/*.h %buildroot%hdfdir/include/netcdf
sed -i 's|config\.h|netcdf_config.h|' \
	%buildroot%hdfdir/include/netcdf/*
install -p -m644 config.h \
	%buildroot%hdfdir/include/netcdf/netcdf_config.h
rm -f %buildroot%hdfdir/include/netcdf/netcdf.h
mv %buildroot%hdfdir/include/*.* %buildroot%hdfdir/include/netcdf/
install -d %buildroot%_includedir
ln -s %hdfdir/include/netcdf %buildroot%_includedir/netcdf-3
ln -s %hdfdir/include/netcdf %buildroot%_includedir/netcdf
rm -f %buildroot%hdfdir/lib/*.la

install -m644 docs/man/man3/* %buildroot%_man3dir

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%hdfdir/lib
for i in %sname.so.*; do
	ln -s ../..%hdfdir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
for i in $(ls *.so); do
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-devel.alternatives
done
echo "%_bindir/nc-config %hdfdir/bin/nc-config %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
echo "%_pkgconfigdir/%oname.pc %hdfdir/lib/pkgconfig/%oname.pc %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
popd
pushd %buildroot%hdfdir/bin
for i in $(ls |egrep -v 'nc\-config'); do
	echo "%_bindir/$i %hdfdir/bin/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
popd

# There is a file in the package with a name starting with <tt>._</tt>,
# the file name pattern used by Mac OS X to store resource forks in non-native
# file systems. Such files are generally useless in packages and were usually
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%pre -n %sname-devel
rm -fR %_includedir/netcdf-3 %_includedir/netcdf \
	%hdfdir/include/netcdf-3 %hdfdir/include/netcdf

%files
%doc COPYRIGHT README* RELEASE_NOTES*
%hdfdir/bin/*
%exclude %hdfdir/bin/nc-config
%_man1dir/*
%ghost %_libdir/%sname.so.*
%hdfdir/lib/%sname.so.*
%_altdir/%name.alternatives

%files -n %sname-devel
%hdfdir/bin/nc-config
%hdfdir/include/netcdf-3
%hdfdir/include/netcdf
%_includedir/netcdf-3
%_includedir/netcdf
%hdfdir/lib/*.so
%hdfdir/lib/pkgconfig/*
%_man3dir/netcdf.3*
%_altdir/%name-devel.alternatives

%files doc
%doc docs/html examples
%_man3dir/*
%exclude %_man3dir/error.3*
%exclude %_man3dir/netcdf.3*
#exclude %_man3dir/index.3*

%changelog
* Fri Sep 08 2017 Mikhail Gordeev <obirvalger@altlinux.org> 4.4.1.1-alt3
- (ALT#33843) Fix broken update

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1.1-alt2
- Split into separate package named libnetcdf11-seq.

* Thu Aug 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1.1-alt1
- Updated to stable upstream version 4.4.1.1.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Wed Jul 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3
- Added Provides: pkgconfig(netcdf) = %EVR

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2
- Applied repocop patch

* Wed Jul 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt3
- Rebuilt with new libhdf5

* Sat Sep 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt2
- Avoid conflict with man-pages

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1.1
- Reenabled netCDF version 2 API

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1
- Version 4.2.1.1

* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt4
- Rebuilt

* Fri Mar 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt3
- Fixed flags in nc-config

* Thu Mar 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt2
- Fixed alternative for %oname.pc (ALT #27049)
- Fixed Cflags in %oname.pc

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt2
- Set %_libdir/libudunits2.so.* as %%ghost

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2
- Disabled devel-static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt8
- Fixed soname set-versions by ghost links (thnx ldv@)

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt7
- Rebuilt for soname set-versions

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt6
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288 for client software

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt5
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288

* Mon Jun 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4.1
- Fixed bug when installing devel package

* Mon Jun 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4
- Fixed bug when installing devel package (ALT #20510)

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3
- Created alternatives

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added explicit conflicts with parallel version of libraries

* Tue Jun 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- new version build based on Mandriva's srpm and obsoleted libnetcdf from ALT Linux Sisyphus

* Thu Aug 14 2008 Emmanuel Andry <eandry@mandriva.org> 4.0-1mdv2009.0
+ Revision: 271832
- New version
- fix license

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.6.3-1mdv2009.0
+ Revision: 232195
- 3.6.3
- added a patch from gentoo, though it won't help much
- use _disable_ld_as_needed and _disable_ld_no_undefined to make it build

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Thauvin <nanardon@mandriva.org>
    - unzip source in %%install instead %%check

* Sun Jan 20 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-4mdv2008.1
+ Revision: 155303
- fix devel static package name
- drop obsoletes

* Sat Jan 19 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-3mdv2008.1
+ Revision: 155130
- fix obsoletes

* Sat Jan 19 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-2mdv2008.1
+ Revision: 155081
- rebuild

* Thu Jan 03 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-1mdv2008.1
+ Revision: 144107
- import netcdf


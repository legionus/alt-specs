%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname parmetis
Name: %{oname}0
Version: 3.2.0
Release: alt4
Summary: Parallel Graph Partitioning and Fill-reducing Matrix Ordering
License: Free for non-commertial
Group: Sciences/Mathematics
Url: http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ParMetis-%version.tar
Source1: %oname.pc

BuildPreReq: %mpiimpl-devel

%description
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

%package -n lib%name
Summary: Shared libraries of ParMETIS
Group: System/Libraries

%description -n lib%name
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains shared libraries of ParMETIS.

%package -n lib%name-devel
Summary: Development files of ParMETIS
Group: Development/C
Requires: lib%name = %version-%release
Requires: %mpiimpl-devel

%description -n lib%name-devel
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains development files of ParMETIS.

%package -n lib%name-devel-doc
Summary: Development documentation of ParMETIS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains development documentation of ParMETIS.

%package examples
Summary: Example graphs for ParMETIS
Group: Development/Documentation
BuildArch: noarch

%description examples
ParMETIS is an MPI-based parallel library that implements a variety of
algorithms for partitioning unstructured graphs, meshes, and for computing
fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
provided by METIS and includes routines that are especially suited for parallel
AMR computations and large scale numerical simulations. The algorithms
implemented in ParMETIS are based on the parallel multilevel k-way
graph-partitioning, adaptive repartitioning, and parallel multi-constrained
partitioning schemes developed in our lab.

This package contains example graphs for ParMETIS.

%prep
%setup
install -m644 %SOURCE1 %name.pc

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" %name.pc

mv %oname.h %name.h

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%make_build \
	INCDIR="-I%mpidir/include" \
	OPTFLAGS="%optflags %optflags_shared" \
	LIBDIR="-L%mpidir/lib -Wl,-R%mpidir/lib" \
	CC="%mpidir/bin/mpicc"

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%mpidir/bin
install -d %buildroot%_libdir
install -d %buildroot%mpidir/lib
install -d %buildroot%_includedir/%name
install -d %buildroot%mpidir/include/metis0
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name
install -d %buildroot%_pkgconfigdir

pushd Graphs
install -m755 *%version %buildroot%mpidir/bin
rm -f *%version
install -p -m644 * %buildroot%_datadir/%name
popd

install -m644 *.a %buildroot%mpidir/lib
install -m644 Manual/* %buildroot%_docdir/%name
install -m644 *.h %buildroot%_includedir
install -m644 METISLib/*.h %buildroot%mpidir/include/metis0
install -m644 ParMETISLib/*.h %buildroot%_includedir/%name

sed -i 's|@VERSION@|%version|' %name.pc
install -m644 %name.pc %buildroot%_pkgconfigdir

# shared libraries

pushd %buildroot%mpidir/lib
for i in %name; do
	mpicc -shared -Wl,--whole-archive libparmetis.a libmetis.a \
		-Wl,--no-whole-archive  -lm -Wl,-soname,lib$i.so.0 \
		-o lib$i.so.0 -Wl,-z,defs -Wl,-R%mpidir/lib
	ln -s lib$i.so.0 lib$i.so
	rm -f *.o
done
mv lib$i.* %buildroot%_libdir/
popd

%files
%doc CHANGES LICENSE.txt README
%mpidir/bin/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%mpidir/include/*
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/%name

%files examples
%_datadir/%name

%changelog
* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt4
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt3
- Fixed RPATH

* Tue Sep 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt2
- Renamed this version: %oname -> %name

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0
- Disabled devel-static package

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt10
- Removed libmetis.so*

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt9
- Rebuilt for debuginfo

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt8
- Packed all necessary symbols into libparmetis.so

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt7
- Fixed overlinking of libraries

* Fri Jul 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt6
- Avoided conflict with metis

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt5
- Added link parmetis.pc -> metis.pc

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt4
- Added shared libraries

* Sun Aug 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt3
- Added pkg-config file
- Fixed "format not a string literal and no format arguments"

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2
- Rebuild with PIC

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus


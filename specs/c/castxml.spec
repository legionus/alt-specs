%define _unpackaged_files_terminate_build 1

Name:    castxml
Version: 0.0.1.20180321
Release: alt2%ubt
Summary: C-family abstract syntax tree XML output tool
Group:   Development/Other

# The main program is Apache 2.0
# src/kwsys/* is BSD
License: Apache-2.0 and BSD
URL:     https://github.com/CastXML/CastXML

# https://github.com/CastXML/CastXML.git
Source:	%name-%version.tar

# Link against the shared llvm library (one common library).
Patch1: %name-fedora-shared.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake ctest gcc-c++
BuildRequires: llvm-devel lld
# The llvm cmake files get confused if the static libraries are
# not present even though we don't link against them.
BuildRequires: llvm-devel-static
BuildRequires: clang-devel
# Required clang libraries are built statically at the moment
BuildRequires: clang-devel-static
BuildRequires: libedit-devel
BuildRequires: zlib-devel
BuildRequires: python-module-sphinx
BuildRequires: /proc

Requires: /proc

Obsoletes: gccxml

%description
Parse C-family source files and optionally write a subset of the
Abstract Syntax Tree (AST) to a representation in XML.

Source files are parsed as complete translation units using the clang
compiler. XML output is enabled by the --castxml-gccxml option and
produces a format close to that of gccxml. Future versions of castxml
may support alternative output formats.

%prep
%setup
%patch1 -p1

# LLVM_LIBRARY_DIRS does not work, and can not be overridden with -D flag
#sed 's!${LLVM_LIBRARY_DIRS}!${LLVM_LIBRARY_DIR}!' -i CMakeLists.txt

%build
%remove_optflags -frecord-gcc-switches
export CC=clang
export CXX=clang++
%cmake_insource -DCastXML_INSTALL_DOC_DIR:STRING=share/doc/%name \
       -DCastXML_INSTALL_MAN_DIR:STRING=share/man \
       -DCLANG_RESOURCE_DIR:PATH=$(clang -print-file-name=include)/.. \
       -DBUILD_TESTING:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON \
       -DCMAKE_EXE_LINKER_FLAGS:STRING=-fuse-ld=lld \
       -DLLVM_DIR=$(llvm-config --cmakedir)
%make

%install
%make install DESTDIR=%buildroot
rm -f %buildroot%_datadir/doc/%name/LICENSE
rm -f %buildroot%_datadir/doc/%name/NOTICE

%check
ctest

%files
%_bindir/castxml
%_man1dir/castxml.1*
%dir %_datadir/%name
%_datadir/%name/clang
%_datadir/%name/detect_vs.c
%_datadir/%name/detect_vs.cpp
%_datadir/%name/empty.c
%_datadir/%name/empty.cpp
%doc LICENSE NOTICE

%changelog
* Fri Apr 20 2018 L.A. Kostis <lakostis@altlinux.ru> 0.0.1.20180321-alt2%ubt
- Use LLD as linker (as ld doesn't understand LTO code generated by LLVM).

* Mon Apr 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1.20180321-alt1%ubt
- Updated to new version from VCS.

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1.20170823-alt2%ubt
- Rebuilt with support of %%ubt macro.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1.20170823-alt1
- Initial build for ALT.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20170301gitfab9c47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.1-0.17.20170301gitfab9c47
- Rebuild for LLVM4

* Wed Mar 15 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.16.20170301gitfab9c47
- New git snapshot
- Remove bundled provides for kwsys components - no longer used
- Rebuild for LLVM 3.9 (Fedora 25)

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.15.20170113gite7252f5
- New git snapshot

* Mon Nov 07 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.14.20161006git05db76f
- Rebuild for LLVM 3.9 (Fedora 26)

* Tue Oct 25 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1-0.13.20161006git05db76f
- New git snapshot

* Fri Jul 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.12.20160617gitd5934bd
- New git snapshot

* Thu May 26 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.11.20160510git9a83414
- New git snapshot

* Thu Feb 25 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.10.20160125gitfc71eb9
- Adjust to llvm library changes again (the split was revoked)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20160125gitfc71eb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.8.20160125gitfc71eb9
- New git snapshot
- Properly adjust to the new llvm library split

* Wed Jan 27 2016 Adam Jackson <ajax@redhat.com> 0.1-0.7.20150924git552dd69
- Rebuild for llvm 3.7.1 library split

* Fri Sep 25 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.6.20150924git552dd69
- Adjust gccxml obsolete version

* Thu Sep 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.5.20150924git552dd69
- New git snapshot
- Allow warnings about guessing the float ABI during tests (fixes tests on arm)

* Thu Sep 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.4.20150902git7acd634
- New git snapshot

* Fri Aug 21 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.3.20150820git2e55b35
- New git snapshot
- Upstream has deleted the parts of the bundled kwsys sources that are not
  used by castxml from the source repository
- Add bundled provides for the remaining kwsys components according to
  revised FPC decision 2015-08-20
  https://fedorahosted.org/fpc/ticket/555

* Fri Aug 07 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.2.20150807git8a08a44
- New git snapshot
- Unbundle kwsys library according to FPC decision 2015-08-06
  https://fedorahosted.org/fpc/ticket/555

* Tue Apr 14 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.1-0.1.20150414git43fa139
- First packaging for Fedora

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libQGLViewer
Version:        2.6.4
Release:        alt1_1
Summary:        Qt based OpenGL generic 3D viewer library

Group:          System/Libraries
License:        GPLv2 with exceptions or GPLv3 with exceptions 
URL:            http://www.libqglviewer.com/index.html
Source0:        http://www.libqglviewer.com/src/%{name}-%{version}.tar.gz

# QGLViewer/VRender/gpc.cpp uses exit(0) to "abort" from a failure of malloc
# Use abort() instead.
Patch0:         libQGLViewer-2.6.3-exit.patch
# libQGLViewer .pro files explicitely remove "-g" from compile flags. Make
# them back.
Patch1:         libQGLViewer-2.6.3-dbg.patch
Patch2:         libQGLViewer-2.6.4-qreal.patch

BuildRequires:  libqt4-declarative libqt4-devel qt4-designer qt4-doc-html qt5-declarative-devel qt5-designer qt5-tools qt5-base-devel
Source44: import.info
Patch33: libQGLViewer-alt-glu.patch

%description
%{name} is a C++ library based on Qt that eases the creation of OpenGL
3D viewers. It provides some of the typical 3D viewer functionality, such
as the possibility to move the camera using the mouse, which lacks in most
of the other APIs. Other features include mouse manipulated frames,
interpolated key-frames, object selection, stereo display, screenshot saving
and much more. It can be used by OpenGL beginners as well as to create
complex applications, being fully customizable and easy to extend.

%package        qt5
Summary:        Qt5 version of %{name}
Group:          Development/Other
Requires:       libqt5-concurrent libqt5-core libqt5-dbus libqt5-network libqt5-sql libqt5-test libqt5-xml

%description    qt5
%{name} is a C++ library based on Qt that eases the creation of OpenGL
3D viewers. It provides some of the typical 3D viewer functionality, such
as the possibility to move the camera using the mouse, which lacks in most
of the other APIs. Other features include mouse manipulated frames,
interpolated key-frames, object selection, stereo display, screenshot saving
and much more. It can be used by OpenGL beginners as well as to create
complex applications, being fully customizable and easy to extend.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       libqt4-declarative qt4-designer qt4-doc-html qt5-designer qt5-tools

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt5-devel
Summary:        Development files for %{name} using Qt5
Group:          Development/Other
Requires:       %{name}-qt5 = %{version}-%{release}

%description    qt5-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} and Qt5.


%package doc
Summary: API documentation, demos and example programs for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .exit
%patch1 -p1 -b .dbg
%patch2 -p0 -b .qreal

# Fix permissions
chmod a-x examples/*/*.vcproj

%patch33 -p1
rm -rf ../%{name}-%{version}-qt5
cp -a ../%{name}-%{version} ../%{name}-%{version}-qt5

%build

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%{!?_qt4_qmake: %define _qt4_qmake /usr/bin/qmake-qt4}
%{!?qmake_qt4: %define qmake_qt4 \
  qmake-qt4 \\\
  QMAKE_CFLAGS_DEBUG="${CFLAGS:-%optflags}" \\\
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_DEBUG="${CXXFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-%optflags}" \\\
  QMAKE_LFLAGS_DEBUG="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_STRIP=
}
%{!?_qt5_qmake: %define _qt5_qmake /usr/bin/qmake-qt5}
%{!?qmake_qt5: %define qmake_qt5 \
  qmake-qt5 \\\
  QMAKE_CFLAGS_DEBUG="${CFLAGS:-%optflags}" \\\
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_DEBUG="${CXXFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-%optflags}" \\\
  QMAKE_LFLAGS_DEBUG="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_STRIP=
}

cd QGLViewer
%{qmake_qt4} \
          LIB_DIR=%{_libdir} \
          DOC_DIR=%{_docdir}/%{name} \
          INCLUDE_DIR=%{_includedir} \
          TARGET_x=%{name}-qt4.so.%{version}
# The TARGET_x variable gives the SONAME. However, qmake behavior is not
# correct when the SONAME is customized: it create wrong symbolic links
# that must be cleaned after the installation.

%make_build

cd ../designerPlugin
%{qmake_qt4} LIB_DIR=../QGLViewer
%make_build

cd ../../%{name}-%{version}-qt5/QGLViewer
qmake-qt5 \
    LIB_DIR=%{_libdir} \
    DOC_DIR=%{_docdir}/%{name} \
    INCLUDE_DIR=%{_includedir} \
    TARGET_x=%{name}-qt5.so.%{version}
# The TARGET_x variable gives the SONAME. However, qmake behavior is not
# correct when the SONAME is customized: it create wrong symbolic links
# that must be cleaned after the installation.

%make_build

%install
cd QGLViewer
make -f Makefile -e INSTALL_ROOT=$RPM_BUILD_ROOT install_target install_include STRIP=/usr/bin/true
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt4.prl

# Clean symbolic links
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt4.so.?.? \
   $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt4.so.%{version}\\*

cd ../designerPlugin
make -e INSTALL_ROOT=$RPM_BUILD_ROOT install STRIP=/usr/bin/true

cd ../../%{name}-%{version}-qt5/QGLViewer
make -f Makefile -e INSTALL_ROOT=$RPM_BUILD_ROOT install_target install_include STRIP=/usr/bin/true
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.prl
# Clean symbolic links
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.so.?.?
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.so.%{version}\\* || true


%files
%doc README LICENCE CHANGELOG GPL_EXCEPTION
%{_libdir}/libQGLViewer-qt4.so.%{version}

%files devel
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer-qt4.so
%{_libdir}/qt4/plugins/designer/libqglviewerplugin.so

%files qt5
%doc README LICENCE CHANGELOG GPL_EXCEPTION
%{_libdir}/libQGLViewer-qt5.so.%{version}

%files qt5-devel
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer-qt5.so

%files doc
%doc doc
%doc examples

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.4-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_1
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_8
- new version

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_5
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_4
- update to new fc release

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.9-alt2_1.1
- Fixed build

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.9-alt1_1
- initial import by fcimport


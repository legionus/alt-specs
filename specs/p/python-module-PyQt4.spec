%define oname PyQt4

%def_with python3

Name: python-module-%oname
Version: 4.12.1
Release: alt3%ubt
Summary: Python bindings for Qt4
License: GPL
Group: Development/Python

%setup_python_module %oname

Source0: PyQt-x11-gpl.tar
URL: http://www.riverbankcomputing.co.uk/software/pyqt

#BuildPreReq: %py_package_dependencies sip-devel >= 4.8.1
#BuildPreReq: %py_package_dependencies dbus-devel

%add_python_req_skip Compiler

BuildRequires(pre): rpm-build-ubt python-module-sip-devel
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: elfutils fontconfig libGL-devel libX11-devel libXext-devel libdbus-devel libgpg-error libgst-plugins1.0 libjson-c libqt4-clucene libqt4-core libqt4-dbus libqt4-declarative libqt4-designer libqt4-devel libqt4-gui libqt4-help libqt4-location libqt4-multimedia libqt4-network libqt4-opengl libqt4-script libqt4-scripttools libqt4-sensors libqt4-sql libqt4-svg libqt4-test libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel pkg-config python-base python-devel python-module-dbus python-module-sip python-modules python-modules-compiler python-modules-logging python-modules-xml python3 python3-base python3-dev python3-module-sip
BuildRequires: gcc-c++ libqt4-webkit-devel phonon-devel python-module-dbus-devel

#BuildRequires: gcc-c++ libqt4-devel lout
#BuildPreReq: python-module-qscintilla2-qt4-devel libqscintilla2-qt4-devel
#BuildRequires: python-module-sip-devel python-devel
#BuildPreReq: python-module-dbus-devel phonon-devel

%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
Requires: python-module-sip = %sipver2

%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-sip-devel
#BuildRequires: python3-devel python3-module-sip-devel
#BuildPreReq: python3-module-dbus-devel
#BuildPreReq: python3-module-qscintilla2-qt4-devel
#BuildPreReq: python3-module-sip-devel
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

%description
Python bindings for the Qt4 C++ class library.  Also includes a PyQt4 backend
code generator for Qt4 Designer.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 bindings for Qt4
Group: Development/Python3
%add_python3_req_skip Compiler
Requires: python3-module-sip = %sipver3

%description -n python3-module-%oname
Python bindings for the Qt4 C++ class library.  Also includes a PyQt4 backend
code generator for Qt4 Designer.

%package -n python3-module-%oname-devel
Requires: python3-module-%oname = %version-%release
Summary:  Sip files for %name (Python 3)
Group: Development/Python3
%py3_provides %oname-devel

%description -n python3-module-%oname-devel
Sip files for PyQt4 to build extension
%endif

%package devel
Requires: %name = %version-%release
Summary:  Sip files for %name
Group: Development/Python
%py_package_provides %modulename-devel = %version-%release

%description devel
Sip files for PyQt4 to build extension

%package examples
Summary: PyQt4 examples
Group: Development/Python
BuildArch: noarch
Requires: %name
%py_package_provides %modulename-examples = %version-%release

%description examples
This package contains PyQt4 examples

%package doc
Summary: PyQt4 docs
Group: Development/Python
BuildArch: noarch
Requires: %name
%py_package_provides %modulename-examples = %version-%release

%description doc
This package contains PyQt4 docs

%prep
%setup -n PyQt-x11-gpl
subst 's|/lib/libpython|/%_lib/libpython|g' configure*.py
subst 's|/lib" |/%_lib" |g' configure*.py
subst 's|#include <QTextStream>|#include <QTextStream>\n#define QT_SHARED\n|g' \
	configure*.py
find . -type f -name \*.pro -o -name '*.pro-in' |while read f; do
cat >> $f << 'E_O_F'
QMAKE_CFLAGS += %optflags %optflags_shared
QMAKE_CXXFLAGS += %optflags %optflags_shared
E_O_F
done

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export QT4DIR=%_qt4dir
%add_optflags -I%_includedir/kde4 -I%_includedir/kde4/phonon
%add_optflags -I$PWD/qpy/QtGui

#cp -fR ../PyQt-x11-gpl ../_tmp_
#pushd ../_tmp_
#echo 'yes' | python configure.py \
#	--debug \
#	--verbose \
#	-q %_qt4dir/bin/qmake \
#	-d %python_sitelibdir \
#	-p %_qt4dir/plugins \
#	-a --confirm-license \
#	--qsci-api \
#	--enable=designer-plugin \
#	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
#popd

#echo 'yes' | python configure-ng.py \
echo 'yes' | python configure.py \
	--debug \
	--verbose \
	-q %_qt4dir/bin/qmake \
	-d %python_sitelibdir \
	-a --confirm-license \
	--qsci-api \
	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
for i in $(find ./ -name Makefile); do
	sed -i 's|-Wl,-rpath,|-I|g' $i
done
%make_build

%if_with python3
pushd ../python3
echo 'yes' | python3 configure.py \
	--debug \
	--verbose \
	-q %_qt4dir/bin/qmake \
	-d %python3_sitelibdir \
	-p %_qt4dir/plugins \
	-a --confirm-license \
	--qsci-api \
	--no-designer-plugin \
	--sipdir=%_datadir/sip3/%oname \
	--qsci-api-destdir=%_datadir/qt4/qsci3 \
	CFLAGS+="%optflags" CXXFLAGS+="%optflags"
for i in $(find ./ -name Makefile); do
	sed -i 's|lpython3\.2|lpython3.2mu|g' $i
done
for i in $(find ./ -name Makefile); do
	sed -i 's|-Wl,-rpath,|-I|g' $i
done
%make_build
popd
%endif

%install
%if_with python3
pushd ../python3
%makeinstall_std INSTALL_ROOT=%buildroot
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
rm -fR %buildroot%python3_sitelibdir/%oname/uic/port_v2
%endif

%makeinstall_std INSTALL_ROOT=%buildroot
rm -rf %buildroot%python_sitelibdir/%oname/uic/port_v3

#install -m644 ../_tmp_/pyqtconfig.py \
#	%buildroot%python_sitelibdir/%oname/

##wait ##
install -d %buildroot/usr/share/sip/PyQt4/Qsci \
	PyQt-x11-gpl/sip/QtGui
#bzip2 ChangeLog

%files
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/PyQt4/pyqtconfig.*

%files devel
%_qt4dir/plugins/designer/libpyqt4.so
%python_sitelibdir/PyQt4/pyqtconfig.*
%dir %_datadir/sip
%_datadir/sip/*
%dir %_datadir/qt4
%_datadir/qt4/qsci

%files doc
%doc doc/*
#doc NEWS README ChangeLog* THANKS
%doc NEWS README THANKS

%files examples
%doc examples

%if_with python3
%files -n python3-module-%oname
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/PyQt4/pyqtconfig.*

%files -n python3-module-%oname-devel
%python3_sitelibdir/PyQt4/pyqtconfig.*
%dir %_datadir/sip3
%_datadir/sip3/*
%dir %_datadir/qt4
%_datadir/qt4/qsci3
%endif

%changelog
* Wed Aug 22 2018 Sergey V Turchin <zerg@altlinux.org> 4.12.1-alt3%ubt
- move pyqtconfig to devel subpackage

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.12.1-alt2.S1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Vitaly Lipatov <lav@altlinux.ru> 4.12.1-alt2.S1.1
- NMU: autorebuild with python-module-sip 4.9.7

* Fri Oct 06 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.12.1-alt2%ubt
- Set strict require to sip version we build with.

* Thu Oct 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.12.1-alt1%ubt
- Updated to upstream version 4.12.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.11.4-alt2.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.11.4-alt2.1
- NMU: Use buildreq for BR.

* Mon Jul 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.4-alt2
- Rebuilt with new SIP

* Mon Jun 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.4-alt1
- Version 4.11.4

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.3-alt3
- Added PyQt4.phonon module (ALT #30697)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.3-alt2
- Rebuilt with new SIP

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.3-alt1
- Version 4.11.3

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.1-alt2
- Added module for Python 3 (ALT #30196)

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.1-alt1
- Version 4.11.1

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11-alt3
- Rebuilt with new SIP

* Sun Jun 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11-alt2
- Added pyqtconfig.py

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11-alt1
- Version 4.11

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.4-alt1
- Version 4.10.4

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.3-alt1
- Version 4.10.3 (ALT #29177)

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.6-alt3
- Fixed for arm (thnx sbolshakov@)

* Fri Dec 28 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.9.6-alt2
- Added missing source files

* Fri Dec 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.6-alt1
- Version 4.9.6

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.4-alt1
- Version 4.9.4

* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.1-alt6
- Added PyQt4.QtCore, PyQt4.QtGui and PyQt4.QtNetwork symbols into
  PyQt4.Qt (ALT #27424)

* Wed May 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.1-alt5
- Built module for Python 3 with qscintilla2

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.1-alt4
- Added module for Python 3 (bootstrap)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.9.1-alt3.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.1-alt3
- Fixed build

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.1-alt2
- Rebuilt with QScintilla2 2.6.1

* Tue Feb 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.9.1-alt1
- Version 4.9.1

* Tue Jan 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9-alt1
- Version 4.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.8.4-alt1.1
- Rebuild with Python-2.7

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt1
- Version 4.8.4

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.3-alt2
- Rebuilt with debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.3-alt1
- Version 4.8.3

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.1-alt1
- Version 4.8.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.4-alt1
- Version 4.7.4

* Wed Jul 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.7-alt3
- Rebuilt with qt 4.7

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.7-alt1.M51.1
- build for M51

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt2
- Set devel, doc and examples packages as noarch

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt1
- Version 4.7

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.4-alt1.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.4-alt1
- Update to new release

* Mon Jul 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.2-alt1
- Update to new release

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5.1-alt1
- Update to new release

* Tue Nov 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.4-alt1
- New version

* Wed Aug 06 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.2-alt2
- Push rlz@ build to Sisyphus

* Sat Jun 07 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 4.4.2-alt1
- New version

* Mon Dec 31 2007 Ivan Fedorov <ns@altlinux.org> 4.3.3-alt1
- 4.3.3

* Sun Nov 04 2007 Alexey Morsov <swi@altlinux.ru> 4.3.1-alt1
- 4.3.1
- total fix build on x86_64

* Wed Sep 05 2007 Ivan Fedorov <ns@altlinux.org> 4.3-alt3
- Fix build on x86_64

* Mon Sep 03 2007 Ivan Fedorov <ns@altlinux.org> 4.3-alt2
- Fix building bug

* Fri Aug 31 2007 Ivan Fedorov <ns@altlinux.org> 4.3-alt1
- 4.3

* Thu Dec 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Fri Sep 08 2006 Ivan Fedorov <ns@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Mon Jun 12 2006 Ivan Fedorov <ns@altlinux.ru> 4.0-alt1
- 4.0 release

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.0.0-alt0.snap20060408.0
- 4.0.0-snapshot-20060408

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.0.0-alt0.snap20060328.0
- 4.0.0-snapshot-20060328

* Sat Dec 31 2005 Ivan Fedorov <ns@altlinux.ru> 4.0.0-alt0.snap20051229.0
- 4.0.0-snapshot-20051229

* Wed Dec 07 2005 Ivan Fedorov <ns@altlinux.ru> 3.15.1-alt1
- 3.15.1

* Thu Jun 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1.1.1
- Rebuilt with libqt3.

* Thu Jun 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1.1
- Rebuild with new libgnutls.so.11 .

* Tue Apr 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1.1
- Rebuilt with libqt3

* Fri Mar 25 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.14.1-alt1.1
- Rebuilt with libqt3

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 3.14.1-alt1
- 3.14.1
- rebuild with python 2.4

* Sat Mar 05 2005 Ivan Fedorov <ns@altlinux.ru> 3.14-alt2
- small fix spec

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 3.14-alt1
- 3.14

* Fri Feb 04 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.13-alt4.1.1
- Rebuilt with qt3-3.3.4

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.13-alt4.1
- Rebuilt with libstdc++.so.6.

* Mon Dec 27 2004 Ivan Fedorov <ns@altlinux.ru> 3.13-alt4
- fixing requires (libqt3)

* Sun Dec 12 2004 Ivan Fedorov <ns@altlinux.ru> 3.13-alt3
- fix spec to be compatible with python policy

* Wed Oct 27 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.13-alt2
- fix sip>=4.1 requires bug (#5323)

* Fri Sep 24 2004 Eugene V. Horohorin <genix@altlinux.org> 3.13-alt1
- new release

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.12-alt2
- new buildrequires

* Thu Sep 02 2004 Eugene V. Horohorin <genix@altlinux.ru> 3.12-alt1
- new release
- removed macros (_findprov_lib_path)
- spec cleanup

* Fri Aug 01 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt2
- added _findprov_lib_path macro to temporary solve problem with dependencies

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt1
- new release

* Mon Apr 28 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt0.1
- New build from snapshot

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt2
- comment patch added ( this comment line needs for eric )
- add devel package ( need to build some extension of qt )

* Tue Dec 17 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt1
- build with qscintilla
- new release

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt0.1.20021205
- correct version

* Sat Dec 07 2002 Serge Sergeev <ssv@altlinux.ru> 20021205-alt1
- build from snapshot
- add documentation

* Tue Nov 05 2002 Serge Sergeev <ssv@altlinux.ru> 3.4-alt1
- new release

* Wed Sep 04 2002 Serge Sergeev <ssv@altlinux.ru> 3.3.2-alt1
- new release

* Thu Jul 25  2002 <sergeyssv@mail.ru>
- Initial release

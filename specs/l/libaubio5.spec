%define origname aubio
%define sover 5
%def_enable python

Name: libaubio%sover
Version: 0.4.7
Release: alt1
Summary: Aubio is a library for real time audio labelling
Url: http://www.aubio.org/
License: GPL
Group: System/Libraries

# git://git.aubio.org/git/aubio/
Source: %origname-%version.tar
Patch0: %name-%version-alt.patch

# Automatically added by buildreq on Thu Nov 06 2008
BuildRequires: docbook-to-man jackit-devel libfftw3-devel libsamplerate-devel libsndfile-devel

BuildPreReq: python-modules waf >= 1.9.12 libavcodec-devel libavformat-devel
BuildPreReq: libavresample-devel txt2man doxygen python-devel libswresample-devel
BuildPreReq: libnumpy-devel

%description
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

A few examples of applications are provided in examples/ and python/:
 - aubioonset output the onset detected,
 - aubionotes emits midi-like notes,
 - aubiocut is a python script that takes an input sound and creates one new
   sample at each detected onset or beat,
 - aubiopitch is a python script to extract pitch tracks from sound files.

%if_enabled python
%package -n python-module-%origname
Group: Development/Python
Summary: Python bindings to %name
Requires: %name = %version-%release

%description -n python-module-%origname
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains the Python bindings required for
building Python programs based on %name.
%endif

%package devel
Group: Development/C
Summary: Development files of %name
Requires: %name = %version-%release
Conflicts: lib%origname-devel

%description devel
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains the C headers and documentation required for
building programs based on %name.

%package examples
Group: Sound
Summary: Examples of %name
Conflicts: lib%origname-examples

%description examples
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains
A few examples of applications are provided in examples/ and python/:
 - aubioonset output the onset detected,
 - aubionotes emits midi-like notes,
 - aubiocut is a python script that takes an input sound and creates one new
   sample at each detected onset or beat,
 - aubiopitch is a python script to extract pitch tracks from sound files.

aubioonset and aubionotes can work either off-line or online, outputting the
results on the console or playing a wood-block sound at each detected onset.
Both Python scripts can plot the results with Gnuplot.

%package devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch detection,
tapping the beat and producing midi streams from live audio.

This package contains documentation for %name.

%prep
%setup -n %origname-%version
%patch0 -p1

rm -fR waflib

%build
waf configure --prefix=%prefix --libdir=%_libdir
waf build -vv

%if_enabled python
%python_build_debug
%endif

%install
waf install --destdir=%buildroot

%if_enabled python
%python_install
%endif

%files
%doc AUTHORS ChangeLog README.md doc/*
%_libdir/*.so.%{sover}*

%if_enabled python
%files -n python-module-%origname
%doc python/README.md python/demos
%python_sitelibdir/*
%endif

%files devel
%_includedir/%origname
%_libdir/*.so
%_pkgconfigdir/%origname.pc

%files examples
%_bindir/*
#_datadir/sounds/%origname
%_man1dir/*

%files devel-docs
%_docdir/lib%origname-doc

%changelog
* Tue Oct 09 2018 Anton Farygin <rider@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 0.4.6-alt2
- rebuilt for ffmpeg-4.0

* Mon Nov 13 2017 Anton Farygin <rider@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Sun Jun 04 2017 Anton Farygin <rider@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt2.git20140312.1
- (AUTO) subst_x86_64.

* Sat Mar 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt2.git20140312
- rebuilt with recent libav

* Sat Sep 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140312
- Version 0.4.1

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.2
- Fixed build

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1.1
- rebuild for set:provides by request of mithraen

* Thu Nov 06 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.3.2-alt1
- 1st version for Sisyphus
- Python bindings are OFF
- build without Lash and PureData

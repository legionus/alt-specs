Name: ale
Version: 0.9.0.3
Release: alt9

Summary: Combining multiple inputs representing the same scene
License: GPLv3+
Group: Graphics

URL: http://auricle.dyndns.org/ALE/
Source: http://auricle.dyndns.org/ALE/download/ale-%version.tar.gz
Patch: ale-0.9.0.3-alt-perl522.patch
Patch1: alt-0.9.0.3-debian-fix-string-issue.patch

# Automatically added by buildreq on Tue Mar 08 2011
BuildRequires: bzlib-devel fontconfig-devel gcc-c++ libGraphicsMagick-devel libImageMagick-devel libXext-devel libXt-devel libfftw3-devel libfreetype-devel libjpeg-devel liblcms-devel liblqr-devel libtiff-devel zlib-devel
BuildRequires: libgomp-devel

%description
ALE (Anti-Lamenessing Engine) is an image-processing program used for
tasks such as super-resolution, deblurring, image stacking, noise
reduction, and anti-aliasing. Its principle of operation is synthetic
capture: combining multiple inputs representing the same scene.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc scripts
%_bindir/*
%_man1dir/*

%changelog
* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt9
- rebuilt for ImageMagick

* Fri Jan 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0.3-alt8
- Updated build dependencies.

* Thu Aug 17 2017 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt7
- rebuild with new ImageMagick
- add patch from debian with fixes for fprintf

* Fri May 06 2016 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt6
- Rebuild with new libImageMagick

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.0.3-alt5.1
- bugfixes for perl 5.22 (ale-0.9.0.3-alt-perl522.patch)

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt5
- Rebuild with new libImageMagick

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt4
- Rebuild with new libImageMagick

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt3.1
- Rebuild with new libImageMagick

* Tue Mar 08 2011 Victor Forsiuk <force@altlinux.org> 0.9.0.3-alt3
- Refresh BuildRequires.

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.9.0.3-alt2.1
- rebuild with new ImageMagick

* Wed Jul 14 2010 Victor Forsiuk <force@altlinux.org> 0.9.0.3-alt2
- Build with libMagickCore.so.3.

* Thu Oct 01 2009 Victor Forsyuk <force@altlinux.org> 0.9.0.3-alt1
- Initial build.

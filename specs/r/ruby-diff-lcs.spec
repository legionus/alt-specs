# vim: set ft=spec : -*- rpm-spec -*-

%define pkgname diff-lcs

Name:    ruby-%pkgname
Version: 1.2.5
Release: alt1.1

Summary: Port of Algorithm::Diff
Group:   Development/Ruby
License: MIT
Url:     http://diff-lcs.rubyforge.org/
#VCS:	 https://github.com/halostatue/diff-lcs.git

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Aug 25 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt
longest common subsequence (LCS) algorithm to compute intelligent
differences between two sequenced enumerable containers. The
implementation is based on Mario I. Wolczko's Smalltalk version (1.2,
1993) and Ned Konz's Perl version (Algorithm::Diff).

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -q -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib tests/*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc *.rdoc
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/Diff*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.2-alt2
- Rebuilt with Ruby 1.9

* Mon Aug 25 2008 Sir Raorn <raorn@altlinux.ru> 1.1.2-alt1
- Built for Sisyphus


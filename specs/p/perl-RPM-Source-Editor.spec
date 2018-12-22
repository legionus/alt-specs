%define module RPM-Source-Editor
%def_without hashertarbuild

Name: perl-%module
Version: 0.9222
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for src.rpm and spec file editing
Group: Development/Perl
License: GPL-1.0-only or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/RPM-Source-Editor.git

# due to rpmbuild -bE
# Recommends: rpm-build

# Automatically added by buildreq on Wed Nov 06 2010
BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl(RPM/Vercmp.pm) perl(RPM/Header.pm) perl(Clone.pm) perl(Tie/Hash.pm)
# for RPM::Source::Tools
BuildRequires: perl(RPM/uscan.pm) perl(Pod/Strip.pm) perl-Source-Shared-Resource
# for srpm-spec-inject-patches
BuildRequires: perl(Gear/Rules.pm)

Obsoletes: hashertarbuild < 0.73
Conflicts: hashertarbuild < 0.73

# recommends, in fact
Requires: pax

%description
Perl extension for editing src.RPMs and spec files

%if_with hashertarbuild
%package -n hashertarbuild
Group: Development/Other
Summary: a tool to create source tarballs for hasher
Requires: %name = %version-%release

%description -n hashertarbuild
A tool to create rpm-based source tarballs for hasher.
Sometimes rpmbuild -bs --nodeps does not work due to macros abcent. 
Use hashertarbuild <spec> to create source tarball ready for hasher.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build 
#INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

install -m755 -D hashertarbuild %buildroot%_bindir/hashertarbuild
for i in hashertarbuild; do
    pod2man  --name $i --center 'hashertarbuild' --section 1 --release %version $i > $i.1
done

mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/srpmtools/hooks

%files
%doc Changes
#doc README
%_bindir/srpm*
%perl_vendor_privlib/RPM*
#perl_vendor_man3dir/*
%dir %_datadir/srpmtools
%dir %_datadir/srpmtools/hooks
%_man1dir/srpm-spec-inject-patches*
%_man1dir/srpmtool*
%_man1dir/srpmnmu*

#files -n hashertarbuild
%_bindir/hashertarbuild
%_man1dir/hashertarbuild*

%changelog
* Sun Oct 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.9222-alt1
- new version

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.9221-alt1
- bugfix release (minor bugs)

* Mon Sep 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9220-alt1
- better GEARDIR support in PkgWriter

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.9219-alt1
- batch hooks support

* Mon Sep 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.9218-alt1
- new version

* Thu Aug 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.9217-alt1
- hack around %ubt thanks to grenka@

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9216-alt1
- new version

* Wed Jul 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.9215-alt1
- new version

* Mon Jul 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.9214-alt1
- repocop diff writer support

* Mon Jul 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.9213-alt1
- bugfix for diff writer

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.9212-alt1
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.9211-alt1
- changed defaults for nmu to nmuadd

* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.9210-alt1
- added subst_body_ee thanks to grenka@

* Fri Mar 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.9209-alt1
- %ubt support for new version

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.9208-alt1
- new version

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.9207-alt1
- new version

* Fri Feb 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.9206-alt1
- bugfix release

* Fri Feb 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.9205-alt1
- new version

* Thu Jan 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.9204-alt1
- new version

* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.9203-alt1
- new version

* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.9202-alt1
- new version

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.9201-alt1
- new version

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9200-alt1
- bugfix release
